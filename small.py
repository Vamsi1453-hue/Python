num = int(input())
hundreds = num // 100
tens = (num // 10) % 10
ones = num % 10
print(min(hundreds, tens, ones))
