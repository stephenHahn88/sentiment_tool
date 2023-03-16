import json
import numpy as np

from data.organize_schubert_data import getAllDF, readPickleAsDF
from DHMM.gatherMatrices import getMixtureTransitionMatrices

from music21.key import Key
from music21.roman import RomanNumeral as RN

EMOTIONS = ["anger", "fear", "sadness", "none", "irony", "love", "joy"]

def getJSONTransitionMatrices(load_from_pickle=False, just_transition_matrix=False):

    all_dfs = None

    if load_from_pickle:
        all_dfs = readPickleAsDF()
    else:
        all_dfs = getAllDF()

    transition_matrices = getMixtureTransitionMatrices(all_dfs)
    transition_matrices = list(transition_matrices)

    # Transition matrices for each emotion is saved as an ndarray: convert to python list for serialization
    for emotion in EMOTIONS:
        transition_matrices[0][emotion] = transition_matrices[0][emotion].tolist()

    chords = dict()
    for chordRN in transition_matrices[1]:
        if chordRN == "START" or chordRN == "PAD":
            pass
        else:
            rn = RN(chordRN)
            rn.key = Key('C')
            # Keep octaves bounded
            harmony = [str(p).replace('-', 'b').replace('6', '5') for p in rn.pitches]
            chords[chordRN] = harmony

    with open('transition_matrices.json', 'w') as f:
        if just_transition_matrix:
            json.dump(transition_matrices[0], f, indent=1)
        else:
            json.dump(transition_matrices, f, indent=1)

    with open('notes_from_chord.json', 'w') as f:
        json.dump(chords, f, indent=1)

getJSONTransitionMatrices(load_from_pickle=True)