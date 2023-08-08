def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    s = list(data.strip(""))
    l = len(s)
    ss = []
    for i in range(0,l):
        # if i==len(s):
        #     break
        if s[i].isdigit():
            continue
        ss.append(s[i])
    return ss
# Read data from file
f = open('data\data04.txt').read()
print(main(f))