import pandas as pd


def combine_data(
        measure_file: str,
        annotation_file: str,
        abc_file: str,
        anacrusis_beats: float,
        repeat_measures: list[range]
):
    measure_times = pd.read_csv("../annotations/measure_annotation/" + measure_file, header=None)
    measure_times.columns = ["Time", "Measure"]
    measure_times["Measure"] = range(1, 1 + len(measure_times["Measure"]))
    measure_times = {i: j for i, j in zip(measure_times["Measure"], measure_times["Time"])}
    measure_times[0] = 0

    time_sentiment = pd.read_csv("../annotations/valence_annotation/" + annotation_file, header=None)
    time_sentiment.columns = ["Time", "Category"]
    time_sentiment = time_sentiment.to_dict()
    time_sentiment = {t: c for t, c in zip(time_sentiment["Time"].values(), time_sentiment["Category"].values())}
    
    return 0, 0

if __name__ == "__main__":
    abc, time_valence = combine_data(
        measure_file="op18_no1_mov4_downbeats.csv",
        annotation_file="op18_no1_mov4_clean.csv",
        abc_file="op18_no1_mov4.tsv",
        anacrusis_beats=0,
        repeat_measures=[]
    )


