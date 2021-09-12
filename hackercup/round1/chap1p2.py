from itertools import combinations
f=open("D:\\aziz\\academic\\Algorthmic Interviews Sheet\\hackercup\\round1\\weak_typing_chapter_2_validation_input.txt",'r')
content=f.readlines()
content=[s.strip() for s in content]
f.close()
t=int(content[0])
content.pop(0)
w=[]
for i in range(t):
    content.pop(0)
    w.append(content[0])
    content.pop(0)


def allSubStrings(Str):
    n=len(Str)
    total=0
    for Len in range(1,n + 1):
        for i in range(n - Len + 1):
            j = i + Len - 1
            r=''
            for k in range(i,j + 1):
                r+=Str[k]
            # do
            count=len(generateNewString(r.replace('F','')))-1
            if count<0:count=0
            total+=count
    return total
             
def generateNewString(s):
    if len(s)<=0:return ''
    n=s[0]
    prev=s[0]
    for i in s:
        if i!=prev:
            n+=i
            prev=i
    return n
memo={}
for j in range(len(w)):
    c=w[j]
    total=0
    out=open('output2.txt','a')
    total= allSubStrings(c)

    out.write("Case #"+str(j+1)+": "+str(total%1000000007)+"\n")


# if ll in memo:
#     total+=memo[ll]
# else:
#     count=0
#     if ll!='':
#         d=ll[0]
#         for f in ll:
#             if f!=d:
#                 count+=1
#                 d=f
#     memo[ll]=count
#     total+=count