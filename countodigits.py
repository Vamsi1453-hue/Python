#n=123 , count=1+2+3=6
def count_digits_sum(n):
    if n == 0:
        return 0
    return n % 10 + count_digits_sum(n // 10)
n = 123


print(count_digits_sum(n))