scores=[85,90,78,92,88]
# method 1
for i in range(len(scores)):
    print(f"scores[{i}]={scores[i]}")
# method 2
for score in scores: print(score)
# method 3 enumerate(index+value)
for idx, val in enumerate(scores):
    print(f"Index {idx} -> {val}")
# method 4 list comprehension
doubled=[x*2 for x in scores]
print(doubled)