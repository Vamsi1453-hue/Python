num = int(input())
hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10
average = (hundreds + tens + ones) / 3
print(int(average) if average.is_integer() else average)
