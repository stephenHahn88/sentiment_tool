from pathlib import Path
from pprint import pprint
import pandas as pd
import re

annotationPath = Path(".", "Schubert_Winterreise_Dataset_v2-0", "02_Annotations")

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


def addRomanNumeral(df: pd.DataFrame):
    rns = []
    for i, row in df.iterrows():
        root, quality, bass = parseShortHand(row["shorthand"])
        chromaticSteps = getChromaticSteps(row["localkey"], root)
        mostLikelyRN = getMostLikelyRomanNumeral(chromaticSteps)
        if quality == "dom":
            mostLikelyRN = convertToSecondaryDom(mostLikelyRN)
        elif quality == "min":
            mostLikelyRN = mostLikelyRN.lower()
        elif quality == "dim":
            mostLikelyRN += "o"
        rns.append(mostLikelyRN)
    df.insert(4, "romannumeral", rns, True)
    print(df.head(60))

if __name__ == "__main__":
    """
    notes:
    recording names - HU33 and SC06
    annotator 2 doesn't list local keys for all chords...
    """
    pd.set_option('display.max_columns', None)
    # n1, n2 = ("C", "B")
    # sd = getScaleDegree(n1, n2)
    # print(sd)
    pairs = getPairedChordLocalKeyPaths("HU33", 3)
    tempdf = combineChordLocalKey(pairs[1])
    addRomanNumeral(tempdf)
    # temp = parseShortHand("A:min7")
    # print(temp)
