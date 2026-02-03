from .signup_page import signup_page 
from .login_page import login_page  
def welcome_page():
    print("Welcome to the Application!")
    while(True):        
        print("1. Sign Up")
        print("2. Log In")
        print("3. Exit")
        choice = input("Enter your choice (1 or 2 or 3): ")
        if choice == "1":
            signup_page()
        elif choice == "2":
            login_page()
        elif choice == "3":
            print("Exiting the application. Goodbye!")
            break

