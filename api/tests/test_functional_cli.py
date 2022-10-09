from typer.testing import CliRunner
from stuart.cli import main

runner = CliRunner()

def test_add_parameters():
    result = runner.invoke(
        main, ["add-parameters", "--max-capacity=45", "--capacity-required=10"]
    )
    assert result.exit_code == 0
    assert "New Couriers Capacity Added" in result.stdout