def main(data:str):
    """
    The data is from the file. Return data as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    l = data.split(",")
    s = []
    i = 0
    while len(l)>i:
        convert = int(l[i])
        s.append(convert)
        i += 1 
    return s
    
# Read data from file
f = open('data/data01.txt').read()
print(main(f))