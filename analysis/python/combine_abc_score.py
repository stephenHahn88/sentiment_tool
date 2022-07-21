import ms3
import pandas as pd
import matplotlib.pyplot as plt


def printPanda(df: pd.DataFrame, rows=True, cols=True):
    """Prints pandas dataframe without abbreviation ellipses"""
    pd.set_option('expand_frame_repr', False)
    pd.set_option('display.max_rows', len(df)) if rows else 0
    pd.set_option('display.max_columns', 100) if cols else 0
    print(df)
    pd.reset_option('display.max_rows') if rows else 0
    pd.reset_option('display.max_columns') if cols else 0
    pd.reset_option('expand_frame_repr')


def gatherPhrases(tsv_path: str):
    """Retrieve a list of phrases in the tsv file provided in `tsv_path`"""
    df = pd.read_csv(tsv_path, sep="\t")

    phraseIndeces = []
    currStartIndex = 0
    while currStartIndex < len(df):
        # Get the next index that has phraseend == True
        currEndIndex = df.iloc[currStartIndex + 1:].loc[df["phraseend"] == True].iloc[0].name

        phraseIndeces.append((currStartIndex, currEndIndex))
        currStartIndex = currEndIndex + 1

    return [df.iloc[start:end+1] for start, end in phraseIndeces]


def readScore(filepath):
    s = ms3.Score(filepath)
    # Retrieve verticalities for each instrument WITHOUT RESTS
    df = s.mscx.chords
    # separate dynamic data
    dynamics = df[df.dynamics.notna()]
    df = df[df.duration != 0].sort_values(['mc', 'mc_onset']).reset_index()
    # Sort data by time
    printPanda(df)
    # printPanda(dynamics.sort_values(["mc", "mc_onset"]))
    return df


def plot(df: pd.DataFrame):
    plt.figure()
    df.duration \
        .value_counts() \
        .plot(kind="pie")
    plt.show()


if __name__ == "__main__":
    # phrases = gatherPhrases("../annotations/abc_dataset/tsv/op18_no1_mov1.tsv")
    # printPanda(phrases[1])
    # df = readScore("../annotations/abc_dataset/converted_mscx/op18_no1_mov1.mscx")
    # plot(df)
    p = ms3.Parse('../annotations/abc_dataset/converted_mscx', key='pergo')
    p.parse_mscx()
    p.store_lists(
        # notes_folder="table/notes_tables",
        # rests_folder="../abc_dataset/notes_tables",
        # notes_and_rests_folder="../annotations/abc_dataset/notes_tables",
        chords_folder="../table/chords_tables",
        # simulate=True

    )
