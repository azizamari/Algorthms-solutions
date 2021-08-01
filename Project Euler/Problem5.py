# Smallest multiple

# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def divByAll20(n):
    r=True
    i=1
    while r and i<=20:
        if n%i!=0:r=False
        i+=1
    return r
num=2520
while not divByAll20(num):
    num+=1
print(num)