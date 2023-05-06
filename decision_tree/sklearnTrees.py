import pandas as pd
import numpy as np
import seaborn as sn
import matplotlib.pyplot as plt
import os.path
import pickle
from random import randint
from pprint import pprint

from data.organize_schubert_data_by_harmony import getAllDF, vocabMaps, mapToInt

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

from chefboost import Chefboost as chef

from gosdt import GOSDT

'''
Music Sentiment Classification Task:
    - Given a chord and some set of emotions associated with it, what is the most likely chord that comes next?
'''


# Plot confusion matrix, as returned by a scikit classifier;
# code taken from: https://stackoverflow.com/questions/35572000/how-can-i-plot-a-confusion-matrix
def plot_confusion_matrix(C, title, plot=True, labels=None):
    if labels is None:
        labels = range(len(C))
    df = pd.DataFrame(C, labels, labels)
    plt.figure(figsize=(10, 10))
    ax = plt.axes()
    sn.set(font_scale=2)  # for label size
    sn.heatmap(df, ax=ax, annot=True, annot_kws={"size": 24})  # font size
    ax.set_title(title)
    if plot:
        plt.show()

def fit_chef(X, Y, model, numClassifiers=50):
    Y = Y.to_frame().rename(columns={"romannumeral": "Decision"})
    X = pd.concat([X, Y], axis=1)

    X_train, X_test = train_test_split(X, test_size=0.2, stratify=X["Decision"])
    if model == "CART":
        config = {'algorithm': 'CART'}
    elif model == "adaboost":
        config = {'enableAdaboost': True, 'num_of_weak_classifier': numClassifiers}
    elif model == "randomForest":
        config = {'enableRandomForest': True, 'num_of_trees': numClassifiers}
    elif model == "gradientBoost":
        config = {'enableGBM': True, 'epochs': 10, 'learning_rate': 1, 'max_depth': 5}
    else:
        config = {'algorithm': 'C4.5'}
    model = chef.fit(X_train, config=config)

    evaluation = chef.evaluate(model, X_test, task="test")

    try:
        rules = "./outputs/rules/rules.py"
        fi = chef.feature_importance(rules).set_index("feature")
        fi.plot(kind="barh", title="Feature Importance")
    except Exception as e:
        print(e)


def fit_gosdt(X, Y):
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

    config = {
        "regularization": 0.115,
        "depth_budget": 2,
        "worker_limit": 4,
        "verbose": True,
        "objective": "bacc",
        "tree": "./data"
    }

    model = GOSDT(config)
    model.fit(X_train, Y_train)

    train_acc = model.score(X_train, Y_train)
    test_acc = model.score(X_test, Y_test)

    print(f"Training acc: {train_acc}")
    print(f"Testing acc: {test_acc}")
    print(f"Leaves: {model.leaves()}")
    print(f"Nodes: {model.nodes()}")

    # preds_train = model.predict(X_train)
    # preds_test = model.predict(X_test)

    # Confusion matrix visual
    # C_train = confusion_matrix(Y_train, preds_train)
    # C_test = confusion_matrix(Y_test, preds_test)
    # plot_confusion_matrix(C_train, f"Training data w/ accuracy {train_acc}", plot=False)
    # plot_confusion_matrix(C_test, f"Testing data w/ accuracy {test_acc}", plot=False)


def fit_model(X, Y, model_class):
    # Get training data and split 90/10 (train/test)
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

    # Init tree and fit
    myModel = model_class()
    myModel.fit(X_train, Y_train)

    # Get predictions on training and testing data
    preds_train = myModel.predict(X_train)
    preds_test = myModel.predict(X_test)

    # Get accuracy scores
    train_acc = myModel.score(X_train, Y_train)
    test_acc = myModel.score(X_test, Y_test)

    # Visualize tree (if possible)
    # if model == tree.DecisionTreeClassifier:
    #     tree.plot_tree(myModel)

    # Confusion matrix visual
    C_train = confusion_matrix(Y_train, preds_train)
    C_test = confusion_matrix(Y_test, preds_test)
    plot_confusion_matrix(C_train, f"Training data w/ accuracy {train_acc}")
    plot_confusion_matrix(C_test, f"Testing data w/ accuracy {test_acc}")

    return myModel

def generate(model, intToVocab: dict, vocabToInt: dict, numHarmonies: int=10):
    happyAlpha = [0.1, 0.1, 0.1, 0.1, 0.1, 6.0, 8.0]
    sadAlpha = [1, 2, 8, 0.1, 0.1, 0.1, 0.1]
    angryAlpha = [8, 1, 2, 0.1, 0.1, 0.1, 0.1]
    getDirichlet = lambda x: np.round(np.random.dirichlet([happyAlpha, sadAlpha, angryAlpha][x]), 3)

    emotions = pd.DataFrame()
    choices = []
    for _ in range(numHarmonies):
        choice = randint(0, 2)
        choices.append(choice)
        newEmotions = pd.DataFrame(getDirichlet(choice)).transpose()
        emotions = pd.concat([emotions, newEmotions]).reset_index(drop=True)
    emotions.columns = ["anger", "fear", "sadness", "none", "irony", "love", "joy"]
    print(emotions)

    currRN = ["START", "PAD", "PAD"]
    sequence = []
    for i, row in emotions.iterrows():
        newRow = row.to_frame().transpose().reset_index(drop=True)
        rn_df = pd.DataFrame(np.array([vocabToInt[r] for r in currRN])).transpose()
        rn_df.columns = ["t-1", "t-2", "t-3"]
        temp_df = pd.concat([rn_df, newRow], axis=1).reset_index(drop=True)
        y = model.predict(temp_df)
        sequence.append(y[0])
        currRN.pop(2)
        currRN.insert(0, y[0])
    return sequence, [["H", "S", "A"][choice] for choice in choices]

if __name__ == "__main__":
    pd.set_option('display.max_columns', None)

    if not os.path.isfile("../data/allDF.pickle"):
        df = getAllDF("HU33", 1)
    else:
        with open("../data/allDF.pickle", "rb") as f:
            df = pickle.load(f)
    print(df["romannumeral"].value_counts())

    cols = ["t-1", "t-2", "t-3"]
    df = df[cols + [
        "romannumeral",
        "anger", "fear", "sadness", "none", "irony", "love", "joy"
    ]]
    VtoI, ItoV = vocabMaps(df)
    mapToInt(df, VtoI, cols=cols)
    X = df.loc[:, df.columns != "romannumeral"]
    # print(X.head(5))
    Y = df["romannumeral"]
    # fit_chef(X, Y, "CART", numClassifiers=20)
    model = fit_model(X, Y, GradientBoostingClassifier)
    sequence, emotions = generate(model, ItoV, VtoI)
    # fit_gosdt(X, Y)

    print(sequence)
    print(emotions)
