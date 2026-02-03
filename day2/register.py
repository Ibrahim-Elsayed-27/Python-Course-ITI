import re
def check_name(name: str) -> bool:
    if(len(name) < 3):
        return False
    return name.isalpha()

def check_email(email: str) -> bool:
    email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.fullmatch(email_pattern, email):
        return True
    else:
        return False
    

    
if __name__ == "__main__":
    print("#" * 10 + " Check Name " + "#" * 10)
    print(check_name("hi"))
    print(check_name("Ibrahim"))
    print(check_name("Ibrahim123"))

    print("#" * 10 + " Check Email " + "#" * 10)
    print(check_email("123@dfijg"))
    print(check_email("iahdsja@gihdi.com"))

    print("#" * 10 + " Check Register " + "#" * 10)
    name = input("Enter your name: ")
    while(not(check_name(name))):
        name = input("Enter a valid name: ")

    email = input("Enter you email:")
    while(not(check_email(email))):
        name = input("Enter a valid email: ")

    print(f"\n\nName: {name}\nEmail: {email}")