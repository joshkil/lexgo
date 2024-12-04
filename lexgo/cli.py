import click
from lexgo import config
import subprocess
import pathlib

# Global Constants
ENGLISH_DICT_PATH = "eng_words_alpha.txt"

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
@click.option("-l", "--lang", type=click.Choice(['de', 'en', 'es', 'fr', 'pt'], case_sensitive=False), default='en',
    help="The language dictionary to search.",
)
def lexgo(word, exclude, include, xp, lang):
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
    # verify that word has only alpha '.' and '*'

    # convert the simple '*' into regular expression".*"
    word = str.replace(word, "*", ".*")
   
    # command stack
    command_stack = []

    # build initial grep command
    output = subprocess.Popen(["grep", "-w", "^" + word, config.DICT_PATHS[lang]], 
                        stdout=subprocess.PIPE, text=True)
    command_stack.append(output)

    # add exclusions
    if exclude:
        p = subprocess.Popen(["grep", "-v", "[{}]".format(exclude)], stdin=command_stack[-1].stdout, 
                                stdout=subprocess.PIPE, text=True)
        command_stack.append(p)
    
    # add inclusions
    if include:
        p = subprocess.Popen(["grep", "[{}]".format(include)], stdin=command_stack[-1].stdout, 
                                stdout=subprocess.PIPE, text=True)
        command_stack.append(p)

    # add positional exclusions (xp)
    if xp:
        for c, p in xp:
            gstr = "^" + "."*(p-1) + c
            p = subprocess.Popen(["grep", "-v", gstr], stdin=command_stack[-1].stdout, 
                                stdout=subprocess.PIPE, text=True)
            command_stack.append(p)

    # execute command stack
    out, error = command_stack[-1].communicate()
    if not error:
        click.echo(out)
