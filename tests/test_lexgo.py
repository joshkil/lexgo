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

# --- Issue #3: Word length is not properly enforced ---

def test_word_length_dot_pattern_three_letters():
    """Searching 'b..' should return only 3-letter words, not longer words like 'bars'."""
    runner = CliRunner()
    result = runner.invoke(lexgo, ["b.."])
    assert result.exit_code == 0
    words = [w for w in result.output.strip().splitlines() if w]
    assert len(words) > 0, "Expected at least one 3-letter word starting with 'b'"
    for word in words:
        assert len(word) == 3, f"Expected 3-letter words only, got '{word}' (length {len(word)})"

def test_word_length_dot_pattern_four_letters():
    """Searching '.est' should return only 4-letter words ending in 'est', not 'tests' etc."""
    runner = CliRunner()
    result = runner.invoke(lexgo, [".est"])
    assert result.exit_code == 0
    words = [w for w in result.output.strip().splitlines() if w]
    assert len(words) > 0, "Expected at least one 4-letter word ending in 'est'"
    for word in words:
        assert len(word) == 4, f"Expected 4-letter words only, got '{word}' (length {len(word)})"

def test_word_length_exact_word_no_longer_matches():
    """Searching 'crane' should return only 'crane', not 'cranes', 'craneway', etc."""
    runner = CliRunner()
    result = runner.invoke(lexgo, ["crane"])
    assert result.exit_code == 0
    words = [w for w in result.output.strip().splitlines() if w]
    assert words == ["crane"], f"Expected only 'crane', got: {words}"

def test_word_length_star_wildcard_allows_multiple_lengths():
    """The '*' wildcard should still return words of varying lengths."""
    runner = CliRunner()
    result = runner.invoke(lexgo, ["*est"])
    assert result.exit_code == 0
    words = [w for w in result.output.strip().splitlines() if w]
    lengths = set(len(w) for w in words)
    assert len(lengths) > 1, "Expected words of multiple lengths when using '*' wildcard"

def test_word_length_issue3_boa_with_exclude():
    """Regression test for Issue #3: 'lexgo -e rd boa..' should return only 5-letter words.
    Previously returned shorter words like 'boas' (4) and 'boat' (4) due to -w flag unreliability."""
    runner = CliRunner()
    result = runner.invoke(lexgo, ["-e", "rd", "boa.."])
    assert result.exit_code == 0
    words = [w for w in result.output.strip().splitlines() if w]
    assert len(words) > 0, "Expected at least one match for 'boa..'"
    for word in words:
        assert len(word) == 5, f"Expected only 5-letter words, got '{word}' (length {len(word)})"
    # Verify the specific bad results from the issue are no longer returned
    assert "boas" not in words, "'boas' (4 letters) should not appear in results for 'boa..'"
    assert "boat" not in words, "'boat' (4 letters) should not appear in results for 'boa..'"