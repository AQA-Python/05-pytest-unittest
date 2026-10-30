import pytest

from src.user import User
from src.user_manager import UserManager


@pytest.fixture
def user():
    return User(
        user_id=1,
        name="Alex",
        age=25,
        email="alex@test.com"
    )


@pytest.fixture
def manager():
    return UserManager()