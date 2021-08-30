import math
l=input().split(" ")
l=[int(n) for n in l]

# sort
n=len(l)
numberOfBuckets=round(math.sqrt(n))
maxVal=max(l)
arr=[]
res=[]
for i in range(numberOfBuckets):
    arr.append([])
for j in l:
    bucket=math.ceil(j*numberOfBuckets/maxVal)
    arr[bucket-1].append(j)
for x in arr:
    x.sort()
    res+=x
print(res)