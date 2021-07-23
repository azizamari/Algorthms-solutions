from LinkedList import *
class Queue:
    def __init__(self):
        self.linkedList = LinkedList()
        self.len=len(self.linkedList)
    def peek(self):
        return self.linkedList.head.value
    def enqueue(self, value):
        self.len+=1
        return self.linkedList.add(value)
    def dequeue(self):
        oldHead=self.linkedList.head
        if self.linkedList.head!=None:
            self.len-=1
            self.linkedList.head=self.linkedList.head.next
        return oldHead
    def isEmpty(self):
        return self.len==0
# q=Queue()
# print(q.isEmpty())
# print(q.dequeue())
# print(q.isEmpty())
# print(q.enqueue(156))
# print(q.enqueue(12))
# print(q.enqueue(14))
# print(q.linkedList)
# print(q.dequeue())
# print(q.linkedList)