import torch
import torch.nn as nn
from torch.utils.data import DataLoader, random_split
import matplotlib.pyplot as plt
import random

from model_emotion_phrase import EmotionNet
from dataset_emotion_phrase import EmotionPhraseDataset

import logging
import logging.handlers
import os

logging.basicConfig(
    filename="./log/EmotionNNParameters.log",
    level=logging.INFO,
    format='%(asctime)s %(name)s %(levelname)s:%(message)s'
)
logger = logging.getLogger(__name__)

os.environ['KMP_DUPLICATE_LIB_OK'] = "True"

config = dict(
    id=0,
    hidden_neurons=64,
    hidden_layers=2,
    dropout_prob=0.3,
    learning_rate=0.001,
    epochs=800,
    burn_in=0,
    batch_size=1,
    graph_num=0,
    train_proportion=0.6,
    include_threshold=0.5,
    dataset=EmotionPhraseDataset([
        "../op18_no2_mov1.json",
        "../op18_no1_mov1.json",
        "../op18_no1_mov2.json",
        "../op18_no1_mov4.json",
        "../op18_no2_mov4.json",
        "../op18_no3_mov2.json",
        "../op18_no4_mov2.json"
    ])
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

    model = EmotionNet(
        hiddenNeurons=config["hidden_neurons"],
        numHiddenLayers=config["hidden_layers"],
        numHarmonies=len(dataset.vocab),
        dropoutProb=config["dropout_prob"]
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
    for epoch in range(EPOCHS):
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
                "\tAverage accuracy %.4f" % (
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
        inputs, labels = data

        optimizer.zero_grad()

        outputs = model(inputs)
        outputs = torch.sigmoid(outputs)
        # print(outputs)
        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
    avg_loss = running_loss / len(train_loader)
    if epoch % 100 == 0:
        print(f"epoch {epoch}, train loss: {avg_loss}")
    return avg_loss


def validation_epoch(epoch, model, validation_loader, criterion):
    model.train(False)

    running_loss = 0.0
    num_correct = 0
    num_total = 0
    for i, data in enumerate(validation_loader, 0):
        inputs, labels = data
        outputs = model(inputs)
        outputs = torch.sigmoid(outputs)
        running_loss += criterion(outputs, labels).item()

        output_thresholded = torch.round(torch.clamp(outputs + (0.5 - config["include_threshold"]), 0, 1))
        num_correct += torch.sum(output_thresholded == labels).item()
        num_total += len(config["dataset"].vocab) * config["batch_size"]

    avg_loss = running_loss / len(validation_loader)
    accuracy = num_correct / num_total
    if epoch % 100 == 0:
        print(f"\t validation loss: {avg_loss}")
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
    # train()
    _train(2, "hidden_layers", [2, 3, 4])
