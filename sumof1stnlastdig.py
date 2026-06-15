def sum_of_1st_and_last_digit(num):
    hundreds=num//100
    tens=(num//10)%10
    ones=num%10
    return hundreds+ones
print(sum_of_1st_and_last_digit(231))
print(sum_of_1st_and_last_digit(312))