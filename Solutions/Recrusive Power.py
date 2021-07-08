def pow(n,p):
    assert int(p)==p and n>=0 , 'Only accepts positive integers as exponents'
    if p==0:
        return 1
    return pow(n,p-1)*n


print(pow(2,15)) #32768
print(pow(5,3)) #125