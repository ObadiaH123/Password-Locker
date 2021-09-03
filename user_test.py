import unittest
from user import User
from user import Credentials
class TestUser(unittest.TestCase):
    def setUp(self):
        """
        a method that run before a test
        """
        self.new_user = User("ObadiaH","Kiprotich")

    def tearDown(self):
        """
        a cleanup method after each test runs
        """
        User.user_list = []