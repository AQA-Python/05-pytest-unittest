import pytest
import allure

from src.user import User


@allure.feature("User")
@allure.story("is_adult")
@pytest.mark.parametrize(
    "age, expected",
    [
        (17, False),
        (18, True),
        (19, True)
    ]
)
def test_is_adult(age, expected):
    pass


@allure.feature("User")
@allure.story("to_dict")
@allure.title("Convert user to dictionary")
def test_to_dict(user):
    pass