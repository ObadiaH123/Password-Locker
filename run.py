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

def save_credential(credential):
    """
    function that save credential
    """
    credential.save_credential()
