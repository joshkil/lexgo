import  lexgo.trie
import importlib.resources
import pathlib

# Global Constants
ENGLISH_DICT_PATH = "eng_words_alpha.txt"

# Global Variables
dictionary = lexgo.trie.Node("", False)

def load():
    dictionary_path = ENGLISH_DICT_PATH
    data_file = pathlib.Path(__file__).parent.joinpath("data", dictionary_path)
    with open(data_file) as f:
        # Read the dictionary file into a list
        words = list(f)
        lexgo.trie.setup(words, dictionary)