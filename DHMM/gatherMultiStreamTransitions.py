import pandas
import pandas as pd
import pickle
import os
from data.organize_schubert_data_by_harmony import getAllDF, harmonyVocabMaps
import numpy as np
from pprint import pprint
import matplotlib.pyplot as plt
from scipy.special import softmax
from dirichlet.dirichlet import mle, NotConvergingError
import enlighten
from random import random

from gatherMatrices import ItoE, EtoI, emotions

def _initializeMatrices(df: pd.DataFrame, mainCol: str, otherCols: list[str]):
    # Set counts for each transition matrix to 0
    numUniqueMain = len(df[mainCol].unique())
    mainMatrices = {emotion: np.zeros((numUniqueMain, numUniqueMain)) for emotion in emotions}
    # print(mainMatrices)
    numUniqueOther = {otherCol: len(df[otherCol].unique()) for otherCol in otherCols}
    otherMatrices = {otherCol: {emotion: np.zeros((numUniqueOther[otherCol], numUniqueMain)) for emotion in emotions} for otherCol in otherCols}
    # print(otherMatrices)
    # print(emotions)
    return numUniqueMain, numUniqueOther, mainMatrices, otherMatrices

def getMixtureTransitionMatricesGeneralized(
        df: pandas.DataFrame,
        mainCol: str,
        otherCols: list[str],
        vocabMaps: dict[str:dict],
        threshold: float=0.02,
        plot: bool=False
):
    # Set counts for each transition matrix to 0
    numUniqueMain, numUniqueOther, mainMatrices, otherMatrices = _initializeMatrices(df, mainCol, otherCols)

    # Loop through every row looking for pairs with the same emotion, adding to the corresponding matrix count
    for i, row in df.iterrows():
        if i == 0: continue
        prevRow = df.iloc[i-1, :]
        for emotion in emotions:
            # Check that the emotion appears in the current and previous rows above the given threshold
            if row[emotion] < threshold or prevRow[emotion] < threshold:
                continue
            if mainCol in vocabMaps:
                toIdx = vocabMaps[mainCol]["VtoI"][row[mainCol]]
                fromIdx = vocabMaps[mainCol]["VtoI"][prevRow[mainCol]]
            else:
                toIdx = row[mainCol]
                fromIdx = prevRow[mainCol]
            if fromIdx != "N/A" and toIdx != "N/A":
                mainMatrices[emotion][fromIdx, toIdx] += 1
            for otherCol in otherCols:
                if otherCol in vocabMaps:
                    fromIdx = vocabMaps[otherCol]["VtoI"][prevRow[otherCol]]
                else:
                    fromIdx = prevRow[otherCol]
                if fromIdx != "N/A" and toIdx != "N/A":
                    otherMatrices[otherCol][emotion][fromIdx, toIdx] += 1
    # Turn all rows in every transition matrix into probability distributions
    for key, matrix in mainMatrices.items():
        for i, row in enumerate(matrix):
            if np.sum(row) == 0: continue
            mainMatrices[key][i] = row/np.sum(row)
    for column, dictionary in otherMatrices.items():
        for emotion, matrix in dictionary.items():
            for i, row in enumerate(matrix):
                if np.sum(row) == 0: continue
                otherMatrices[column][emotion][i] = row/np.sum(row)

    # Plot heatmap of each emotion matrix if plot is True
    if plot:
        _plotMatrices(mainMatrices, mainCol, vocabMaps, numUniqueMain, otherCols, otherMatrices, numUniqueOther)

    return mainMatrices, otherMatrices


def _plotMatrices(mainMatrices, mainCol, vocabMaps, numUniqueMain, otherCols, otherMatrices, numUniqueOther):
    for emotion, matrix in mainMatrices.items():
        plt.imshow(matrix, cmap='hot', interpolation='nearest')
        plt.title(f"{emotion} {mainCol}")
        if mainCol in vocabMaps:
            plt.xticks(range(numUniqueMain), [vocabMaps[mainCol]["ItoV"][i] for i in range(numUniqueMain)], rotation=90)
            plt.yticks(range(numUniqueMain), [vocabMaps[mainCol]["ItoV"][i] for i in range(numUniqueMain)])
        else:
            plt.xticks(range(numUniqueMain), [i for i in range(numUniqueMain)], rotation=90)
            plt.yticks(range(numUniqueMain), [i for i in range(numUniqueMain)])
        plt.show()
    for otherCol in otherCols:
        for emotion, matrix in otherMatrices[otherCol].items():
            plt.imshow(matrix, cmap='hot', interpolation='nearest')
            plt.title(f"{emotion} {otherCol}")
            plt.subplots_adjust(bottom=0.15)
            if mainCol in vocabMaps:
                plt.xticks(range(numUniqueMain), [vocabMaps[mainCol]["ItoV"][i] for i in range(numUniqueMain)],
                           rotation=90)
            else:
                plt.xticks(range(numUniqueMain), [i for i in range(numUniqueMain)], rotation=90)
            if otherCol in vocabMaps:
                plt.yticks(range(numUniqueOther[otherCol]),
                           [vocabMaps[otherCol]["ItoV"][i] for i in range(numUniqueOther[otherCol])])
            else:
                plt.yticks(range(numUniqueOther[otherCol]), [i for i in range(numUniqueOther[otherCol])])
            plt.show()


