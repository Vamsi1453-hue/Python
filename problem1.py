n = input("enter the sentence: ")
words = n.split()
palindromes = [word for word in words if word == word[::-1]]
print(" ".join(palindromes))
