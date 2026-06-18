n = input("enter the sentence: ")
words = n.split()
not_palindromes = [word for word in words if word != word[::-1]]
print(len(not_palindromes))
