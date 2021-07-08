def d2b(n):
    if n//2==0: return str(n%2)
    return d2b(n//2) + str(n%2)

print(d2b(3))