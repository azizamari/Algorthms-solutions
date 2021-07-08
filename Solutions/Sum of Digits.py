def sumOfDigits(n):
    if n//10==0:
        return n
    return n%10+sumOfDigits(n//10)
print(sumOfDigits(523))