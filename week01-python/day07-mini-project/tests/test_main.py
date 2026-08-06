import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from src.main import main


def test_main_creates_pipeline_outputs(capsys) -> None:
    main()

    output = capsys.readouterr().out
    assert "Pipeline completed successfully." in output
    assert "Employees processed: 5" in output

    data_dir = Path(__file__).resolve().parent.parent / "data"
    assert (data_dir / "employees_processed.csv").exists()
    assert (data_dir / "summary.json").exists()
