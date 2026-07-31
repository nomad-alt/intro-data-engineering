from src.exercises import classify_salary
from src.functions import square


def test_square():
    assert square(5) == 25


def test_classify_salary():
    assert classify_salary(35000) == "Low"
    assert classify_salary(50000) == "Medium"
    assert classify_salary(80000) == "High"
