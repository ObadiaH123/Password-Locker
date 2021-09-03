from user import User,Credentials
def create_new_user(username,password):
    """
    function that create a new user
    """
    new_user = User(username,password)
    return new_user

def save_user(user):
    """
    function that save user
    """
    user.save_user()

def display_user(user):
    """
    function that display the user
    """
    return User.display_user()

def login_user(username,password):
    """
    function that log in user
    """
    checked_user = Credentials.verify_user(username,password)
    return checked_user

def create_new_credential(account,username,password):
    """
    function that create a new credentials
    """
    new_credentials = Credentials(account,username,password)
    return new_credential

def save_credentials(credentials):
    """
    function that add new credentials to the credentials list
    """
    credentials.save_user_credentials()

def delete_credentials(credentials):
    """
    function that delete credentials from the credentials list
    """
    credentials.delete_credentials()

def find_credentials(account):
    """
    function that find credentials from the credentials list by an account name 
    """
    return Credentials.find_by_number(account)

def check_credentials(account):
    """
    function that check if a credential exists with that account name
    """
    return Credentials.credential_exist(account)
