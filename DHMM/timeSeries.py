import arviz as az
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle
import pymc as pm
import os



emotions = ["anger", "fear", "sadness", "none", "irony", "love", "joy"]


def loadAlphas(windowSize: int=8, songNum: int=2):
    path = f"./alphas/windowSize_{windowSize}/{songNum}_alphas.pickle"
    with open(path, 'rb') as f:
        return pickle.load(f)


def plotSeries(series: pd.Series):
    _, ax = plt.subplots(figsize=(8, 1.8))
    ax.plot(series.to_numpy())
    ax.set_xlabel("t")
    ax.set_ylabel("alpha")
    ax.set_title(f"Time Series for {series.name}")
    plt.show()


def BVAR(df: pd.DataFrame):
    train_data = df[emotions][:-10]
    test_data = df[emotions][-10:]

    lags = 1
    coords = {
        "lags": reversed(range(-lags, 0)),
        "vars": tuple(emotions),
        "cross_vars": tuple(emotions),
        "time": range(len(train_data) - lags)
    }

    with pm.Model(coords=coords) as BVAR_model:
        intercept = pm.Normal("intercept", mu=0, sigma=1, dims=("vars",))
        lag_coefs = pm.Normal("lag_coefs", mu=0, sigma=1, dims=("lags", "vars", "cross_vars"))
        noise = pm.HalfNormal("noise", dims=("vars",))

        ar_anger = pm.math.sum([
            pm.math.sum(lag_coefs[i, 0] * train_data.values[lags-(i+1): -(i+1)], axis=-1)
            for i in range(lags)
        ])
        ar_fear = pm.math.sum([
            pm.math.sum(lag_coefs[i, 1] * train_data.values[lags - (i + 1): -(i + 1)], axis=-1)
            for i in range(lags)
        ])
        ar_sadness = pm.math.sum([
            pm.math.sum(lag_coefs[i, 2] * train_data.values[lags - (i + 1): -(i + 1)], axis=-1)
            for i in range(lags)
        ])
        ar_none = pm.math.sum([
            pm.math.sum(lag_coefs[i, 3] * train_data.values[lags - (i + 1): -(i + 1)], axis=-1)
            for i in range(lags)
        ])
        ar_irony = pm.math.sum([
            pm.math.sum(lag_coefs[i, 4] * train_data.values[lags - (i + 1): -(i + 1)], axis=-1)
            for i in range(lags)
        ])
        ar_love = pm.math.sum([
            pm.math.sum(lag_coefs[i, 5] * train_data.values[lags - (i + 1): -(i + 1)], axis=-1)
            for i in range(lags)
        ])
        ar_joy = pm.math.sum([
            pm.math.sum(lag_coefs[i, 6] * train_data.values[lags - (i + 1): -(i + 1)], axis=-1)
            for i in range(lags)
        ])

        mean = intercept + pm.math.stack([ar_anger, ar_fear, ar_sadness, ar_none, ar_irony, ar_love, ar_joy])

        obs = pm.Normal("obs", mu=mean, sigma=noise, observed=train_data[lags:], dims=("time", "vars"))

    os.environ["PATH"] += os.pathsep + 'C:\\Program Files\\Graphviz\\bin'
    gv = pm.model_to_graphviz(BVAR_model)
    gv.render("graph", format="png")
    # with BVAR_model:
    #     trace = pm.sample(chains=2, random_seed=88, cores=1)

    # az.plot_trace(trace)

def main():
    az.style.use("arviz-darkgrid")

    alphas = loadAlphas(32, 3)
    BVAR(alphas)
    # for emotion in emotions:
    #     plotSeries(alphas[emotion])
    # print(alphas)


if __name__ == "__main__":
    main()














