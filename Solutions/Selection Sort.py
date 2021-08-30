l=input().split(" ")
l=[int(n) for n in l]

# sort
n=len(l)
for i in range(n):
    smallest=i
    for j in range(i+1,n):
        if l[j]<l[smallest]:
            smallest=j
    l[i],l[smallest]=l[smallest],l[i]
print(l)