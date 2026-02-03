from validation import *
import json
user_config = json.load(open("user/user_config.json"))
class user:
    def __init__(self):
        pass

    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, value: str):
        if not check_name(value):
            raise ValueError("Invalid name")
        self._name = value  

    @property
    def email(self):
        return self._email  
    @email.setter
    def email(self, value: str):    
        if not check_email(value, user_config["email_regex"]):
            raise ValueError("Invalid email")
        self._email = value
    
    @property
    def phone(self):
        return self._phone
    
    @phone.setter
    def phone(self, value: str):
        if not check_phone(value, user_config["phone_regex"]):
            raise ValueError("Invalid phone number")
        self._phone = value

    @property
    def password(self):
        return self._password   
    
    @password.setter
    def password(self, value: str):
        if not check_password(value, user_config["min_password_length"]):
            raise ValueError("Invalid password")
        self._password = value

    def __str__(self):
        return f"Name: {self.name}\nEmail: {self.email}\nPhone: {self.phone}"

    @staticmethod
    def save_users(new_user: "user"):
        try:
            with open(user_config["users_data_file"], "r") as file:
                users = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            users = []

        
        for user in users:
            if user["email"].lower() == new_user.email.lower():
                raise ValueError("Email already exists")

        users.append({
            "name": new_user.name,
            "email": new_user.email,
            "phone": new_user.phone,
            "password": new_user.password
        })

        with open(user_config["users_data_file"], "w") as file:
            json.dump(users, file, indent=4)



if __name__ == "__main__":
    u = user()
    u.name = "John Doe"
    u.email = "jonh@gamil.com"
    u.phone = "01012345678"
    u.password = "securePass123"
    user.save_users(u)