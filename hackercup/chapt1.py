t=0
sList=[]
# for i in range(t):
#     sList.append(input())
with open('consistency_chapter_1_input.txt','r') as f:
    content=f.readlines()
    t=int(content[0])
    sList=content[1:]
    sList=[s.strip() for s in sList]

for index,s in enumerate(sList):
    voc=0
    coc=0
    vowels=0
    consants=0
    for c in s:
        if c in ["A", "E", "I", "O", "U"]:
            vowels+=1
            voc=max(voc, s.count(c))
        else:
            consants+=1
            coc=max(coc, s.count(c))
    seconds=min((vowels-voc)*2+consants,(consants-coc)*2+vowels)
    print("Case #"+str(index+1)+": "+str(seconds))
    with open('output.txt','a') as f:
        f.write("Case #"+str(index+1)+": "+str(seconds)+"\n")