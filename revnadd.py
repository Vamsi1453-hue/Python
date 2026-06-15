num = int(input())
hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10
reversed_num = ones * 100 + tens * 10 + hundreds
print("Palindrome" if num == reversed_num else "Not Palindrome")
