import pandas
import pandas as pd
import pickle
import os
from data.organize_schubert_data import getAllDF, vocabMaps
import numpy as np
from pprint import pprint
import matplotlib.pyplot as plt
from scipy.special import softmax
from dirichlet.dirichlet import mle, NotConvergingError
import enlighten
from random import random

emotions = ["anger", "fear", "sadness", "none", "irony", "love", "joy"]
EtoI = {emotion: i for i, emotion in enumerate(emotions)}
ItoE = {i: emotion for i, emotion in enumerate(emotions)}


def softmax(x):
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0)

def getMixtureTransitionMatrices(df: pandas.DataFrame, threshold: float=0.02, plot: bool=False):
    """
    Produces the mixture transition matrix from the provided df
    :param df: a pandas dataframe holding information from the Winterreise dataset, Roman numerals, and emotions
    :param threshold: what portion of an emotion needs to exist at a given time to count as present
    :param plot: boolean determining whether to visualize heatmaps of transition matrices
    :return: (
        matrices: a dict[emotion: np.array] that stores the transition matrix for each emotion
        VtoI: a dict[str:int] that translates Roman numerals to their index in the transition matrix
        ItoV: a dict[int:str] that does the reverse of VtoI
    )
    """
    # Get vocab/int maps for all Roman numerals in df
    VtoI, ItoV = vocabMaps(df)

    # Set counts for each transition matrix to 0
    numUnique = len(df["romannumeral"].unique()) + 2
    matrices = {emotion: np.zeros((numUnique, numUnique)) for emotion in emotions}

    # Loop through every row looking for pairs with the same emotion, adding to the corresponding matrix count
    for i, row in df.iterrows():
        if i == 0: continue
        prevRow = df.iloc[i-1, :]
        for emotion in emotions:
            # Check that the emotion appears in the current and previous rows above the given threshold
            if row[emotion] >= threshold and prevRow[emotion] >= threshold:
                fromRnIdx = VtoI[prevRow["romannumeral"]]
                toRnIdx = VtoI[row["romannumeral"]]
                matrices[emotion][fromRnIdx, toRnIdx] += 1
    # Turn all rows in every transition matrix into probability distributions
    for key, matrix in matrices.items():
        for i, row in enumerate(matrix):
            if np.sum(row) == 0: continue
            matrices[key][i] = row/np.sum(row)

    # Plot heatmap of each emotion matrix if plot is True
    if plot:
        for emotion, matrix in matrices.items():
            plt.imshow(matrix, cmap='hot', interpolation='nearest')
            plt.title(emotion)
            plt.xticks(range(numUnique), [ItoV[i] for i in range(numUnique)], rotation=45)
            plt.yticks(range(numUnique), [ItoV[i] for i in range(numUnique)])
            plt.show()

    return matrices, VtoI, ItoV


def getMixtureEmissionMatrices(df: pd.DataFrame, threshold: float=0.02):
    VtoI, ItoV = vocabMaps(df)
    numUnique = len(df["romannumeral"].unique())
    matrix = np.zeros((len(emotions), numUnique))

    for i, row in df.iterrows():
        for emotion in emotions:
            if row[emotion] >= threshold:
                emotionIdx = EtoI[emotion]
                rnIdx = VtoI[row["romannumeral"]]
                matrix[emotionIdx, rnIdx] += 1
    for i, row in enumerate(matrix):
        if np.sum(row) == 0: continue
        matrix[i] = row / np.sum(row)
    pprint(matrix)

    plt.imshow(matrix, cmap='hot', interpolation='nearest')
    plt.xticks(range(numUnique), [ItoV[i] for i in range(numUnique)], rotation=45)
    plt.yticks(range(len(emotions)), [ItoE[i] for i in range(len(emotions))])
    plt.show()


