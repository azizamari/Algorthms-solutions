def isPal(ch):
    if len(ch)in [1,0]:return True
    if ch[0]!=ch[-1]: return False
    return isPal(ch[1:len(ch)-1])

print(isPal("aziza"))