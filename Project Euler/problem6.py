# Sum square difference

# https://projecteuler.net/problem=6

# square of sum of the first 100 natural nums
# sum method (n*(n+1))/2

sqs=(100*101)//2
sqs=sqs**2

# sum of squres of the first 100 natural nums
# sum of squares method (n*(n+1)*(2n+1))/6

ssq=(100*101*201)/6
print(sqs-ssq)