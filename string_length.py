str = input("Enter string: ")

def str_len(str):
    if str == "":
        return 0
    else:
        return 1 + str_len(str[1:])

print(str_len(str))