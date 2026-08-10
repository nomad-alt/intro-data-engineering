"""Run the ETL pipeline."""

import logging

from extract import extract_file

try:
    from .config import DEPARTMENT_JSON, EMPLOYEE_CSV
except ImportError:  # pragma: no cover - fallback for direct script execution
    from config import DEPARTMENT_JSON, EMPLOYEE_CSV

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s",
)

logger = logging.getLogger(__name__)


def main() -> None:
    """Run the extraction stage."""
    employees = extract_file(EMPLOYEE_CSV)
    departments = extract_file(DEPARTMENT_JSON)

    logger.info("Employees extracted: %d", len(employees))
    logger.info("Departments extracted: %d", len(departments))


if __name__ == "__main__":
    main()
