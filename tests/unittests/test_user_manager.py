import unittest
import allure

from src.user import User
from src.user_manager import UserManager


@allure.feature("User Manager")
class TestUserManager(unittest.TestCase):

    def setUp(self):
        self.manager = UserManager()

        self.user = User(
            user_id=1,
            name="Alex",
            age=25,
            email="alex@test.com"
        )

    def tearDown(self):
        self.user = None
        self.manager = None

    @allure.story("Add user")
    @allure.title("Add valid user")
    def test_add_user(self):
        pass

    @allure.story("Add user")
    @allure.title("Duplicate id raises ValueError")
    def test_add_user_duplicate_id(self):
        pass

    @allure.story("Add user")
    @allure.title("Invalid id type raises TypeError")
    def test_add_user_invalid_id_type(self):
        pass

    @allure.story("Add user")
    @allure.title("Empty name raises ValueError")
    def test_add_user_empty_name(self):
        pass

    @allure.story("Add user")
    @allure.title("Short name raises ValueError")
    def test_add_user_short_name(self):
        pass

    @allure.story("Add user")
    @allure.title("Invalid name type raises TypeError")
    def test_add_user_invalid_name_type(self):
        pass

    @allure.story("Add user")
    @allure.title("Negative age raises ValueError")
    def test_add_user_negative_age(self):
        pass

    @allure.story("Add user")
    @allure.title("Age greater than 120 raises ValueError")
    def test_add_user_large_age(self):
        pass

    @allure.story("Add user")
    @allure.title("Invalid age type raises TypeError")
    def test_add_user_invalid_age_type(self):
        pass

    @allure.story("Add user")
    @allure.title("Invalid email raises ValueError")
    def test_add_user_invalid_email(self):
        pass

    @allure.story("Add user")
    @allure.title("Invalid email type raises TypeError")
    def test_add_user_invalid_email_type(self):
        pass

    @allure.story("Get user")
    @allure.title("Get existing user")
    def test_get_existing_user(self):
        pass

    @allure.story("Get user")
    @allure.title("Get missing user")
    def test_get_missing_user(self):
        pass

    @allure.story("Remove user")
    @allure.title("Remove existing user")
    def test_remove_user(self):
        pass

    @allure.story("Remove user")
    @allure.title("Remove missing user")
    def test_remove_missing_user(self):
        pass

    @allure.story("Get all users")
    @allure.title("Get users from empty manager")
    def test_get_all_users_empty(self):
        pass

    @allure.story("Get all users")
    @allure.title("Get users list")
    def test_get_all_users(self):
        pass

    @allure.story("Count users")
    @allure.title("Count users in empty manager")
    def test_count_users_empty(self):
        pass

    @allure.story("Count users")
    @allure.title("Count users")
    def test_count_users(self):
        pass