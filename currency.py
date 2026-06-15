def calculate_notes(a):
    n500, a = divmod(a, 500)
    n200, a = divmod(a, 200)
    n100, a = divmod(a, 100)
    n50,  a = divmod(a, 50)
    n20,  a = divmod(a, 20)
    n10,  a = divmod(a, 10)
    n5,   a = divmod(a, 5)
    n2,   a = divmod(a, 2)
    return n500, n200, n100, n50, n20, n10, n5, n2, a
print(calculate_notes)