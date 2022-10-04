import torch
import torch.nn as nn
import torch.nn.functional as F


class EmotionNet(nn.Module):
    def __init__(self,
                 numHarmonies=7,
                 hiddenNeurons=4,
                 numHiddenLayers=1,
                 dropoutProb=0.2
                 ):
        super(EmotionNet, self).__init__()
        self.numHarmonies = numHarmonies

        self.fc1 = nn.Linear(7, hiddenNeurons)
        self.hidden = [nn.Linear(hiddenNeurons, hiddenNeurons) for _ in range(numHiddenLayers-1)]
        # self.fc2 = nn.Linear(16, 16)
        self.out = nn.Linear(hiddenNeurons, numHarmonies)

        self.dropout = [nn.Dropout(p=dropoutProb) for _ in range(numHiddenLayers)]

    def forward(self, x):
        x = self.fc1(x)
        if self.training:
            x = self.dropout[0](x)
        x = F.relu(x)
        for i, layer in enumerate(self.hidden):
            x = layer(x)
            if self.training:
                x = self.dropout[i+1](x)
            x = F.relu(x)
        x = self.out(x)
        return x


if __name__ == "__main__":
    en = EmotionNet()
    print(en)






