from MockDynamoDbExample.src.service import Service
from moto import mock_dynamodb
from unittest import TestCase


@mock_dynamodb
class TestService(TestCase):
    def setUp(self) -> None:
        """Method called before every test case is executed"""

        # Create an instance of the Service class
        self.service = Service("user", env="test")

    def tearDown(self) -> None:
        """Method called after every test case has finished execution"""

        # Clear the table after use
        self.service.delete_table()

        # Reset the service variable
        self.service = None

    def test_create_user(self):
        username = "test-mike"
        age = 19
        first_name = "Mike"
        last_name = "Ross"
        email = "test_mike@example.com"

        try:
            self.service.create_user(username, email, age, first_name, last_name)
        except Exception as exc:
            assert False, f"service.create_user raised an exception {exc}"
        assert True

    def test_get_user_by_username(self):
        username = "test-mike"
        age = 19
        first_name = "Mike"
        last_name = "Ross"
        email = "test_mike@example.com"

        # Create a user in the database
        try:
            self.service.create_user(username, email, age, first_name, last_name)
        except Exception as exc:
            assert False, f"service.create_user raised an exception {exc}"

        # Get the user by username from the database
        try:
            response = self.service.get_user_by_username(username)
        except Exception as exc:
            assert False, f"service.get_user_by_username raised an exception {exc}"

        # Verify the details
        assert response is not None
        assert response["username"] == username
        assert response["age"] == age
        assert response["email"] == email
        assert response["first_name"] == first_name
        assert response["last_name"] == last_name
