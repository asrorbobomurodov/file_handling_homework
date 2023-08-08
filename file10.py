def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    s = data.split("\n")
    max = len(s[0])
    i = 1
    while len(s)>i:
        if len(s[i])>max:
            max = len(s[i])
        i += 1
    return max

# Read data from file
file = open("data/data10.txt")
f = file.read()
print(main(f))