def getMixtureTransitionMatricesForHarmony(df: pandas.DataFrame, threshold: float=0.02, plot: bool=False):
    """
    Produces the mixture transition matrix from the provided df
    :param df: a pandas dataframe holding information from the Winterreise dataset, Roman numerals, and emotions
    :param threshold: what portion of an emotion needs to exist at a given time to count as present
    :param plot: boolean determining whether to visualize heatmaps of transition matrices
    :return: (
        harmonyMatrices: a dict[emotion: np.array] that stores the harmony transition matrix for each emotion
        dynamicsMatrices: a dict[emotion: np.array] that stores the dynamic transition matrix for each emotion
        VtoI: a dict[str:int] that translates Roman numerals to their index in the transition matrix
        ItoV: a dict[int:str] that does the reverse of VtoI
    )
    """
    # Get vocab/int maps for all Roman numerals in df
    VtoI, ItoV = harmonyVocabMaps(df, foreground=True)

    # Set counts for each transition matrix to 0
    numUniqueHarmonies = len(df["romannumeral_foreground"].unique())
    harmonyMatrices = {emotion: np.zeros((numUniqueHarmonies, numUniqueHarmonies)) for emotion in emotions}

    numUniqueDynamics = len(df["dynamic_level"].unique())
    dynamicsMatrices = {emotion: np.zeros((numUniqueDynamics, numUniqueHarmonies)) for emotion in emotions}

    # Loop through every row looking for pairs with the same emotion, adding to the corresponding matrix count
    for i, row in df.iterrows():
        if i == 0: continue
        prevRow = df.iloc[i-1, :]
        for emotion in emotions:
            # Check that the emotion appears in the current and previous rows above the given threshold
            if row[emotion] >= threshold and prevRow[emotion] >= threshold:
                fromRnIdx = VtoI[prevRow["romannumeral_foreground"]]
                toRnIdx = VtoI[row["romannumeral_foreground"]]
                harmonyMatrices[emotion][fromRnIdx, toRnIdx] += 1
                dynamicsMatrices[emotion][prevRow["dynamic_level"], toRnIdx] += 1
    # Turn all rows in every transition matrix into probability distributions
    for key, matrix in harmonyMatrices.items():
        for i, row in enumerate(matrix):
            if np.sum(row) == 0: continue
            harmonyMatrices[key][i] = row/np.sum(row)
    for key, matrix in dynamicsMatrices.items():
        for i, row in enumerate(matrix):
            if np.sum(row) == 0: continue
            dynamicsMatrices[key][i] = row/np.sum(row)

    # Plot heatmap of each emotion matrix if plot is True
    if plot:
        for emotion, matrix in harmonyMatrices.items():
            plt.imshow(matrix, cmap='hot', interpolation='nearest')
            plt.title(f"{emotion} harmonies")
            plt.xticks(range(numUniqueHarmonies), [ItoV[i] for i in range(numUniqueHarmonies)], rotation=90)
            plt.yticks(range(numUniqueHarmonies), [ItoV[i] for i in range(numUniqueHarmonies)])
            plt.show()
        for emotion, matrix in dynamicsMatrices.items():
            plt.imshow(matrix, cmap='hot', interpolation='nearest')
            plt.title(f"{emotion} dynamics")
            plt.subplots_adjust(bottom=0.15)
            plt.xticks(range(numUniqueHarmonies), [ItoV[i] for i in range(numUniqueHarmonies)], rotation=90)
            plt.yticks(range(numUniqueDynamics), [i for i in range(numUniqueDynamics)])
            plt.show()

    return harmonyMatrices, dynamicsMatrices, VtoI, ItoV


def getMixedProbs(mainMatrices, otherMatrices, previous: int, sentimentMixture: np.array, featureMixture: np.array):
    pass

def main():
    pd.set_option('display.max_columns', None)
    pd.set_option('display.max_rows', None)

    allDF = pd.DataFrame()
    for songNumber in range(1, 25):
        try:
            with open(f"../data/with_dynamics_generalized_romans/song_{songNumber}.pickle", "rb") as f:
                df = pickle.load(f)
                allDF = pd.concat([allDF, df], ignore_index=True)
        except FileNotFoundError as e:
            print(e)
    # print(allDF["measure"])

    # getMixtureTransitionMatricesForHarmony(df, plot=True)
    VtoI, ItoV = harmonyVocabMaps(allDF, foreground=True)
    vocabMaps = {"romannumeral_foreground": {"VtoI": VtoI, "ItoV": ItoV}}
    mainMatrices, otherMatrices = getMixtureTransitionMatricesGeneralized(
        allDF,
        # "dynamic_level",
        # ["romannumeral_foreground"],
        "romannumeral_foreground",
        ["dynamic_level"],
        vocabMaps=vocabMaps,
        plot=True
    )
    print(mainMatrices)


if __name__ == "__main__":
    main()