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