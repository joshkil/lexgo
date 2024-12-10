import subprocess
import re

def is_grep_installed():
    try:
        cp = subprocess.run(["grep", "--version"], capture_output=True)
        return "grep" in cp.stdout.decode("utf-8")
    except FileNotFoundError:
        return False
    
def is_alpha():
    return True

def is_alpha_dot_star(str):
    return re.fullmatch(r"[\w\.\*]*",str) != None

def is_alpha(str):
    return re.fullmatch(r"[\w\.\*]*",str) != None