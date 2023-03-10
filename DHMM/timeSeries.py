import arviz as az
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import pickle
import pymc as pm
import os
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.api import VAR
from statsmodels.tools.eval_measures import rmse, aic, bic
from statsmodels.tsa.vector_ar.vecm import coint_johansen

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

# Based on https://www.analyticsvidhya.com/blog/2021/08/vector-autoregressive-model-in-python/
def augmentedDickeyFuller(series: pd.Series, title=''):
    print(f'Augmented Dickey-Fuller Test: {title}')
    result = adfuller(series.dropna(), autolag='AIC')  # .dropna() handles differenced data
    labels = [
        'ADF test statistic',
        'p-value',
        '# lags used',
        '# observations'
    ]
    print(result)
    out = pd.Series(result[0:4], index=labels)
    for key, val in result[4].items():
        out[f'critical value ({key})'] = val
    print(out.to_string())  # .to_string() removes the line "dtype: float64"
    if result[1] <= 0.05:
        print("Strong evidence against the null hypothesis")
        print("Reject the null hypothesis")
        print("Data has no unit root and is stationary")
    else:
        print("Weak evidence against the null hypothesis")
        print("Fail to reject the null hypothesis")
        print("Data has a unit root and is non-stationary")

# Based on https://www.machinelearningplus.com/time-series/vector-autoregression-examples-python/
def cointegrationTest(df: pd.DataFrame, alpha=0.10):
    out = coint_johansen(df, -1, 5)
    d = {0.90: 0, 0.95: 1, 0.99: 2}
    traces = out.lr1
    cvts = out.cvt[:, d[1-alpha]]
    def adjust(val, length=6): return str(val).ljust(length)

    print('Name   ::  Test Stat > C(95%)    =>   Signif  \n', '--' * 20)
    for col, trace, cvt in zip(df.columns, traces, cvts):
        print(adjust(col), ':: ', adjust(round(trace, 2), 9), ">", adjust(cvt, 8), ' =>  ', trace > cvt)


def myVAR(df: pd.DataFrame, criterion: str="aic"):
    test_len = 10
    train = df[:-test_len]
    test = df[-test_len:]

    model = VAR(train)
    criterions = {
        'aic': [],
        'bic': [],
        'fpe': [],
        'hqic': []
    }
    for i in range(1, 10):
        result = model.fit(i)
        criterions["aic"].append(result.aic)
        criterions["bic"].append(result.bic)
        criterions["fpe"].append(result.fpe)
        criterions["hqic"].append(result.hqic)
    optimal_i = np.argmin(criterions[criterion]) + 1
    model_fitted = model.fit(optimal_i)
    print(model_fitted.summary())
    model_fitted.plot()


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

    alphas: pd.DataFrame = loadAlphas(32, 3)
    alphas_diff = alphas.diff().dropna()[emotions]
    # cointegrationTest(alphas_diff.dropna()[emotions])
    myVAR(alphas_diff)

    # for emotion in emotions:
        # plotSeries(alphas[emotion])
        # augmentedDickeyFuller(alphas[emotion], emotion)

        # plotSeries(alphas_diff[emotion])
        # augmentedDickeyFuller(alphas_diff[emotion], emotion)
    # print(alphas)


if __name__ == "__main__":
    main()














