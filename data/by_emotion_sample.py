from pathlib import Path
from pprint import pprint

from tqdm import tqdm
import pandas as pd
import re
import numpy as np
from server import getSongAnalyses
from collections import defaultdict
import enlighten
from math import ceil, log10, floor
import pickle
from collections import Counter
from data.organize_schubert_data_by_harmony import getPairedChordLocalKeyPaths
from DHMM.gatherMatrices import emotionConvolutionMLE
import librosa as lr
import matplotlib.pyplot as plt

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
repoPath = "C:/Users/88ste/OneDrive/Documents/GitHub/sentiment_tool/"
globalKeysDF = pd.read_csv(
    Path(
        repoPath,
        "data\\Schubert_Winterreise_Dataset_v2-0\\02_Annotations\\ann_audio_globalkey.csv"
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
        "time": times.keys(),
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


def addRomanNumerals(emotionDF: pd.DataFrame, songNum: int, recording: str= "HU33", annotationNum: int=1):
    paths = getPairedChordLocalKeyPaths(recording, annotationNum)
    chordCSV, localKeyCSV = paths[songNum-1]
    chordDF = pd.read_csv(chordCSV, sep=";")
    localKeyDF = pd.read_csv(localKeyCSV, sep=";")
    chordDF = parseKeyRootQuality(chordDF, localKeyDF)
    # print(emotionDF)
    # print(chordDF)
    localKeys = []
    roots = []
    qualities = []
    for i, emotionRow in emotionDF.iterrows():
        foundChord = False
        for j, chordRow in chordDF.iterrows():
            if float(chordRow["start"]) <= float(emotionRow["time"]) <= float(chordRow["end"]):
                localKeys.append(chordRow["local_key"])
                roots.append(chordRow["root"])
                qualities.append(chordRow["quality"])
                foundChord = True
                break
        if not foundChord:
            localKeys.append("none")
            roots.append("none")
            qualities.append("none")
    emotionDF.insert(1, "root", roots, True)
    emotionDF.insert(1, "local_key", localKeys, True)
    emotionDF.insert(1, "quality", qualities, True)
    emotionDF.insert(1, "global_key", [chordDF.iloc[0]["global_key"] for _ in range(len(localKeys))], True)
    return emotionDF


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
        if "dim" in chordRow["shorthand"]:
            quality = "dim"
        qualities.append(quality)


    chordDF.insert(2, "root", roots, True)
    chordDF.insert(2, "local_key", localKeys, True)
    chordDF.insert(2, "quality", qualities, True)
    chordDF.insert(2, "global_key", [globalKey for _ in range(len(localKeys))], True)
    return chordDF


def saveAlphas(windowSizes: list[int]):
    with enlighten.get_manager() as manager:
        pbar = manager.counter(total=24, desc="Songs", unit="songs", leave=False)

        for songNumber in range(1, 25):
            try:
                df = extractEmotionTimeSeries(songNumber=songNumber, toDistribution=True)
                df = addRomanNumerals(df, songNum=songNumber)
                emotionConvolutionMLE(df, f"song{songNumber}", 128)
                for ws in windowSizes:
                    emotionConvolutionMLE(df, f"song{songNumber}", windowSize=ws, manager=manager)
            except Exception as e:
                # print(e)
                continue
            pbar.update()


def addAlpha(df: pd.DataFrame, songNum: int, windowSize: int=128):
    with open(f"{repoPath}data/alphasByEmotionSample/windowSize_{windowSize}/song{songNum}_alphas.pickle", "rb") as f:
        df_alpha = pickle.load(f)
    df = pd.concat([df, df_alpha], axis=1).drop("index", axis=1)
    return df


def addPseudoRomanNumeral(df: pd.DataFrame):
    romans = []
    for i, row in df.iterrows():
        romans.append(f"{row['local_key']}:{row['root']}:{row['quality']}")
    df.insert(2, "romannumeral", romans, True)
    return df


def addMeasureNumbers(emotionDF: pd.DataFrame, songNum: int, recording: str="HU33"):
    if len(str(songNum)) == 1:
        songNum = f"0{songNum}"
    measureDF = pd.read_csv(
        f"C:\\Users\\88ste\\OneDrive\\Documents\\GitHub\\sentiment_tool\\data\\Schubert_Winterreise_Dataset_v2-0\\02_Annotations\\ann_audio_measure\\Schubert_D911-{songNum}_{recording}.csv",
        sep=";"
    )
    measures = []
    for i, emotionRow in emotionDF.iterrows():
        found = False
        for j, measureRow in measureDF.iterrows():
            if (j+1) >= len(measureDF) and float(measureRow["start"]) <= float(emotionRow["time"]):
                found = True
                measures.append(floor(measureRow["measure"]))
                break
            if float(measureRow["start"]) <= float(emotionRow["time"]) < float(measureDF.iloc[j+1]["start"]):
                measures.append(floor(measureRow["measure"]))
                found = True
                break
        if not found:
            measures.append(0)
    emotionDF.insert(1, "measure", measures, True)
    return emotionDF


def determineDynamicLevels(recording: str= "HU33", dynamicSampleEvery: float=0.1, noiseLevel: float=0.001, numDiscreteDynamics: int=4, plot: bool=False):
    loudest = []
    for songNum in range(1, 25):
        if len(str(songNum)) == 1:
            songNum = f"0{songNum}"
        file = f"C:\\Users\\88ste\\OneDrive\\Documents\\GitHub\\sentiment_tool\\data\\Schubert_Winterreise_Dataset_v2-0\\01_RawData\\audio_wav\\Schubert_D911-{songNum}_{recording}.wav"
        samples, sampsPerSec = lr.load(file)

        for time in range(0, len(samples), int(sampsPerSec * dynamicSampleEvery)):
            currLoudest = np.max(samples[time:time + sampsPerSec])
            if currLoudest > noiseLevel:
                loudest.append(currLoudest)

    maxLoud = max(loudest)
    bins = np.arange(0, maxLoud + 0.02, maxLoud / numDiscreteDynamics)
    print(bins)

    if plot:
        fig, ax = plt.subplots()
        plt.hist(loudest, bins=bins)
        if len(bins) < 10:
            plt.xticks(bins)
        plt.show()

    return bins


def main():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    # songNumber = 2
    #
    # df = extractEmotionTimeSeries(songNumber=songNumber, toDistribution=True)
    # df = addRomanNumerals(df, songNum=songNumber)
    # df = addAlpha(df, songNum=songNumber)
    # df = addPseudoRomanNumeral(df)
    # df = addMeasureNumbers(df, songNum=songNumber)
    # print(df)
    determineDynamicLevels(numDiscreteDynamics=25, plot=True)


if __name__ == "__main__":
    main()
