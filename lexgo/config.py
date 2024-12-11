import pathlib

# Global Constants
DATA_DIR_NAME = "data"
DICT_PATHS = {
    "en" : pathlib.Path(__file__).parent.joinpath(DATA_DIR_NAME, "en.txt").absolute().as_posix(),
    "es" : pathlib.Path(__file__).parent.joinpath(DATA_DIR_NAME, "es.txt").absolute().as_posix(),
    "fr" : pathlib.Path(__file__).parent.joinpath(DATA_DIR_NAME, "fr.txt").absolute().as_posix(),
    "pt" : pathlib.Path(__file__).parent.joinpath(DATA_DIR_NAME, "pt.txt").absolute().as_posix(),
    "de" : pathlib.Path(__file__).parent.joinpath(DATA_DIR_NAME, "de.txt").absolute().as_posix(),
    "it" : pathlib.Path(__file__).parent.joinpath(DATA_DIR_NAME, "it.txt").absolute().as_posix()
}

LARGEST_WORD = 50