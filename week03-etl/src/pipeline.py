"""Run the ETL pipeline."""

import logging

from config import EMPLOYEE_CSV
from extract import extract_employees

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s",
)

logger = logging.getLogger(__name__)


def main() -> None:
    """Run the extraction stage."""
    employees = extract_employees(EMPLOYEE_CSV)

    logger.info("Employees extracted: %s", len(employees))

    for employee in employees:
        logger.info(employee)


if __name__ == "__main__":
    main()
