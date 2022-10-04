import requests
import json

def fetch_analyses():
    url = "https://music-sentiment-tool.herokuapp.com/api/analyses"
    response = requests.get(url)
    return response.json()

def get_RN_times(file_name):
    with open(file_name, "r") as f:
        json_data = json.load(f)
    return json_data

def clean_data():
    json_file = fetch_analyses()
    analyses = {}
    for analysis in json_file:
        if analysis["id"] in [1, 2, 5, 9]:
            continue
        entry = {}
        for item in analysis['analysis'].split(",\n"):
            if item == "":
                continue
            split = item.split(" : ")
            entry[split[0]] = split[1]
        if analysis['piece'] in analyses:
            analyses[analysis['piece']].update(entry)
        else:
            analyses[analysis["piece"]] = entry
    return analyses


def get_emotion_percentages(piece, start, end):
    DATA = clean_data()
    emotions = ["anger", "fear", "sadness", "none", "irony", "love", "joy"]
    counts = {k: 0 for k in emotions}
    total = 0
    for key in DATA[piece]:
        k = float(key)
        if k < end and k > start:
            counts[DATA[piece][key]] += 1
            total += 1
    return [round(counts[e]/total * 100, 2) for e in emotions]


def get_phrase_ranges(file_name):
    rn_json = get_RN_times(file_name + ".json")

    curr_start_i = 0
    phrase_end = rn_json["phraseend"]

    ranges = {}
    phrase_num = 0
    for ended_i in phrase_end:
        ended_i = int(ended_i)
        if phrase_end[str(ended_i)] and ended_i+1 < len(rn_json["time"]):
            start = rn_json["time"][str(curr_start_i)]
            end = rn_json["time"][str(ended_i + 1)]

            rns_sequence = [
                rn_json["numeral"][str(i)] if not rn_json["relativeroot"][str(i)]
                else f"{rn_json['numeral'][str(i)]}/{rn_json['relativeroot'][str(i)]}"
                for i in range(curr_start_i, ended_i)
            ]
            rns = set(rns_sequence)

            ranges[phrase_num] = {
                "start": round(start, 2),
                "end": round(end, 2),
                "start_i": curr_start_i,
                "end_i": ended_i,
                "emotion_distribution": get_emotion_percentages(file_name + ".mp3", start, end),
                "harmonies": list(rns),
                "sequence": rns_sequence
            }

            curr_start_i = ended_i + 1
            phrase_num += 1
    return ranges

def write_phrase_ranges(file_names):
    for file_name in file_names:
        data = get_phrase_ranges(file_name)
        with open(f"../{file_name}.json", "w") as f:
            obj = json.dumps(data)
            f.write(obj)

if __name__ == "__main__":
    from pprint import pprint
    # data = clean_data()
    # data = get_emotion_percentages("op18_no2_mov1.mp3", 3, 8)
    # data = get_RN_times("./op18_no2_mov1.json")
    # data = get_phrase_ranges("op18_no1_mov1")
    # with open("../op18_no1_mov1.json", "w") as f:
    #     obj = json.dumps(data)
    #     f.write(obj)
    file_names = [
        # "op18_no1_mov1",
        # "op18_no1_mov2",
        # "op18_no1_mov4",
        # "op18_no2_mov1",
        # "op18_no2_mov4",
        # "op18_no3_mov2",
        # "op18_no4_mov2",
        "op18_no6_mov2"
    ]
    write_phrase_ranges(file_names)


