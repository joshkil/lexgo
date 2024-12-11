# lexgo

[![PyPI](https://img.shields.io/pypi/v/lexgo.svg)](https://pypi.org/project/lexgo/)
[![Changelog](https://img.shields.io/github/v/release/joshkil/lexgo?include_prereleases&label=changelog)](https://github.com/joshkil/lexgo/releases)
[![Tests](https://github.com/joshkil/lexgo/actions/workflows/test.yml/badge.svg)](https://github.com/joshkil/lexgo/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/joshkil/lexgo/blob/master/LICENSE)

A lexicon search tool for language teachers and students. Explore word patterns in any language. 

![The wordle logo from New York Times](wordle.png)

Crack WORDLE in minutes using lexgo for hints. It's also great for cracking crossword puzzles. You can ask lexgo to find example words of specific lengths and with specific letters. 

## Installation

Install this tool using `pip`:
```bash
pip install lexgo
```
Python Package Index: https://pypi.org/project/lexgo/

## Usage

For help, run:
```bash
lexgo --help
```
You can also use:
```bash
python -m lexgo --help
```
## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:
```bash
cd lexgo
python -m venv venv
source venv/bin/activate
```
Now install the dependencies and test dependencies:
```bash
pip install -e '.[test]'
```
To run the tests:
```bash
python -m pytest
```
## Acknowledgements

The English lexicon used was taken from the [english-words](https://github.com/dwyl/english-words) repo. Thanks to the esteemed programer [@dwyl](https://github.com/dwyl) for his excelent work. 

The Spanish lexicon used was taken from the [diccionario-español.txt](https://github.com/JorgeDuenasLerin/diccionario-espanol-txt) repo. Gracias al estimado programador [@JorgeDuenasLerin](https://github.com/JorgeDuenasLerin) por su trabajo excelente. 

The French lexicon used was taken from the [French-Dictionary](https://github.com/hbenbel/French-Dictionary) repo. Merci au programmeur estimé [@hbenbel](https://github.com/hbenbel) pour son excellent travail.

The Portuguese lexicon used was taken from the [words-pt](https://github.com/jfoclpf/words-pt) repo. Obrigado ao estimado programador [@jfoclpf](https://github.com/jfoclpf) por seu excelente trabalho.

The German lexicon used was taken from the [wortliste](https://github.com/davidak/wortliste) repo. Vielen Dank an den geschätzten Programmierer [@davidak](https://github.com/davidak) für seine hervorragende Arbeit.