def getEmotionTransitionMatrix(df: pd.DataFrame, threshold: float=0.02):
    matrix = np.zeros((len(emotions), len(emotions)))

    for i, currRow in df.iterrows():
        if i == 0: continue
        prevRow = df.iloc[i-1, :]
        for currEmotion in emotions:
            for prevEmotion in emotions:
                if currRow[currEmotion] >= threshold and prevRow[prevEmotion] >= threshold:
                    prevIdx = EtoI[prevEmotion]
                    currIdx = EtoI[currEmotion]
                    matrix[prevIdx, currIdx] += 1
    for i, row in enumerate(matrix):
        if np.sum(row) == 0: continue
        matrix[i] = row / np.sum(row)

    pprint(matrix)
    plt.imshow(matrix, cmap='hot', interpolation='nearest')
    plt.xticks(range(len(emotions)), [ItoE[i] for i in range(len(emotions))], rotation=45)
    plt.yticks(range(len(emotions)), [ItoE[i] for i in range(len(emotions))])
    plt.show()

    return matrix


def getTransitionProbabilities(
        transitionMatrices: dict[str:np.array],
        fromEmotionDistribution: dict[str:float],
        prevRN: str,
        vocabToInt: dict[str:int],
        intToVocab: dict[int:str]
):
    """
    Find the transition probabilities based on a mixture of transition matrices and
    a particular emotion distribution and previous RomanNumeral
    :param transitionMatrices: dict[emotion:transition matrix] from getMixtureTransitionMatrices
    :param fromEmotionDistribution: dict[emotion:proportion] where all proportions add up to 1
    :param prevRN: the Roman numeral at the previous time step
    :param vocabToInt:
    :param intToVocab:
    :return: an np.array of probabilities for the next harmony given the above parameters
    """
    prevRNInt = vocabToInt[prevRN]
    answer = np.zeros(len(vocabToInt))
    for emotion, matrix in transitionMatrices.items():
        weightedProbs = fromEmotionDistribution[emotion] * matrix[prevRNInt]
        answer += weightedProbs
    answer /= sum(answer)
    return answer


def emotionConvolutionMLE(df: pd.DataFrame, name: str, windowSize: int=16, manager=None):
    alphas = []
    emotionsOnly: pd.DataFrame = df.loc[:, emotions].reset_index(drop=True)
    rand = pd.DataFrame([[random()/20 for _ in range(len(emotionsOnly.columns))] for _ in range(len(emotionsOnly))])
    rand.columns = emotionsOnly.columns
    emotionsOnly = emotionsOnly.add(rand, fill_value=0)
    emotionsOnly = emotionsOnly.apply(lambda x: x / sum(x), axis=1)

    if manager:
        pbar = manager.counter(total=len(emotionsOnly), desc='Emotion Convolutions', unit='row', leave=False)

    for i, row in emotionsOnly.iterrows():
        try:
            left = min(windowSize // 2, i)
            right = min(windowSize - (windowSize // 2), len(emotionsOnly)-i-1)
            tempdf: pd.DataFrame = emotionsOnly.iloc[i-left:i+right]

            extra = windowSize - len(tempdf)
            if extra > 0:
                mean = tempdf.mean(axis=0).to_frame().transpose()
                extradf = [mean]*extra
                tempdf = pd.concat([tempdf]+extradf, ignore_index=True)

            estimate = mle(tempdf, maxiter=30000)#, method='fixedpoint')
            alphas.append([i] + list(estimate))
        except NotConvergingError as e:
            # print(e)
            continue
        if manager:
            pbar.update()

    alphaDF = pd.DataFrame(alphas)
    alphaDF.columns = ["index"] + emotions
    pd.set_option('display.max_rows', None)
    basePath = f"./alphas/windowSize_{windowSize}"
    if not os.path.exists(basePath):
        os.makedirs(basePath)
    with open(basePath + f"/{name}_alphas.pickle", "wb") as f:
        pickle.dump(alphaDF, f)


def main():
    with enlighten.get_manager() as manager:
        pbar = manager.counter(total=24, desc="Songs", unit="songs", leave=False)

        for i in range(1, 25):
            try:
                with open(f"../data/organized_for_emotions/df_{i}.pickle", "rb") as f:
                    df = pickle.load(f)
                    for ws in [8, 16]:
                        emotionConvolutionMLE(df, str(i), windowSize=ws, manager=manager)
            except Exception as e:
                # print(e)
                continue
            pbar.update()


if __name__ == "__main__":
    main()

