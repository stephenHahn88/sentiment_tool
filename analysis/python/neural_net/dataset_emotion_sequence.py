from torch.nn.functional import one_hot
import torch
from torch.utils.data import Dataset
import json
from numerical_encode_decode import HarmonyEncoderDecoder
from utility import find_vocab

class EmotionRNSequenceDataset(Dataset):
    def __init__(self, emotion_files: list[str], remove_consecutives=True):
        self.emotion_files = emotion_files
        self.labels = []
        self.vocab = list(find_vocab(self.emotion_files))
        self.harmonyTranslator = HarmonyEncoderDecoder(self.vocab)
        for file in emotion_files:
            with open(file, "r") as f:
                data = json.load(f)
                for value in data.values():
                    sequence = [s for s in value["sequence"] if s]
                    if remove_consecutives:
                        sequence = [v for i, v in enumerate(sequence) if i == 0 or v != sequence[i-1]]
                    if len(sequence) <= 1:
                        continue
                    sequence_enc = self.harmonyTranslator.encode(sequence)
                    emotions = torch.tensor(value["emotion_distribution"], dtype=torch.float32)
                    emotions = torch.div(emotions, 100)
                    self.labels.append((emotions, torch.tensor(sequence_enc[:-1]), torch.tensor(sequence_enc[1:])))

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, item):
        emotions = self.labels[item][0]
        sequence_x = self.labels[item][1]
        sequence_y = self.labels[item][2]
        return emotions, sequence_x, sequence_y

    def printHarmonyTranslator(self):
        print(self.harmonyTranslator.decoder)

    def printHarmonyTranslation(self, idx):
        print(self.harmonyTranslator.decode(self[idx][1]))

    def decodePrint(self, indeces: torch.Tensor):
        print(self.harmonyTranslator.decode(indeces))


if __name__ == "__main__":
    ds = EmotionRNSequenceDataset(["../op18_no2_mov1.json"])
    print(ds[1])
    ds.printHarmonyTranslation(1)







