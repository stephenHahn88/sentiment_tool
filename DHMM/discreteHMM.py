import numpy as np
from hmmlearn import hmm
from gatherMatrices import getDiscretizedAlphaStates, getDiscretizedAlphaMatrices

emotions = ["anger", "fear", "sadness", "none", "irony", "love", "joy"]


def tupleToString(tup: tuple[int]):
    return [emotions[i] for i, b in enumerate(tup) if b]


def rnsToObs(rns: list[str], encoder):
    return [encoder[rn] for rn in rns]

def runHMM():
    transitionMatrix, emissionMatrix, startProbs, hiddenEncoder, hiddenDecoder, observedEncoder, observedDecoder = getDiscretizedAlphaMatrices()
    model = hmm.CategoricalHMM(
        n_components=len(hiddenEncoder),
    )
    model.n_features = len(observedEncoder)
    model.transmat_ = transitionMatrix
    model.emissionprob_ = emissionMatrix
    model.startprob_ = startProbs

    # print(transitionMatrix.shape)
    # print(emissionMatrix.shape)
    # print(startProbs.shape)
    X = np.array([rnsToObs(["i", "iv", "V", "i", "bIII", "IV", "V", "I", "bVI", "V", "iii", "iv", "V"], observedEncoder)])
    states = model.predict(X)
    print([tupleToString(hiddenDecoder[s]) for s in states])


def main():
    runHMM()

if __name__ == "__main__":
    main()








