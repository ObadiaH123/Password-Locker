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
    while True:
        print("Use these short codes: \n cc - create new credential \n dc - display credentials \n fc -find a credential \n gp - generate password \n del - delete credential \n ex - exit the credential list")
        short_code = input().lower().strip()
        if short_code == "cc":
            print("Create New Credential")
            print("."*20)
            print("Account name ....")
            account = input().lower()
            print("Your account username")
            username = input()
            while True:
                print("TP - Type your own pasword if you had and account:\n GR - Generate a random password")
                password_Choice = input().lower().strip()
                if password_Choice == 'tp':
                    password = input("Enter Your Own Password\n")
                    break
                elif password_Choice == 'gr':
                    password = generate_password(password)
                    break
                else:
                    print("Invalid password please try again")
            save_credentials(create_new_credential(account,username,password))
            print('\n')
            print(f"Account Credential for:Account {account} :Username: {username} - Password:{password} created succesfully")
            print('\n')
        elif short_code == "dc":
            print("Enter the Account Name you want to view")
            search_name = input().lower()
            if find_credentials(search_name):
                search_credentials = find_credentials(search_name)
                print(f"Name : {search_credential.username}")
                print('-' * 40)
                print(f"User Name : {search_credential.username} Password :{search_credential.password}")
                print('-' * 40)
            else:
                print("That credentials you searching doesn't exist")
                print('\n')
        elif short_code == "del":
            print("Enter account name of the Credentials you want to delete")
            search_name = input().lower()
            if find_credentials(search_name):
                search_credential = find_credentials(search_name)
                print("_"*40)
                search_credential.delete_credentials()
                print('\n')
                print(f"Your stored credentials for : {search_credential.account} successfully deleted!!!")
                print('\n')
            else:
                print("The Credential you want to delete does not exist")

        elif short_code == 'gp':

            password = generate_password(password)
            print(f" {password} Successful. You use it now.")
        elif short_code == 'ex':
            print("Thanks for using PasswordLocker.See you next time!")
            break
        else:
            print("Wrong entry!!!Check your entry again")
    else:
        print("Please enter a valid input to continue")

if __name__ == '__main__':
    main()


