import math

import torch
import torch.nn as nn
import torch.nn.functional as F
from torch.nn import TransformerEncoder, TransformerEncoderLayer


class PositionalEncoding(nn.Module):
    def __init__(self, token_dimension, dropout=0.1, max_len=5000):
        super().__init__()
        self.dropout = nn.Dropout(p=dropout)
        position = torch.arange(max_len).unsqueeze(1)
        div_term = torch.exp(torch.arange(0, token_dimension, 2) * (-math.log(10_000.0) / token_dimension))
        pe = torch.zeros(max_len, 1, token_dimension)
        pe[:, 0, 0::2] = torch.sin(position * div_term)
        pe[:, 0, 1::2] = torch.cos(position * div_term)
        self.register_buffer('pe', pe)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        x += self.pe[:x.size(0)]
        return self.dropout(x)


# class EmotionalEncoder(nn.Module):
#     def __init__(self, token_dimension, emotion_dimension):
#         super().__init__()
#         ee = torch.zeros(emotion_dimension, 1, token_dimension)
#         self.register_buffer('ee', ee)
#
#     def forward(self, x: torch.Tensor, emotion_distribution) -> torch.Tensor:
#         self.ee


class EmotionTransformer(nn.Module):
    def __init__(self,
                 numHarmonies: int = 8,
                 token_dimension: int = 4,
                 d_model: int = 128,
                 heads: int = 4,
                 dim_feedforward: int = 128,
                 hidden_layers: int = 4,
                 dropout: float = 0.3,
                 emotion_dim: int = 7
                 ):
        super(EmotionTransformer, self).__init__()

        self.emotion_dim = emotion_dim
        self.numHarmonies = numHarmonies

        self.embedding = nn.Embedding(numHarmonies, token_dimension)
        self.token_dimension = token_dimension
        self.positional_encoder = PositionalEncoding(token_dimension, dropout)
        self.projection = nn.Linear(token_dimension + emotion_dim, d_model)
        # self.projection = nn.Linear(token_dimension, d_model)

        encoder_layer = TransformerEncoderLayer(
            batch_first=True,
            d_model=d_model,
            nhead=heads,
            dim_feedforward=dim_feedforward,
            dropout=dropout
        )
        self.transformer_encoder = TransformerEncoder(encoder_layer, hidden_layers)

        self.dropout = nn.Dropout(p=dropout)

        self.fc1 = nn.Linear(d_model, numHarmonies)

    def _generate_mask(self, sz):
        return torch.triu(torch.ones(sz, sz) * float('-inf'), diagonal=1)

    def forward(self, x_dict: dict[str:torch.Tensor]) -> torch.Tensor:
        x = x_dict["x"]
        emotion_dist = x_dict["emotion_dist"]

        embed = self.embedding(x)
        embed = self.positional_encoder(embed)

        emotion_encoding = torch.zeros(x.size()[0], x.size()[1], self.emotion_dim)
        emotion_encoding[:, :, :] = emotion_dist.unsqueeze(dim=1)
        embed = torch.cat((embed, emotion_encoding), dim=2)

        projected = F.relu(self.projection(embed))

        mask = self._generate_mask(x.size()[1])
        out = self.transformer_encoder(projected, mask)
        out = self.dropout(out)
        out = self.fc1(out)
        return F.log_softmax(out, dim=2)


if __name__ == "__main__":
    et = EmotionTransformer()
    xdict = {
        "x": torch.tensor([[1, 3, 2],
                           [2, 3, 2]]),
        "emotion_dist": torch.tensor([[0.4, 0.2, 0.2, 0.2, 0, 0, 0],
                                      [0.2, 0.1, 0.5, 0.0, 0, 0.2, 0]])
    }
    out = et(xdict)
    print(out)
    print(out.shape)
