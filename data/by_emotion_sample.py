from pathlib import Path
from pprint import pprint

from tqdm import tqdm
import pandas as pd
import re
import numpy as np
from server import getSongAnalyses
from collections import defaultdict
from math import ceil, log10
import pickle
from collections import Counter
from organize_schubert_data_by_harmony import getPairedChordLocalKeyPaths

pitchClasses = {
    "B#": 0,
    "C": 0,
    "C#": 1,
    "Db": 1,
    "D": 2,
    "D#": 3,
    "Eb": 3,
    "E": 4,
    "Fb": 4,
    "E#": 5,
    "F": 5,
    "F#": 6,
    "Gb": 6,
    "G": 7,
    "G#": 8,
    "Ab": 8,
    "A": 9,
    "A#": 10,
    "Bb": 10,
    "B": 11,
    "Cb": 11
}
diatonicPitchClasses = {
    n: i for i, n in enumerate(list("CDEFGAB"))
}
emotions = ["anger", "fear", "sadness", "none", "irony", "love", "joy"]
globalKeysDF = pd.read_csv(
    Path(
        ".\\Schubert_Winterreise_Dataset_v2-0\\02_Annotations\\ann_audio_globalkey.csv"
    ), sep=";"
)


def extractEmotionTimeSeries(
        songNumber: int,
        time_discretization: float = 0.1,
        toDistribution: bool = True
) -> pd.DataFrame:
    # Retrieve data from database
    response = getSongAnalyses(str(songNumber))
    # Find highest time analyzed across all analyses
    maxTime = max([float(time) for analysis in response['analyses'] for time in analysis["analysis"]])
    # Find the number of digits needed to round given the time_discretization parameter
    rounding_digits = round(-log10(time_discretization))
    # Set up a counter for number of emotions at each discretized time step
    times = {
        round(time, rounding_digits): Counter({
            emotion: 0 for emotion in emotions
        }) for time in np.arange(0, ceil(maxTime), time_discretization)
    }
    # Count emotions at each time step
    for analysis in response['analyses']:
        for time, emotion in analysis["analysis"].items():
            rounded_time = round(float(time), rounding_digits)
            times[rounded_time][emotion] += 1
    # Convert emotions to distribution if desired
    if toDistribution:
        for time, counts in times.items():
            distribution = {emotion: count / (sum(counts.values()) + 1e-100) for emotion, count in counts.items()}
            times[time] = distribution
    # Convert into a Pandas Dataframe object
    emotion_cols = {
        emotion: [
            times[time][emotion] for time in times
        ] for emotion in emotions
    }
    df = pd.DataFrame({
        "times": times.keys(),
        **emotion_cols
    })
    return df


def combineChordLocalKey(pathPair: tuple[Path, Path]):
    chordCSV, localKeyCSV = pathPair
    chordDF = pd.read_csv(chordCSV, sep=";")
    localKeyDF = pd.read_csv(localKeyCSV, sep=";")

    currKey = []
    for chordIdx, chordRow in chordDF.iterrows():
        for keyIdx, keyRow in localKeyDF.iterrows():
            if keyRow["start"] <= chordRow["start"] <= keyRow["end"]:
                letter, quality = keyRow["key"].split(":")
                currKey.append(letter)
                break

    # print(chordDF.head(20))
    # print(currKey)
    chordDF.insert(2, "localkey", currKey, True)
    # print(chordDF.head(20))
    return chordDF


def addRomanNumerals(df: pd.DataFrame, songNum: int, recording: str="HU33", annotationNum: int=1):
    paths = getPairedChordLocalKeyPaths(recording, annotationNum)
    chordCSV, localKeyCSV = paths[songNum-1]
    chordDF = pd.read_csv(chordCSV, sep=";")
    localKeyDF = pd.read_csv(localKeyCSV, sep=";")
    print(chordDF)
    print(localKeyDF)
    parseKeyRootQuality(chordDF, localKeyDF)


def parseKeyRootQuality(chordDF: pd.DataFrame, localKeyDF: pd.DataFrame, recording: str="HU33", songNum: int=2):
    #Extract the global key for the given recording
    globalKey = globalKeysDF.loc[globalKeysDF["PerformanceID"] == recording]
    if len(str(songNum)) == 1:
        songNum = f"0{songNum}"
    globalKey = globalKey.loc[globalKey["WorkID"] == f"Schubert_D911-{songNum}"]["key"].iloc[0].split(":")[0]
    globalKey = pitchClasses[globalKey]

    roots = []
    qualities = []
    localKeys = []
    for i, chordRow in chordDF.iterrows():
        #Determine local key of current chord
        localKey = None
        for j, keyRow in localKeyDF.iterrows():
            if float(keyRow["start"]) <= float(chordRow["end"]) <= float(keyRow["end"]):
                localKey = keyRow["key"].split(":")[0]
        if localKey is None:
            raise ValueError(f"Chord {chordRow['extended']} is not associated with a local key")
        localKey = (pitchClasses[localKey] - globalKey) % 12
        localKeys.append(localKey)

        #Determine roots of each chord with respect to local key
        rootName = chordRow["majmin"].split(":")[0]
        roots.append((pitchClasses[rootName] - localKey - globalKey) % 12)

        #Determine quality of each chord
        quality = chordRow["majmin"].split(":")[1]
        qualities.append(quality)

    print(roots)
    print(localKeys)
    chordDF.insert(2, "root", roots, True)
    chordDF.insert(2, "local_key", localKeys, True)
    chordDF.insert(2, "quality", qualities, True)
    chordDF.insert(2, "global_key", [globalKey for _ in range(len(localKeys))], True)
    print(chordDF)

def main():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    df = extractEmotionTimeSeries(songNumber=2, toDistribution=True)
    addRomanNumerals(df, songNum=2)


if __name__ == "__main__":
    main()
