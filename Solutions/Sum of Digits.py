def sumOfDigits(n):
    assert int(n)==n and n>=0, 'This needs to be an integer'
    if n==0:
        return 0
    return n%10+sumOfDigits(n//10)
    
print(sumOfDigits(153)) #=9
print(sumOfDigits(523)) #=10
print(sumOfDigits(111115)) #10
print(sumOfDigits(-1)) #Assertion error
print(sumOfDigits(18.5)) #Assertion error