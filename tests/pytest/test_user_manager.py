import pytest
import allure

from src.user import User


@allure.feature("User Manager")
@allure.story("Add user")
def test_add_user(manager, user):
    pass


@allure.feature("User Manager")
@allure.story("Add user")
def test_add_user_duplicate_id(manager):
    pass


@allure.feature("User Manager")
@allure.story("Add user")
@pytest.mark.parametrize(
    "invalid_id",
    [
        "1",
        None,
        1.5
    ]
)
def test_invalid_id(manager, invalid_id):
    pass


@allure.feature("User Manager")
@allure.story("Add user")
@pytest.mark.parametrize(
    "name",
    [
        "",
        "A"
    ]
)
def test_invalid_name(manager, name):
    pass


@allure.feature("User Manager")
@allure.story("Add user")
@pytest.mark.parametrize(
    "age",
    [
        -1,
        121
    ]
)
def test_invalid_age(manager, age):
    pass


@allure.feature("User Manager")
@allure.story("Add user")
@pytest.mark.parametrize(
    "email",
    [
        "test",
        "gmail.com"
    ]
)
def test_invalid_email(manager, email):
    pass


@allure.feature("User Manager")
@allure.story("Get user")
def test_get_existing_user(manager, user):
    pass


@allure.feature("User Manager")
@allure.story("Get user")
def test_get_missing_user(manager):
    pass


@allure.feature("User Manager")
@allure.story("Remove user")
def test_remove_user(manager, user):
    pass


@allure.feature("User Manager")
@allure.story("Remove user")
def test_remove_missing_user(manager):
    pass


@allure.feature("User Manager")
@allure.story("Get all users")
def test_get_all_users(manager):
    pass


@allure.feature("User Manager")
@allure.story("Count users")
def test_count_users(manager):
    pass