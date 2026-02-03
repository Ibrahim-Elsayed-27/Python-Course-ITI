def range_arr(length: int, start: int) -> list:
    range_list = []
    i = start + 1
    while i < start + length + 1:
        range_list.append(i)
        i = i+1
    
    return range_list

if __name__ == "__main__":
    print(range_arr(5,5))