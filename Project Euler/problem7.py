# 10001st prime

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def isPrime(n):
    i=2
    while i<=n**0.5:
        if n%i==0:
            return False
        i+=1
    return True
count=0
i=1
while count <10001:
    i+=1
    if isPrime(i):count+=1

print(i)