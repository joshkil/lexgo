MAX_ENG_WORD_LENGTH = 45

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

# This function serializes a Trie Node into a string that can be stored. 
# This function is untested
def serialize(node):
    stk = list()
    serialized_trie = list()
    # load the stack with all children of root node
    stk.append(">")
    for k, v in node.children.items():
        stk.append(v)
    stk.append("<")

    while(len(stk)>0):
        cur_node = stk.pop()
        if not isinstance(cur_node, str):
            serialized_trie.append(cur_node.value)
            stk.append('>')
            for k, v in cur_node.children.items():
                stk.append(v)
            stk.append('<')
        else:
            serialized_trie.append(cur_node)

    return "".join(serialized_trie)

# This function builds a tree from a string representing a serialized
# tree. This function is untested. 
def deserialize(s):
    if not s or len(s) == 0:
        return None
    root = Node("",False)
    current = root
    stk = list()
    for c in s:
        if c == "<":
            stk.append(current)
        if c == ">":
            stk.pop()
        else:
            current = Node(c,"False")
            stk[-1].children[c] = current
    return root