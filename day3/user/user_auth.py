from user import user
import json
def user_sign_up():
    new_user = user()
    user_name = input("Enter your username: ")
    new_user.name = user_name
    
    user_email = input("Enter your email: ")
    new_user.email = user_email
    user_phone = input("Enter your phone number: ")
    new_user.phone = user_phone
    user_password = input("Enter your password: ")
    user_confirm_password = input("Confirm your password: ")
    while user_password != user_confirm_password:
        print("Passwords do not match. Please try again.")
        user_password = input("Enter your password: ")
        user_confirm_password = input("Confirm your password: ")
    new_user.password = user_password

    new_user.save_users(new_user)



def user_login() -> dict:
    user_email = input("Enter your email: ")
    user_password = input("Enter your password: ")
    user_config = json.load(open("user/user_config.json"))
    #search for user in data file
    with open(user_config["users_data_file"], "r") as f:
        users_data = json.load(f)
        for user_data in users_data:
            if user_data["email"] == user_email and user_data["password"] == user_password:
                print("Login successful!")
                return user_data
        print("Invalid email or password.")
    return {}


    