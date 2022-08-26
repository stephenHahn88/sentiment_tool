import json
from collections import defaultdict
from pprint import pprint

def clean_data():
    with open("data2.json", "r") as f:
        file = json.load(f)
    # print(file)
    analyses = {}
    for row in file:
        # print(row['piece'])
        split = [x.split(' : ') for x in row['analysis'].split(",\n") if x]
        split = {round(float(time), 3): emotion for time, emotion in split}
        # print(split)
        if row['piece'] in analyses.keys():
            analyses[row['piece']].update(split)
        else:
            analyses[row['piece']] = split

    with open("data_temp.js", "w") as f:
        json.dump(analyses, f)


if __name__ == "__main__":
    clean_data()