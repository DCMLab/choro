# Harmony and Form in Brazilian Choro: A Data-Driven Approach to Musical Style Analysis

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.1442765.svg)](https://doi.org/10.5281/zenodo.1442765)

This project is one of the corpus projects conducted at the [Digital and Cognitive Musicology Lab (DCML)](http://dcml.epfl.ch/) at EPFL, Lausanne, Switzerland. For any questions regarding this project contact Fabian C. Moss (fabian.moss@epfl.ch) or Willian Fernandes Souza (willianfersou@yahoo.com.br).

## Abstract
The impetus of digital musicology and computational music analysis in recent years can largely be attributed to the increased creation of symbolic corpora. While covering diverse genres, encodings, formats, and methodologies, most datasets focus on melody and harmony to describe or infer idiosyncrasies of a certain style, genre, or composer. The current project contributes to this trend and aims at complementing data-driven approaches to musical style analysis by studying Choro, a Brazilian music genre beyond canonical datasets in computational research on classical  and popular music. A newly created dataset of transcriptions of chord symbols and the formal structure of pieces from the three volumes of the *Choro Songbook* (Chediak, Sève, Souza, & Dininho, 2009, 2011a, 2011b) is presented and analyzed against the backdrop of the textbook *A estrutura do Choro* (Almada, 2006) which contains a number of assumptions about this genre. The findings show that Choro composers employ different harmonic relations for chord transitions (recurring harmonic patterns) and key transitions within pieces, that the harmonies in regular 16- and 32-bar phrases conform to the hypermetrical structure of these phrases, and that historically older compositions employ chords with fewer modifications than younger pieces. These results constitute the first quantitative large-scale investigation of Choro and reveal central stylistic features of this musical idiom.

**References**

* Almada, C. (2006). A estrutura do choro. Rio de Janeiro: Editora Da Fonseca.
* Chediak, A., Sève, M., Souza, R., Dininho. (2009). Choro Songbook, volume 1. São Paulo: Lumiar Editora.
* Chediak, A., Sève, M., Souza, R., Dininho. (2011a). Choro Songbook, volume 2. São Paulo: Lumiar Editora.
* Chediak, A., Sève, M., Souza, R., Dininho. (2011b). Choro Songbook, volume 1. São Paulo: Lumiar Editora.

## Data Description

The data from all transcriptions is stored in `\data\choro.csv`. The individual transcriptions can be found in the `\data\transcriptions` folder. It contains the following columns:

**Key and Meter**
- `global_key`: global key per piece (e.g. `F`, `Dm`)
- `local_key`: local key at chord position
- `relative_key`: local key relative to the global key (e.g. `V`, `IIm`)
- `global_mode`: either `major` or `minor`
- `local_mode`: either `major` or `minor`
- `global_meter`: global meter per piece (e.g. `2/2`)
- `local_meter`: local meter at chord position
    
 **Form**
 - `path`: path from chord symbol to root node (e.g. `['P1', 'PartA', 'S']`)
 - `phrase`: phrase of chord symbol (e.g. `P1`) 
 - `part`: part of chord symbol (e.g. `PartA`)
    
**Chords**
- `bar_no`: bar number 
- `duration`: duration in quarter notes (e.g. `0.5` for a 1/2 note)
- `chord`: chord symbol as transcribed
- `root`: root note
- `rn_chord`: Roman numeral chord symbol (e.g. `V7(b9)`)
- `sd`: scale degree
- `type`: chord type (e.g. `m`, `o`)
- `added`: sixths and sevenths
- `extensions`: other chord extensions
- `bass_note`: bass note

**Metadata**
- `songbook`: songbook volume
- `title`: title of the piece
- `composer`: composer name(s)
- `sub_genre`: sub-genre
- `year`: year of composition (if available)
- `filename`: filename of the transcription
