#print lower case(a-z) using no loops
def lowercase(ch=97):
    if ch > 122:
        return
    print(chr(ch))
    lowercase(ch+1)

lowercase()
