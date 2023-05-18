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


def getMixtureTransitionMatrices(df: pandas.DataFrame, threshold: float=0.02, plot: bool=False):
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
    dynamicsMatrices = {emotion: np.zeros((numUniqueDynamics, numUniqueDynamics)) for emotion in emotions}

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
                dynamicsMatrices[emotion][prevRow["dynamic_level"], row["dynamic_level"]] += 1
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
            plt.xticks(range(numUniqueDynamics), [i for i in range(numUniqueDynamics)], rotation=90)
            plt.yticks(range(numUniqueDynamics), [i for i in range(numUniqueDynamics)])
            plt.show()

    return harmonyMatrices, dynamicsMatrices, VtoI, ItoV


def main():
    pd.set_option('display.max_columns', None)
    # pd.set_option('display.max_rows', None)

    songNumber = 2
    with open(f"../data/with_dynamics_generalized_romans/song_{songNumber}.pickle", "rb") as f:
        df = pickle.load(f)
    print(df)
    getMixtureTransitionMatrices(df, plot=True)


if __name__ == "__main__":
    main()