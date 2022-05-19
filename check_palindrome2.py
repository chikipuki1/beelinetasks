num = int(input("Enter the number: "))

def check_palindrome(num):
    temp = str(num)
    reverse = str(num)
    reverse = reverse[::-1]
    return str(num) == reverse

print(check_palindrome(num))