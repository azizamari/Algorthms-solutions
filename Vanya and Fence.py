l1=input().split()
n=int(l1[0])
h=int(l1[1])
he=input().split()
m=0
for i in he:
    m+=1
    if int(i)>h:
        m+=1
print(m)