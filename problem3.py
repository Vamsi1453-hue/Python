n = input("enter the sentence: ")
target = input("enter the target word: ")
words = n.split()
result = [("*" * len(word)) if word == target else word for word in words]
print(" ".join(result))
