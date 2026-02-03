def fizz_buzz (num: int) -> str:
    answer = ""
    if(num % 3 == 0):
        answer += "Fizz"
    if(num % 5 == 0):
        answer += "Buzz"

    return answer



if __name__ == "__main__":
    print(fizz_buzz(3))
    print(fizz_buzz(5))
    print(fizz_buzz(15))