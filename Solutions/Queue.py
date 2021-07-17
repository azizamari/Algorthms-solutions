from LinkedList import *
class Queue:
    def __init__(self):
        self.linkedList = LinkedList()
    def peek(self):
        return self.linkedList.head.value
    def enqueue(self, value):
        return self.linkedList.add(value)
    def dequeue(self):
        oldHead=self.linkedList.head
        if self.linkedList.head!=None:
            self.linkedList.head=self.linkedList.head.next
        return oldHead
q=Queue()
print(q.dequeue())
print(q.enqueue(156))
print(q.enqueue(12))
print(q.enqueue(14))
print(q.linkedList)
print(q.dequeue())
print(q.linkedList)