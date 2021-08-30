l=input().split(" ")
l=[int(n) for n in l]

# sort
n=len(l)
for i in range(n-1):
    for j in range(n-1):
        if l[j]>l[j+1]:
            l[j+1],l[j]=l[j],l[j+1]
print(l)