from pathlib import Path
from pprint import pprint

from tqdm import tqdm
import pandas
import pandas as pd
import re
from server import getSongAnalyses
from collections import defaultdict
import pickle

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


def getDiatonicSteps(tonic, toNote):
    n1 = tonic[0]
    n2 = toNote[0]
    dpc1 = diatonicPitchClasses[n1]
    dpc2 = diatonicPitchClasses[n2]
    count = 0
    while dpc2 != dpc1:
        count += 1
        dpc1 = (dpc1 + 1) % 7
    return count + 1


def getChromaticSteps(tonic, toNote):
    n1 = pitchClasses[tonic]
    n2 = pitchClasses[toNote]
    count = 0
    while n1 != n2:
        count += 1
        n1 = (n1 + 1) % 12
    return count


def getMostLikelyRomanNumeral(chromaticStepsAboveTonic: int):
    if chromaticStepsAboveTonic == 0: return "I"
    if chromaticStepsAboveTonic == 1: return "viio/ii"
    if chromaticStepsAboveTonic == 2: return "ii"
    if chromaticStepsAboveTonic == 3: return "bIII"
    if chromaticStepsAboveTonic == 4: return "iii"
    if chromaticStepsAboveTonic == 5: return "IV"
    if chromaticStepsAboveTonic == 6: return "viio/V"
    if chromaticStepsAboveTonic == 7: return "V"
    if chromaticStepsAboveTonic == 8: return "bVI"
    if chromaticStepsAboveTonic == 9: return "vi"
    if chromaticStepsAboveTonic == 10: return "bVII"
    if chromaticStepsAboveTonic == 11: return "vii"


def convertToSecondaryDom(rn: str):
    if rn == "I": return "V7/IV"
    if rn == "ii": return "V7/V"
    if rn == "bIII": return "V7/bVI"
    if rn == "iii": return "V7/vi"
    if rn == "IV": return "IV7"
    if rn == "V": return "V7"
    if rn == "bVI": return "V7/bII"
    if rn == "vi": return "V7/ii"
    if rn == "bVII": return "V7/bIII"
    if rn == "vii": raise ValueError("viio is a secondary dominant?")


def getScaleDegree(tonic, toNote):
    diatonicDistance = getDiatonicSteps(tonic, toNote)
    chromaticDistance = getChromaticSteps(tonic, toNote)

    if diatonicDistance == 1:
        if chromaticDistance == 0: return "n1"
        if chromaticDistance == 1: return "#1"
    if diatonicDistance == 2:
        if chromaticDistance == 1: return "b2"
        if chromaticDistance == 2: return "n2"
        if chromaticDistance == 3: return "#2"
    if diatonicDistance == 3:
        if chromaticDistance == 3: return "b3"
        if chromaticDistance == 4: return "n3"
    if diatonicDistance == 4:
        if chromaticDistance == 4: return "b4"
        if chromaticDistance == 5: return "n4"
        if chromaticDistance == 6: return "#4"
    if diatonicDistance == 5:
        if chromaticDistance == 6: return "b5"
        if chromaticDistance == 7: return "n5"
        if chromaticDistance == 8: return "#5"
    if diatonicDistance == 6:
        if chromaticDistance == 8: return "b6"
        if chromaticDistance == 9: return "n6"
        if chromaticDistance == 10: return "#6"
    if diatonicDistance == 7:
        if chromaticDistance == 10: return "b7"
        if chromaticDistance == 11: return "n7"
    raise NotImplementedError()


def getPairedChordLocalKeyPaths(identifier: str, annotatorNumber: int):
    annotationPath = Path("C:/Users/88ste/OneDrive/Documents/GitHub/sentiment_tool/data/Schubert_Winterreise_Dataset_v2-0/02_Annotations")
    pathChord = annotationPath / "ann_audio_chord"
    pathLocalKey = annotationPath / f"ann_audio_localkey-ann{annotatorNumber}"
    globChord = pathChord.glob(f"Schubert_D911-[0-9][0-9]_{identifier}.csv")
    globLocalKey = pathLocalKey.glob(f"Schubert_D911-[0-9][0-9]_{identifier}.csv")
    return list(zip(globChord, globLocalKey))


# TODO: OPTIONAL extend to include dominant 7ths, 9ths etc.
def parseShortHand(shorthand: str):
    letter, quality = shorthand.split(":")
    bass = letter
    if "/" in quality:
        quality, bass = quality.split("/")
    quality = re.sub("\(.+\)", "", quality)
    if "min" in quality:
        quality = "min"
    elif "maj" in quality:
        quality = "maj"
    elif "dim" in quality:
        quality = "dim"
    elif "7" in quality:
        quality = "dom"
    else:
        quality = "maj"

    return letter, quality, bass


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


def rnToFunction(rn, nextRN):
    if rn in ["vi", "bVI"] and nextRN in ["V", "viio"]:
        return "PD"
    if rn in ["i", "I", "iii", "bIII", "vi", "bVI"]:
        return "T"
    if rn in ["ii", "iio", "iv", "IV", "viio/V", "viio/ii"]:
        return "PD"
    if rn in ["v", "V", "viio", "vii", "bvii"]:
        return "D"

def rnToFunctionNoNext(rn):
    if rn in ["i", "I", "iii", "bIII", "vi", "bVI"]:
        return "T"
    if rn in ["ii", "iio", "iv", "IV", "viio/V", "viio/ii"]:
        return "PD"
    if rn in ["v", "V", "viio", "vii", "bvii"]:
        return "D"

