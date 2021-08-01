# Largest palindrome product

# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def isPal(n):
    rev=0
    aux=n
    while aux!=0:
        rev=rev*10+aux%10
        aux=aux//10
    return rev==n
max=0
for i in range(999):
    for j in range(999):
        prod=i*j
        if prod>max and isPal(prod):
            max=prod
print(max)