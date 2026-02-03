def longest_alpha_order(string: str) ->str:

    if(not string or not (string.isalpha())):
        return ""
    string = string.lower()
    longest = string[0]
    current  = longest
    for i in range(1,len(string)):
        if(string[i] >= string[i-1]):
            current += string[i]
        else:
            if(len(current) > len(longest)):
                longest = current
            current = string[i]


    return longest


if __name__ == "__main__":
    print(longest_alpha_order("abdulrahman"))
    print(longest_alpha_order("ibrahim"))
    print(longest_alpha_order("IbRahim"))
    print(longest_alpha_order("ibrahim1"))

            
