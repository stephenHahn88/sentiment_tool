import pandas as pd
from copy import deepcopy
from analysis.python.data_cleaning.unused.combine_abc_score import printPanda


def combine_data(
        measure_file: str,
        # annotation_file: str,
        abc_file: str,
        anacrusis_beats: float,
        repeat_measures: list[range]):
    measure_times = pd.read_csv("../../annotations/measure_annotation/" + measure_file, header=None)
    measure_times.columns = ["Time", "Measure"]
    measure_times["Measure"] = range(1, 1 + len(measure_times["Measure"]))
    measure_times = {i: j for i, j in zip(measure_times["Measure"], measure_times["Time"])}
    measure_times[0] = 0

    # time_sentiment = pd.read_csv("../annotations/valence_annotation/" + annotation_file, header=None)
    # time_sentiment.columns = ["Time", "Category"]
    # time_sentiment = time_sentiment.to_dict()
    # time_sentiment = {t: c for t, c in zip(time_sentiment["Time"].values(), time_sentiment["Category"].values())}

    # DATA CLEANING
    abc = pd.read_csv("../../annotations/abc_dataset/tsv/" + abc_file, sep="\t")
    # Change all measure numbers to account for anacrusis as m. 0 instead of m. 1
    if anacrusis_beats > 0:
        abc["measure"] = [i - 1 for i in abc["measure"]]
        abc["totbeat"] = [i - anacrusis_beats for i in abc["totbeat"]]
    # Remove chords of length 0
    abc = abc[abc["length"] != 0]
    abc = abc.reset_index(drop=True)

    # add repeats TODO: more tests
    for repeat_range in repeat_measures:
        new_part = deepcopy(abc.loc[abc["measure"].isin(repeat_range)])
        new_part["measure"] = [i + len(repeat_range) for i in new_part["measure"]]

        after_part = deepcopy(abc.loc[abc["measure"] > repeat_range[-1]])
        after_part["measure"] = [i + len(repeat_range) for i in after_part["measure"]]

        last_index = new_part.index[-1]
        abc["measure"] = pd.concat([abc["measure"][:last_index + 1]])
        abc = pd.concat([abc.iloc[:last_index + 1], new_part, after_part]).reset_index(drop=True)

    # Add placeholder for times
    abc["time"] = [0.0 for _ in range(abc.shape[0])]

    # Apply downbeat times using measure_times
    beats_per_measure = float(abc["timesig"][0].split("/")[0])
    for i, row in abc.iterrows():
        # Ignore anacrusis
        if row["measure"] == 0:
            continue
        # Downbeats are simply sampled from measure_times
        if row["beat"] == 1:
            abc.at[i, "time"] = measure_times[row["measure"] - 1]
        # Other harmony changes are determined based on the proportion of the measure in which they occur
        else:
            downbeat_delta = measure_times[row["measure"]] - measure_times[row["measure"] - 1]
            proportion = (row["beat"] - 1) / beats_per_measure
            abc.at[i, "time"] = measure_times[row["measure"] - 1] + proportion * downbeat_delta

    # print(abc)

    return abc#, time_sentiment


def apply_avg_valence(df: pd.DataFrame, valence_dict: dict):
    df = df.reset_index(drop=True)
    # print(df)
    df["sentiment"] = ["" for _ in range(df.shape[0])]
    for i, t in enumerate(df["time"]):
        if i >= df.shape[0] - 1:
            valences = [valence for time, valence in valence_dict.items() if time >= t]
        else:
            next_time = df["time"].iloc[i + 1]
            valences = [valence for time, valence in valence_dict.items() if t <= time < next_time]

        if valences:
            df.at[i, "avg_valence"] = sum(valences) / len(valences)
        else:
            df.at[i, "avg_valence"] = df.at[i - 1, "avg_valence"]

    df.to_csv("../annotations/combined/test.csv")
    # print(df)
    # pprint(valence_dict)


if __name__ == "__main__":
    movement = "op18_no6_mov2"
    abc = combine_data(
        measure_file=f"{movement}_downbeats.csv",
        # annotation_file="op18_no2_mov1_clean.csv",
        abc_file=f"{movement}.tsv",
        anacrusis_beats=0,
        repeat_measures=[
            # range(1, 82)
        ]
    )
    printPanda(abc)
    abc.to_json(f"./{movement}.json")
    # apply_avg_valence(abc, time_valence)
