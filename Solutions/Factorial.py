def fact(n):
    if n in [0,1]: return n
    return n*fact(n-1)
print(fact(5))