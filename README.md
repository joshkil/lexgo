# lexgo

[![PyPI](https://img.shields.io/pypi/v/lexgo.svg)](https://pypi.org/project/lexgo/)
[![Changelog](https://img.shields.io/github/v/release/joshkil/lexgo?include_prereleases&label=changelog)](https://github.com/joshkil/lexgo/releases)
[![Tests](https://github.com/joshkil/lexgo/actions/workflows/test.yml/badge.svg)](https://github.com/joshkil/lexgo/actions/workflows/test.yml)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/joshkil/lexgo/blob/master/LICENSE)

A lexicon search tool for language teachers and students. Explore word patterns in any language. 

## Installation

Install this tool using `pip`:
```bash
pip install lexgo
```
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
