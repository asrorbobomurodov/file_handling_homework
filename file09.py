def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    numbers = []

    for i in data:
        if i.isdigit():
            numbers.append(i)
    
    minimum = numbers[0]
    for i in range(len(numbers)):
        if minimum > numbers[i]:
            minimum = numbers[i]

    return minimum
# Read data from file
file = open('data\data09.txt')
f = file.read()
print(main(f))