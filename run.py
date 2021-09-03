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
    return Credentials.credentials_exist(account)

def generate_password(self):
    """
    function that generates a password for the user randomly
    """
    auto_password = Credentials.generate_password(self)
    return auto_password

def main():
    print("Welcome User to password locker.\n To continue enter any of the following short initials\n cna --- Create new Account \n ah --- Already have an Account \n ")
    short_code = input("").lower().strip()
    if short_code == "cna":
        print("Sign Up")
        print('*' * 50)
        print("Username")
        username = input()
        print("password")
        password = ""
        while True:
            print("OP - Use your own password?\n RP - Generate a random password")
            pass_choice = input().lower().strip()
            if pass_choice == "op":
                print("\n")
                password = input("Enter your password: \n")
                break
            elif pass_choice == "rp":
                password = generate_password(password)
                break
            else:
                print("Invalid input")
        save_user(create_new_user(username,password))
        print("*"*60)
        print(f"New Account Created for: {username}, Successfully and your password is: {password}")
        print("*"*60)
    elif short_code == "ah":
        print("*"*50)
        print("Enter your username and password to log in: ")
        print("*"*40)
        username = input("User name: \n")
        password = input("Password: \n")
        login = login_user(username,password)
        if login_user == login:
            print(f"Hello {username} Welcome to my Password-Locker" )
            print("\n")
