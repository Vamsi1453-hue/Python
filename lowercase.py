#print lower case(z-a) using no loops
def lowercase(ch = 120):
    if ch < 97:
        return
    print(chr(ch))
    lowercase(ch-1)
    
lowercase()