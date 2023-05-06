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


def main():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    extractEmotionTimeSeries(songNumber=2, toDistribution=True)


if __name__ == "__main__":
    main()
