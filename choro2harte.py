import numpy as np
import pandas as pd
import re

def parse_extensions(extensions):
    ext = ",".join([ 
        e
        .replace("omit", "*") \
        .strip("(").strip(")") \
        for e in re.findall(r'\(.*?\)', extensions) 
    ])
    return f"({ext})"


def choro2harte(chord, type="root"):
    """Transforms chord symbols in Choro Songbook Corpus format to 
    Harte et al's chord syntax. See Harte, C. A., Sandler, M., 
    Abdallah, S., & Gómez, E. (2005). Symbolic representation of 
    musical chords: A proposed syntax for text annotations. 
    Proceedings of the 4th International Conference on Music Information 
    Retrieval (ISMIR), 56, 66--71.

    Parameters
    ----------
    chord : str 
        Chord symbol as encoded in the _Choro Songbook Corpus_.

    Returns
    -------
    str
        Chord symbol conforming to syntax in Harte et al. (2005).
    """

    assert type in ["root", "rn"]

    harte = ""
    if chord.chord == "NC":
        harte = "N"
    else:
        # ROOT
        harte += chord.root if type == "root" else chord.sd
        
        # TYPE
        if chord.type == "m":
            if chord.added == "7":
                harte += ":min7"
            elif chord.added == "6":
                harte += ":min6"
            else: 
                harte += ":min"
        elif chord.type == "o":
            harte += ":dim"
        elif chord.type is np.nan:
            if chord.added == "7":
                harte += ":7"
            elif chord.added == "7M":
                harte += ":maj7"
            elif chord.added == "6":
                harte += ":maj6"
            else:
                harte += ":maj"

        # EXTENSIONS
        if chord.extensions is not np.nan:
            harte += parse_extensions(chord.extensions)

        # SPECIFIC SHORTHANDS
        harte = harte.replace("min7(b5)", "hdim7") \
                .replace("maj(#5)", "aug") \
                .replace("maj7(9)", "maj9") \
                .replace(":7(9)", ":9") \
                .replace("min(7M)", "minmaj7") \
                .replace("add9", "9") \
                .replace("min7(9)", "min9") \
                .replace("(9,7M)", "(7,9)") \
                .replace("dim(7M)", "dim(7)")
        
        # BASS
        if chord.bass_note is not np.nan:
            harte += "/" + chord.bass_note

    return harte


if __name__ == "__main__":
    
    # read data
    df = pd.read_csv("data/choro.tsv", sep="\t", index_col=0)

    # create new column
    df["harte"] = df.apply(lambda x: choro2harte(x, type="root"), axis=1)
    df["rn_harte"] = df.apply(lambda x: choro2harte(x, type="rn"), axis=1)

    # sort columns
    df = df[['global_key', 'local_key', 'global_meter', 'local_meter', 'local_mode',
       'global_mode', 'path', 'phrase', 'part', 'bar_no', 'duration', 'chord', 'harte',
       'root', 'rn_chord', 'rn_harte', 'sd', 'type', 'added', 'extensions', 'bass_note',
       'songbook', 'title', 'composer', 'sub_genre', 'year', 'filename' ]]
    
    # export to file
    df.to_csv("data/choro.tsv", sep="\t", index=False)