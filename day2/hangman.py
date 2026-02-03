import random

if __name__ == "__main__":
    words = ["Alahly", "Barcelona", "Liverpool", "Manchester City"]
    random_number = random.randint(0, len(words) - 1)
    target_club = words[random_number]
    target_club_length = len(target_club)
    hangman_flag = False
    user_trials = 7
    user_guess = "_" * target_club_length
    guessed = 0
    for i in range(target_club_length):
        if(target_club[i] == " "):
            guessed += 1
            user_guess = user_guess[:i] + " " + user_guess[i+1:]



    while(not hangman_flag and user_trials):
        print(user_guess)

        input_guess = input("Enter a char to guess: ")
        while(not (input_guess.isalpha()) and len(input_guess) != 1 and input_guess not in user_guess):
            input_guess = input("Enter a valid char to guess: ")
        
        input_guess = input_guess.lower()
        check_guess = False
        for i in range(target_club_length):
            target_char  = target_club[i].lower()
            if(target_char == input_guess):
                user_guess = user_guess[:i] + target_club[i] + user_guess[i+1:]
                guessed +=1
                check_guess = True
        if(not check_guess):
            user_trials -= 1
            if(user_trials == 0):
                print("You Lost!")
                print(f"Club was: {target_club}")

                
        if(guessed == target_club_length):
            print("You Won!")
            print(f"Club is: {user_guess}")
            hangman_flag = True



########## improved version

# import random

# if __name__ == "__main__":
#     words = ["Alahly", "Barcelona", "Liverpool", "Manchester City"]
#     target_club = random.choice(words)
#     target_club_length = len(target_club)

#     hangman_flag = False
#     user_trials = 7
#     user_guess = "_" * target_club_length
#     guessed = 0

#     char_indices = {}
#     for i, ch in enumerate(target_club):
#         if ch == " ":
#             user_guess = user_guess[:i] + " " + user_guess[i+1:]
#             guessed += 1
#             continue

#         key = ch.lower()
#         char_indices.setdefault(key, []).append(i)

#     while not hangman_flag and user_trials:
#         print(user_guess)

#         input_guess = input("Enter a char to guess: ")
#         while not (input_guess.isalpha() and len(input_guess) == 1):
#             input_guess = input("Enter a valid char to guess: ")

#         input_guess = input_guess.lower()

#         if input_guess in char_indices:
#             for idx in char_indices[input_guess]:
#                 if user_guess[idx] == "_":   
#                     user_guess = user_guess[:idx] + target_club[idx] + user_guess[idx + 1:]
#                     guessed += 1
#         else:
#             user_trials -= 1
#             if user_trials == 0:
#                 print("You Lost!")
#                 print(f"Club was: {target_club}")
    

#         if guessed == target_club_length:
#             print("You Won!")
#             print(f"Club is: {user_guess}")
#             hangman_flag = True

