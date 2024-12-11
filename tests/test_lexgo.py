from click.testing import CliRunner
from lexgo.cli import lexgo


def test_version():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(lexgo, ["--version"])
        assert result.exit_code == 0
        assert result.output.startswith("lexgo, version ")

def test_find_basic_word_eng():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(lexgo, ["test"])
        assert result.exit_code == 0
        assert result.output.startswith("test")

def test_find_basic_word_es():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(lexgo, ["-l", "es", "prueba"])
        assert result.exit_code == 0
        assert result.output.startswith("prueba")

def test_find_basic_word_fr():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(lexgo, ["-l", "fr", "tester"])
        assert result.exit_code == 0
        assert result.output.startswith("tester")

def test_find_basic_word_de():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(lexgo, ["-l", "de", "testen"])
        assert result.exit_code == 0
        assert result.output.startswith("testen")

def test_find_basic_word_pt():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(lexgo, ["-l", "pt", "teste"])
        assert result.exit_code == 0
        assert result.output.startswith("teste")

def test_find_basic_word_it():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(lexgo, ["-l", "it", "testare"])
        assert result.exit_code == 0
        assert result.output.startswith("testare")