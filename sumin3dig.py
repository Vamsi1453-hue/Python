def sum_of_digits(num):
    hundreds = num // 100
    tens = (num // 10) % 10
    ones = num % 10
    return hundreds + tens + ones
print(sum_of_digits(572))  
print(sum_of_digits(123))  
