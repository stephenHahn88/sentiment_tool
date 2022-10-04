import json


def find_vocab(emotion_files):
    vocab = set()
    for file in emotion_files:
        with open(file, "r") as f:
            data = json.load(f)
            for value in data.values():
                vocab.update([h for h in value["harmonies"] if h])
    return vocab



