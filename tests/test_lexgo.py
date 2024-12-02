from click.testing import CliRunner
from lexgo.cli import lexgo


def test_version():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(lexgo, ["--version"])
        assert result.exit_code == 0
        assert result.output.startswith("lexgo, version ")
