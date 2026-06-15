def reverse_number(num):
    hundreds = num // 100
    tens = (num // 10) % 10
    ones = num % 10
    return ones * 100 + tens * 10 + hundreds
print(reverse_number(123)) 
