from multipledispatch import dispatch
import torch

class HarmonyEncoderDecoder:
    def __init__(self, vocabulary: list[str]):
        self.vocabulary = vocabulary
        self.encoder = {harmony: i for i, harmony in enumerate(vocabulary)}
        self.decoder = {i: harmony for harmony, i in self.encoder.items()}

    @dispatch(str)
    def encode(self, harmony: str):
        if harmony not in self.vocabulary:
            raise ValueError(f"Given harmony {harmony} is not in the vocabulary.")
        return self.encoder[harmony]

    @dispatch(list)
    def encode(self, harmonies: list[str]):
        return [self.encode(harmony) for harmony in harmonies]

    @dispatch(int)
    def decode(self, number: int):
        if number not in self.decoder.keys():
            raise ValueError(f"Given key {number} is not in range of this object.")
        return self.decoder[number]

    @dispatch(list)
    def decode(self, numbers: list[int]):
        return [self.decode(number) for number in numbers]

    @dispatch(torch.Tensor)
    def decode(self, tensor: torch.Tensor):
        return [self.decode(number.item()) for number in tensor.flatten()]



if __name__ == "__main__":
    vocab = ["v", "V", "vi", "I", "IV"]
    hed = HarmonyEncoderDecoder(vocab)
    print(hed.encode(["IV", "IV", "v", "vi"]))
    print(hed.decode([0, 0, 2, 4]))
    print(hed.decode(torch.tensor([1, 2, 3])))
