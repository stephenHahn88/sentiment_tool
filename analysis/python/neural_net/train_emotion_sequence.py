import torch
import torch.nn as nn
from torch.utils.data import DataLoader, random_split
import torch.nn.functional as F
import matplotlib.pyplot as plt
import random

import logging
import logging.handlers
import os
from tqdm import tqdm

logging.basicConfig(
    filename="./log/EmotionNNParameters.log",
    level=logging.INFO,
    format='%(asctime)s %(name)s %(levelname)s:%(message)s'
)
logger = logging.getLogger(__name__)

import os

os.environ['KMP_DUPLICATE_LIB_OK'] = "True"

from model_emotion_sequence import EmotionTransformer
from dataset_emotion_sequence import EmotionRNSequenceDataset

config = dict(
    id=0,
    token_dimension=4,
    d_model=16,
    heads=2,
    dim_feedforward=16,
    hidden_layers=2,
    dropout_prob=0.3,
    learning_rate=0.001,
    epochs=800,
    print_every=10,
    burn_in=2,
    batch_size=1,
    graph_num=0,
    train_proportion=0.80,
    include_threshold=0.5,
    dataset=EmotionRNSequenceDataset([
        "../op18_no2_mov1.json",
        "../op18_no1_mov1.json",
        "../op18_no1_mov2.json",
        "../op18_no1_mov4.json",
        "../op18_no2_mov4.json",
        "../op18_no3_mov2.json",
        "../op18_no4_mov2.json"
    ], remove_consecutives=True
    )
)


def setParameters():
    seed = random.randint(0, 9999)
    torch.manual_seed(seed)

    print(config)

    dataset = config["dataset"]
    train_size = int(config["train_proportion"] * len(dataset))
    validation_size = len(dataset) - train_size
    train_dataset, validation_dataset = random_split(dataset, [train_size, validation_size])

    batch_size = config["batch_size"]
    train_loader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    validation_loader = DataLoader(validation_dataset, batch_size=batch_size, shuffle=False)

    model = EmotionTransformer(
        numHarmonies=len(dataset.vocab),
        token_dimension=config["token_dimension"],
        d_model=config["d_model"],
        heads=config["heads"],
        dim_feedforward=config["dim_feedforward"],
        hidden_layers=config["hidden_layers"],
        dropout=config["dropout_prob"],
        emotion_dim=7
    )
    learning_rate = config["learning_rate"]

    criterion = nn.BCELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

    EPOCHS = config["epochs"]

    return train_loader, validation_loader, model, learning_rate, criterion, optimizer, EPOCHS, seed


def train():
    train_loader, validation_loader, model, learning_rate, criterion, optimizer, EPOCHS, seed = setParameters()

    train_losses = []
    validation_losses = []
    validation_accs = []
    for epoch in tqdm(range(EPOCHS)):
        train_loss = train_epoch(epoch, model, train_loader, optimizer, criterion)
        train_losses.append(train_loss) if epoch > config["burn_in"] else 0

        validation_loss, val_acc = validation_epoch(epoch, model, validation_loader, criterion)
        validation_losses.append(validation_loss) if epoch > config["burn_in"] else 0
        validation_accs.append(val_acc) if epoch > config["burn_in"] else 0

    if not os.path.exists(f"./log/id{config['id']}/"):
        os.makedirs(f"./log/id{config['id']}/")
    graph(train_losses, validation_losses, validation_accs,
          save_path=f"./log/id{config['id']}/model{config['id']}_{config['graph_num']}.png")
    min_train = min(train_losses)
    min_validation = min(validation_losses)
    logger.info("Seed %s:  \tMinimum train loss: %.4f at epoch %s."
                "\tMinimum validation loss %.4f at epoch %s."
                "\tAverage validation acc %.4f" % (
                    seed,
                    min_train, train_losses.index(min_train),
                    min_validation, validation_losses.index(min_validation),
                    sum(validation_accs) / len(validation_accs)
                ))
    print("Done!")


def train_epoch(epoch, model, train_loader, optimizer, criterion):
    model.train(True)
    running_loss = 0.0
    for i, data in enumerate(train_loader, 0):
        emotion_dist, harmony_x, harmony_y = data
        x_dict = {
            "x": harmony_x,
            "emotion_dist": emotion_dist
        }

        optimizer.zero_grad()

        outputs = model(x_dict)
        outputs = torch.flatten(outputs, 0, 1)
        loss = F.nll_loss(outputs, harmony_y.flatten())
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
    avg_loss = running_loss / len(train_loader)
    if epoch % config["print_every"] == 0:
        print(f"epoch {epoch}, loss: {avg_loss}")
    return avg_loss


def validation_epoch(epoch, model, validation_loader, criterion):
    model.train(False)
    rand_choice = random.randint(0, 30)

    running_loss = 0.0
    num_correct = 0
    num_total = 0
    for i, data in enumerate(validation_loader, 0):
        emotion_dist, harmony_x, harmony_y = data
        x_dict = {
            "x": harmony_x,
            "emotion_dist": emotion_dist
        }
        outputs = model(x_dict)
        outputs = torch.flatten(outputs, 0, 1)
        loss = F.nll_loss(outputs, harmony_y.flatten())
        running_loss += loss.item()

        output_guesses = torch.argmax(outputs, dim=1)
        num_correct += torch.sum(output_guesses == harmony_y).item()
        num_total += len(harmony_y.flatten())
        if i == rand_choice:
            print(config["dataset"].decodePrint(output_guesses), config["dataset"].decodePrint(harmony_y))
            print(emotion_dist)


    avg_loss = running_loss / len(validation_loader)
    accuracy = num_correct / num_total
    if epoch % config["print_every"] == 0:
        print(f"\n\t validation loss: {avg_loss}")
        print(f"\t validation acc:  {accuracy}")
    return avg_loss, accuracy


def graph(train_loss, validation_loss, validation_acc, show=False, save_path=None):
    plt.clf()
    fig, axs = plt.subplots(2)
    axs[0].plot(train_loss, label="train loss")
    axs[0].plot(validation_loss, label="val loss")
    axs[1].plot(validation_acc, label="val acc")
    for ax in axs:
        ax.legend()
        ax.grid(visible=True, which='both')
    plt.show() if show else 0
    plt.savefig(save_path) if save_path else 0
    config['graph_num'] += 1


def resetConfig(**kwargs):
    for key, value in kwargs.items():
        config[key] = value
    config["id"] += 1
    config["graph_num"] = 0
    logger.info("Parameters: %s", config)


def _train(n: int, key: str, vals: list):
    for val in vals:
        resetConfig(**{key: val})
        for _ in range(n):
            train()


if __name__ == "__main__":
    train()
    # _train(2, "dropout_prob", [0.1, 0.2, 0.3, 0.4])
