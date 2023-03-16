import pickle

import matplotlib.pyplot as plt
from server import getSongAnalyses
from data.organize_schubert_data import addEmotionCounts
import pandas as pd
from tqdm import tqdm
import numpy as np
from sklearn.manifold import TSNE
import seaborn as sns
import seaborn.objects as so
from sklearn.cluster import AgglomerativeClustering
from scipy.cluster.hierarchy import dendrogram, linkage
import os

emotions = ["joy", "love", "irony", "none", "sadness", "fear", "anger"]


def retrieveAvailableDfs():
    dfs = {}
    for i in range(1, 25):
        try:
            with open(f"../data/organized_for_emotions/df_{i}.pickle", "rb") as f:
                dfs[i] = pickle.load(f)
        except FileNotFoundError as e:
            continue

    return dfs


def getTotalProportion(df: pd.DataFrame):
    cols = [e + "Count" for e in emotions]
    counts: pd.Series = df[cols].sum()
    total = counts.sum()
    percents = (counts/total) * 100
    return percents


def proportionsToArray(proportions: dict[int:pd.Series]):
    X = np.zeros((len(proportions), 7))
    y = np.zeros(len(proportions))
    for i, (song, props) in enumerate(proportions.items()):
        X[i] = props.to_numpy()
        y[i] = song
    return X, y


def run_tsne(X: np.array, y: np.array, perplexity=1.0, plot=True):
    tsne = TSNE(2, perplexity=perplexity)
    tsne_result = tsne.fit_transform(X)
    df = pd.DataFrame({'tsne_1': tsne_result[:, 0], 'tsne_2': tsne_result[:, 1], 'text': y})

    if plot:
        fig, ax = plt.subplots(1)
        lim = (tsne_result.min() - 50, tsne_result.max() + 50)
        ax.set_xlim(lim)
        ax.set_ylim(lim)
        ax.set_aspect('equal')
        p = so.Plot(x='tsne_1', y='tsne_2', data=df, text='text')\
            .add(so.Dot(marker='.'))\
            .add(so.Text(halign='left'))
        p.on(ax).show()

    return df


def agglomerativeClustering(df: pd.DataFrame):
    data = df[["tsne_1", "tsne_2"]].to_numpy()
    hier_cluster = AgglomerativeClustering(
        n_clusters=4,
        affinity='euclidean',
        linkage='ward'
    )
    labels = hier_cluster.fit_predict(data)

    plt.scatter(x=[i for i, j in data], y=[j for i, j in data], c=labels)
    plt.show()


def main():
    pd.set_option('display.max_columns', None)

    path = "./totalProportions.pickle"
    if not os.path.exists(path):
        proportions = {}
        dfs = retrieveAvailableDfs()
        for i, df in tqdm(dfs.items()):
            addEmotionCounts(df, i, False)
            proportions[i] = getTotalProportion(df)
        with open(path, "wb") as f:
            pickle.dump(proportions, f)
    else:
        with open(path, "rb") as f:
            proportions = pickle.load(f)
    X, y = proportionsToArray(proportions)
    df = run_tsne(X, y, perplexity=1.2)
    agglomerativeClustering(df)


if __name__ == "__main__":
    main()