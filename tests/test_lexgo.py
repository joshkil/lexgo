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

# --- Issue #2: --include option doesn't AND multiple letters ---

def test_include_single_letter():
    """Including a single letter should return only words containing that letter."""
    runner = CliRunner()
    result = runner.invoke(lexgo, ["-i", "z", "....."])
    assert result.exit_code == 0
    words = [w for w in result.output.strip().splitlines() if w]
    assert len(words) > 0, "Expected at least one 5-letter word containing 'z'"
    for word in words:
        assert "z" in word, f"Expected all words to contain 'z', got '{word}'"

def test_include_multiple_letters_and():
    """Including 'aei' should return only words containing ALL of a, e, and i (AND, not OR).
    Regression test for Issue #2."""
    runner = CliRunner()
    result = runner.invoke(lexgo, ["-i", "aei", "....."])
    assert result.exit_code == 0
    words = [w for w in result.output.strip().splitlines() if w]
    assert len(words) > 0, "Expected at least one 5-letter word containing a, e, and i"
    for word in words:
        assert "a" in word, f"Expected all words to contain 'a', got '{word}'"
        assert "e" in word, f"Expected all words to contain 'e', got '{word}'"
        assert "i" in word, f"Expected all words to contain 'i', got '{word}'"

def test_include_multiple_letters_excludes_partial_matches():
    """Words with only some of the included letters should not appear in results."""
    runner = CliRunner()
    result = runner.invoke(lexgo, ["-i", "aei", "....."])
    assert result.exit_code == 0
    words = [w for w in result.output.strip().splitlines() if w]
    for word in words:
        assert not ("a" in word and "e" not in word), f"'{word}' has 'a' but not 'e'"
        assert not ("a" in word and "i" not in word), f"'{word}' has 'a' but not 'i'"

def test_include_duplicate_letters():
    """Duplicate letters in --include (e.g. 'aai') should work without error."""
    runner = CliRunner()
    result = runner.invoke(lexgo, ["-i", "aai", "....."])
    assert result.exit_code == 0
    words = [w for w in result.output.strip().splitlines() if w]
    for word in words:
        assert "a" in word and "i" in word, f"Expected all words to contain 'a' and 'i', got '{word}'"


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