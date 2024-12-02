import  lexgo.trie

# Global Constants
ENGLISH_DICT_PATH = "eng_words_alpha.txt"

# Global Variables
dictionary = lexgo.trie.Node("", False)

def load():
    dictionary_path = ENGLISH_DICT_PATH
    with open(dictionary_path) as f:
        # Read the dictionary file into a list
        words = list(f)
        lexgo.trie.setup(words, dictionary)