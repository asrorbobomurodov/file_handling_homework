def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    numbers = []
    for i in data:
        if i.isdigit():
            numbers.append(i)
    return max(numbers)

# Read data from file
file = open('data/data08.txt')
f = file.read()
print(main(f))