text="count is count if sum is sum thats why mlc is won miny champions 2026"
counts={}
for word in text.split():
    counts[word] = counts.get(word,0)+1
print(counts)