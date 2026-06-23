#print upper case(Z-A) using no loops
def uppercase(ch=90):
    if ch < 65:
        return
    print(chr(ch))
    uppercase(ch-1)

uppercase()
