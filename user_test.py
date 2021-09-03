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
        """
        method that does clean up after each test run
        """
        Credentials.credentials_list = []
    def test_details(self):
        """
        Test case to check if a new Credentials instance has been initialized correctly
        """
        self.assertEqual(self.new_credentials.account,"kiprotich")
        self.assertEqual(self.new_credentials.username,"obadiah@123")
        self.assertEqual(self.new_credentials.password,"123bett")

    def test_save_credentials(self):
        """
        test case to test if the credentials object is saved into the credentials list
        """
        self.new_credentials.save_user_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

    def test_save_many_account(self):
        """
        test to check if we can save multiple credentials objects to our credentials list
        """
        self.new_credentials.save_user_credentials()
        test_credential = Credentials("Taphe","Taphees","taphe123")
        test_credential.save_user_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)

    def test_find_credential(self):
        """
        test to check if we can find a credential entry by account name and display the details of the credential
        """
        
        self.new_credentials.save_user_credentials()
        test_credentials = Credentials('Taphe','Taphees','taphe123')
        test_credentials.save_user_credentials()

        the_credential = Credentials.find_by_number("Taphe")
        self.assertEqual(the_credential.account,test_credentials.account)

    def test_creditial_exist(self):
        """
        test to check if we can return a true or false based on whether we find or can't find the credential.
        """
        self.new_credentials.save_user_credentials()
        test_credentials = Credentials('Taphe','Taphees','taphe123')
        test_credentials.save_user_credentials()
        
        found_credential = Credentials.credentials_exist("Taphe")
        self.assertTrue(found_credential)

    def test_delete_credential(self):
        """
        test method to test if we can remove an account credentials from our credentials_list
        """
        self.new_credentials.save_user_credentials()
        test_credentials = Credentials('Taphe','Taphees','taphe123')
        test_credentials.save_user_credentials()
        
        
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credentials_list),1)

if __name__ == '__main__':
    unittest.main()

        

    

