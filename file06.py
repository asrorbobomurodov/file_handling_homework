def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    rows = data.split('\n')
    count = []
    for row in rows:
        len_row = len(row)
        count.append(len_row)
    return count

# Read data from file
file = open('data/data06.txt')
f = file.read()
print(main(f))