

if __name__ == "__main__":
    flag = 1

    while(flag):
        user_input = input("Enter new number or done: ")
        if(not(user_input.isnumeric()) and user_input != "done"):
            print("Error: Not a number")
        elif(user_input == "done"):
            flag = 0
        else:
            print(user_input)