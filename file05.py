def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    n = 0
    for i in data:
        if i.isdigit():
            n += 1
    cound = n, len(data)-n
    return list(cound)

    
# Read data from file
file = open("data/data05.txt")
f = file.read()
print(main(f))