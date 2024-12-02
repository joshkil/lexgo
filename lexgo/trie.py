# Trie Node Class
# value    - each node has a value which is a single character
# children - each node has a dictionary of child nodes. the key is the 
#            character represented by the child node
# is_word  - a boolean value indicating if this node is the end of
#            a "word path". 
class Node:
    def __init__(self, value, is_word):
        self.value = value
        self.children = {}
        self.is_word = is_word

def add_to_trie(word, root):
    # recursion base case
    if len(word) == 0:
        root.is_word = True
        return

    # split off the first character of the current word
    first_char = word[0:1]
    sufx = word[1:]

    # recursive step
    if first_char in root.children:
        add_to_trie(sufx, root.children[first_char])
    else:
        new_node = Node(first_char, False)
        root.children[first_char] = new_node
        add_to_trie(sufx, new_node)

def setup(words, root):
    for w in words:
        add_to_trie(w.strip(), root)

# convenience function to initiate recursion
def find_words(word, node):
    fwords = list()
    return find_words_r(word, node, fwords)

# recursive search
def find_words_r(word, node, fwords, path=""):

    # recursion base case
    if len(word) == 0:
        if node.is_word:
            fwords.append(path)
        return fwords

    # split the first character off the curent word
    first_char = word[0:1]
    sufx = word[1:] 

    # recursive step
    if first_char in node.children:
        return find_words_r(sufx, node.children[first_char], fwords, path + first_char)
    elif first_char == '.':
        for k in node.children.keys():
            find_words_r(sufx, node.children[k], fwords, path + k)
        return fwords
    elif first_char == '*':
        # if we encounter a '*' we exand it into '.' characters
        # we try every possible length of word 
        for k in range(1,MAX_ENG_WORD_LENGTH-(len(path)+ len(sufx))):
            expansion = "."*k
            sufx = expansion + sufx
            find_words_r(sufx, node, fwords, path)
        return fwords
    else:
        return fwords