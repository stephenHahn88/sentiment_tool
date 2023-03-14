import json
import numpy as np

from data.organize_schubert_data import getAllDF, readPickleAsDF
from DHMM.gatherMatrices import getMixtureTransitionMatrices

EMOTIONS = ["anger", "fear", "sadness", "none", "irony", "love", "joy"]

def getJSONTransitionMatrices(just_transition_matrix=False):

    all_dfs = readPickleAsDF()
    transition_matrices = getMixtureTransitionMatrices(all_dfs)
    transition_matrices = list(transition_matrices)

    # Transition matrices for each emotion is saved as an ndarray: convert to python list for serialization
    for emotion in EMOTIONS:
        transition_matrices[0][emotion] = transition_matrices[0][emotion].tolist()
    
    with open('transition_matrices.json', 'w') as f:
        if just_transition_matrix:
            json.dump(transition_matrices[0], f, indent=1)
        else:
            json.dump(transition_matrices, f, indent=1)
