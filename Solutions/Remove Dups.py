from LinkedList import *

n=LinkedList()
print(n.populateRandom(30,1,20))
curr=n.head
prev=None
nums=set()
while curr:
    if curr.value in nums:
        if curr.next==None:
            prev.next=None
            curr=None
            n.tail=prev
        else:
            prev.next=curr.next
            curr.next.prev=prev
            curr=curr.next    
    else:
        nums.add(curr.value)
        prev=curr
        curr=curr.next
print(n)