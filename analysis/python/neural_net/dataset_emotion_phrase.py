import os
import pandas as pd
from torch.utils.data import Dataset
import json
from numerical_encode_decode import HarmonyEncoderDecoder
from torch.nn.functional import one_hot
import torch
from utility import find_vocab


class EmotionPhraseDataset(Dataset):
    def __init__(self, emotion_files: list[str]):
        self.emotion_files = emotion_files
        self.emotion_labels = []
        self.vocab = list(find_vocab(self.emotion_files))
        self.harmonyTranslator = HarmonyEncoderDecoder(self.vocab)
        for file in emotion_files:
            with open(file, "r") as f:
                data = json.load(f)
                for value in data.values():
                    harmonies = [h for h in value["harmonies"] if h]
                    harmonies_enc = self.harmonyTranslator.encode(harmonies)
                    multihot = torch.sum(one_hot(torch.tensor(harmonies_enc), num_classes=len(self.vocab)), dim=0)
                    emotions = torch.tensor(value["emotion_distribution"], dtype=torch.float32)
                    emotions = torch.div(emotions, 100)
                    # print(emotions)
                    self.emotion_labels.append(
                        (
                            emotions,
                            torch.tensor(multihot, dtype=torch.float32)
                        )
                    )

    def __len__(self):
        return len(self.emotion_labels)

    def __getitem__(self, idx):
        emotions = self.emotion_labels[idx][0]
        harmonies = self.emotion_labels[idx][1]
        return emotions, harmonies

    def printHarmonyTranslator(self):
        print(self.harmonyTranslator.decoder)

    def printHarmonyTranslation(self, idx):
        print(self.harmonyTranslator.decode(self[idx][1]))


if __name__ == "__main__":
    epd = EmotionPhraseDataset(["../op18_no2_mov1.json"])
    print(epd[1])
    epd.printHarmonyTranslator()
    epd.printHarmonyTranslation(2)