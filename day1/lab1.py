#### Write a program that counts up the number of vowels [a, e, i, o, u] contained in the string.
# vowels = "aeiouAEIOU"
# example_string = "Hello, World!"

# vowels_count = 0
# for char in example_string:
#     if char in vowels:
#         vowels_count += 1

# print("Number of vowels in the string:", vowels_count)

#### Fill an array of 5 elements from the user, Sort it in descending and ascending orders then display the output.

# user_array = []
# for i in range(5):
#     element = int(input(f"Enter element {i+1}: "))
#     user_array.append(element)


# print("Original array:", user_array)
# user_array.sort()
# print("Array in ascending order:", user_array)
# user_array.sort(reverse=True)
# print("Array in descending order:", user_array)




#### Write a program that prints the number of times the string 'iti' occurs in anystring
# test_string = "iti is a part of iti and iti"
# substring = "iti"
# count = test_string.count(substring)
# print(f"The substring '{substring}' occurs {count} times in the string.")


#### Write a program that remove all vowels from the input word and generate a brief version of it

# vowels = "aeiouAEIOU"
# test_string = "International"
# brief_version = ''.join([char for char in test_string if char not in vowels])

# print("Brief version of the word:", brief_version)


#### Write a program that prints the locations of "i" character in any string you added.
# test_string = "international"

# for idx, element in enumerate(test_string):
#     if(element == 'i'):
#         print(idx)


#### Write a program that generate a multiplication table from 1 to the number passed

# num = int(input("Enter the number to generate the multiplication table:"))
# outer_arr = []
# for i in range(1, num+1):
#     j = i
#     inner_arr = []
#     while(len(inner_arr) < i ):
#         inner_arr.append(j)
#         j = j+i
#     outer_arr.append(inner_arr)

# print(outer_arr)


####  Write a program that build a Mario pyramid

num = int(input("Enter the length of the pyramid: "))

for i in range(1, num+1):
    row = ""
    row += " " * (num-i)
    row += "*" * i 
    
    print(row)

