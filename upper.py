#print upper case(A-Z) using no loops
def uppercase(ch=65):
    if ch > 90:
        return
    print(chr(ch))
    uppercase(ch+1)

uppercase()
