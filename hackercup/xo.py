f=open('xs_and_os_input.txt','r')
content=[s.strip() for s in f.readlines()]
f.close()
content.reverse()
t=int(content[-1])
content.pop()
for i in range(t):
    n=int(content[-1])
    content.pop()
    board=''
    solutions=[]
    conflict=set()
    for j in range(n):
        line=content[-1]
        content.pop()
        board+=line
        cempty=line.count('.')
        if 'O' not in line and cempty!=0:
            if(cempty==1):
                conflict.add(str(j)+","+str(line.index(".")))
            solutions.append(cempty)
    for x in range(n):
        col=''
        for y in range(n):
            col+=board[x+n*y]
        cempty=col.count('.')
        if 'O' not in col and cempty!=0:
            if(cempty==1 and (str(col.index("."))+","+str(x)) in conflict):
                continue
            else:
                solutions.append(cempty)
    result=''
    if (len(solutions)==0):
        result="Impossible"
    else:
        minM=min(solutions)
        c=solutions.count(minM)
        result=str(minM)+" "+str(c)
    with open('output2.txt','a') as f2:
        f2.write("Case #"+str(i+1)+": "+result+"\n")
        print("Case #"+str(i+1)+": "+result)