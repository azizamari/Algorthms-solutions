from LinkedList import *

llist=LinkedList()
print(llist.populateRandom(10,1,20))
n=int(input('give me number'))
if n>len(llist):
    print('number is too big')
else:
    i=0
    currNode=llist.head
    kth=None
    while currNode:
        if i>n: kth=kth.next
        elif i==n:kth=llist.head
        currNode=currNode.next
        i+=1
    print(kth)