def addRomanNumeral(df: pd.DataFrame):
    rns = []
    for i, row in df.iterrows():
        root, quality, bass = parseShortHand(row["shorthand"])
        chromaticSteps = getChromaticSteps(row["localkey"], root)
        mostLikelyRN = getMostLikelyRomanNumeral(chromaticSteps)
        # if quality == "dom":
        #     mostLikelyRN = convertToSecondaryDom(mostLikelyRN)
        if quality == "min":
            mostLikelyRN = mostLikelyRN.lower()
        # if quality == "dim":
        #     mostLikelyRN += "o"
        rns.append(mostLikelyRN)

    df.insert(4, "romannumeral", rns, True)


def addmajmin(df: pd.DataFrame):
    majmin = []
    for i, row in df.iterrows():
        if "dim" in row["shorthand"]:
            majmin.append("dim")
            continue
        val = row["majmin"]
        majmin.append(val.split(":")[1])
    df.insert(4, "romannumeral", majmin, True)


def addEmotionCounts(df: pd.DataFrame, songNumber: int, toDistribution=True):
    newRowInfo = []
    response = getSongAnalyses(str(songNumber))
    for i, row in df.iterrows():
        emotions = {
            "anger": 0,
            "fear": 0,
            "sadness": 0,
            "none": 0,
            "irony": 0,
            "love": 0,
            "joy": 0
        }
        for analysis in response["analyses"]:
            for sample, emotion in analysis["analysis"].items():
                sample = float(sample)
                start = row["start"]
                end = row["end"]
                if start <= sample <= end:
                    emotions[emotion] += 1
        if toDistribution:
            total = sum(emotions.values())
            for key in emotions.keys():
                emotions[key] = round(emotions[key] / total, 2)
        newRowInfo.append(emotions)
    if toDistribution:
        for key in emotions.keys():
            df.insert(5, key, [i[key] for i in newRowInfo], True)
    else:
        for key in emotions.keys():
            df.insert(5, key + "Count", [i[key] for i in newRowInfo], True)

    # print(df.head(30))

def insertRNLags(df: pandas.DataFrame):
    rn_t_1 = df["romannumeral"].iloc[:-1].reset_index(drop=True).values.tolist()
    rn_t_1 = ["START"] + rn_t_1

    rn_t_2 = df["romannumeral"].iloc[:-2].reset_index(drop=True).values.tolist()
    rn_t_2 = ["PAD", "START"] + rn_t_2

    rn_t_3 = df["romannumeral"].iloc[:-3].reset_index(drop=True).values.tolist()
    rn_t_3 = ["PAD", "PAD", "START"] + rn_t_3

    for i, rn in enumerate([rn_t_3, rn_t_2, rn_t_1]):
        df.insert(0, f"t-{3-i}", rn)

def getAllDF(recording: str="HU33", annotationNum: int=1):
    finaldf = pd.DataFrame()

    pairs = getPairedChordLocalKeyPaths(recording, annotationNum)
    for i, pair in tqdm(enumerate(pairs), total=len(pairs)):
        try:
            tempdf = combineChordLocalKey(pair)
            addRomanNumeral(tempdf)
            # addmajmin(tempdf)
            addEmotionCounts(tempdf, i + 1)
            insertRNLags(tempdf)
            finaldf = pd.concat([finaldf, tempdf])
        except ValueError as e:
            print(e)

    return finaldf

def getAllIndividualDF(recording: str="HU33", annotationNum: int=1):
    dfs = {}

    pairs = getPairedChordLocalKeyPaths(recording, annotationNum)
    for i, pair in tqdm(enumerate(pairs), total=len(pairs)):
        try:
            tempdf = combineChordLocalKey(pair)
            addRomanNumeral(tempdf)
            addEmotionCounts(tempdf, i+1)
            insertRNLags(tempdf)
            dfs[i+1] = tempdf
        except ValueError as e:
            print(e)

    return dfs


def harmonyVocabMaps(df: pd.DataFrame, foreground=False):
    if foreground:
        vocab = list(set(df["romannumeral_foreground"].values.tolist()))
    else:
        vocab = list(set(df["romannumeral"].values.tolist()))
    vocabToInt = {v: i for i, v in enumerate(vocab)}
    intToVocab = {i: v for v, i in vocabToInt.items()}

    if not foreground:
        vocabToInt["START"] = -1
        vocabToInt["PAD"] = -2
        intToVocab[-1] = "START"
        intToVocab[-2] = "PAD"
    return vocabToInt, intToVocab

def readPickleAsDF():
    return pandas.read_pickle("./data/allDF.pickle")

def saveAllDFs():
    df = getAllDF()
    with open("./allDF.pickle", "wb") as f:
        pickle.dump(df, f)

def saveAllIndividualDFs():
    dfs = getAllIndividualDF()
    for i, df in dfs.items():
        with open(f"./organized_for_emotions/df_{i}.pickle", "wb") as f:
            pickle.dump(df, f)


def mapToInt(df: pd.DataFrame, vocabToIntMap: dict[str: int], cols: list[str]=None):
    if cols is None:
        cols = ["romannumeral", "t-1", "t-2", "t-3"]
    for col in cols:
        rn = df[col].values.tolist()
        rn = [vocabToIntMap[r] for r in rn]
        df[col] = rn


if __name__ == "__main__":
    """
    notes:
    recording names - HU33 and SC06
    annotator 2 doesn't list local keys for all chords...
    """
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    # df = pd.DataFrame()
    # pairs = getPairedChordLocalKeyPaths("HU33", 1)
    # for i, pair in enumerate(pairs):
    #
    #     try:
    #         tempdf = combineChordLocalKey(pairs[i])
    #         addmajmin(tempdf)
    #         print(tempdf)
    #     except:
    #         continue
    #     df = pd.concat([df, tempdf])
    #     break

    # saveAllDFs()
    saveAllIndividualDFs()

    # print(df[["t-1", "t-2", "t-3", "romannumeral", "joy", "love", "fear", "anger"]].head(20))

