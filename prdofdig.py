def product_of_digits(num):
    hundreds=num//100
    tens=(num//10)%10
    ones=num%10
    return hundreds*tens*ones
print(product_of_digits(321))
print(product_of_digits(212))
