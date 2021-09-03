import unittest
from user import User
from user import Credentials
class TestUser(unittest.TestCase):
    def setUp(self):
        """
        a method that run before a test
        """
        self.new_user = User("ObadiaH","bett@123")

    def tearDown(self):
        """
        a cleanup method after each test runs
        """
        User.user_list = []

    def test_init(self):
        """
        checking if the if the object is initialized correctly
        """
        self.assertEqual(self.new_user.username,"ObadiaH")
        self.assertEqual(self.new_user.password,"bett@123")

    def test_save_user(self):
        """
        check if the new instance of the object has been created
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)

class TestCredentials(unittest.TestCase):
    """
    A test class that defines a test cases for class Credentials
    """
    def setUp(self):
        """
        a method that run before each individual test cases runs
        """
        self.new_credentials = Credentials("Kiprotich","obadiah@123","123bett")

    def tearDown(self):
