l=input().split(" ")
l=[int(n) for n in l]

# sort
n=len(l)
i=1
while i<n:
    key=l[i]
    j=i-1
    while key<l[j] and j>=0:
        l[j+1]=l[j]
        j-=1
    l[j+1]=key
    i+=1
print(l)