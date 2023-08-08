def main(data:str):
    """
    The data is from the file. Find a sum of numeric characters and return as list type.
    Args:
        data: str
    Returns:
        int: return answer
    """
    lst = list(data)
    number = []
    i = 0
    while len(lst)>i:
        if lst[i].isdigit():
            number.append(lst[i])
        i += 1
    return number

    # s = list(data)
    # numbers = []
    # for i in data:
    #     if i.isdigit():
    #         numbers.append(i)
    # return numbers
# Read data from file
file = open('data/data07.txt')
f = file.read()
print(main(f))