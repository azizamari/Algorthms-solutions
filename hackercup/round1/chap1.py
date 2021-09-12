f=open('weak_typing_chapter_1_input.txt','r')
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
for j in range(len(w)):
    curr=w[j]
    curr=curr.replace('F','')
    count=0
    out=open('output.txt','a')
    if curr!='':
        d=curr[0]
        for f in curr:
            if f!=d:
                count+=1
                d=f
    out.write("Case #"+str(j+1)+": "+str(count)+"\n")