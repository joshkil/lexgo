import click
from lexgo import config
from lexgo import trie
import lexgo.trie


@click.command()
@click.argument(
    "word"
)
@click.version_option()
@click.option("-e", "--exclude", default="",
    help="Individual letters that MUST NOT appear in found words.",
)
@click.option("-i", "--include", default="",
    help="Individual letters that MUST appear in found words.",
)
@click.option("-xp", type=(str, int), multiple=True, default=[],
    help="A letter and a position in which it must not appear.",
)
def lexgo(word, exclude, include, xp):
    '''
    Search for WORD.

    WORD can be made up of letters, dots ('.'), and stars ('*'). A dot is a placeholder for any
    one letter. A star is a placeholder for one or more letters.  

    EXAMPLES: 

    \b
    lexgo .est - search for words that start with any letter and end 'est'
    lexgo ..ed - search four letter words ending 'ed'
    lexgo *est - search all words that end in 'est'
    lexgo b.. -e td -i a -xp ns 3
               - search 3 letter words starting with b, without letters 't' or 'd',
                 with letter a, and without letters 'n' or 's' in the 3rd letter.
    '''
    config.load()
    fwords = trie.find_words(word, config.dictionary)
    candidates = []
    if exclude or include or (len(xp) > 0):
        for w in fwords:
            candidate = True
            for c in exclude:
                if c in w:
                    candidate = False
            for c in include:
                if c not in w:
                    candidate = False
            for tup in xp: 
                for c in tup[0]:
                    if w[tup[1]-1] == c:
                        candidate = False
            if candidate: 
                candidates.append(w)
    else:
        candidates.extend(fwords)
    click.echo(candidates)
