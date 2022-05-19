num = int(input("Enter the number: "))

def check_palindrome(num: int) -> bool:
   temp = num
   reverse = 0
   while num > 0:
      reverse *= 10
      reverse += num % 10
      num //= 10
   return temp == reverse

print(check_palindrome(num))