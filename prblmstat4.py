def compress_string(s: str) -> str:
    compressed = []
    count = 1
    
    for i in range(1, len(s) + 1):
        if i < len(s) and s[i] == s[i - 1]:
            count += 1
        else:
            compressed.append(s[i - 1] + (str(count) if count > 1 else ""))
            count = 1
    
    result = "".join(compressed)
    return result if len(result) < len(s) else s

print(compress_string("aaabbbcccc"))  
print(compress_string("abcd"))        
