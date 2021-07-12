import random

class Node:
    def __init__(self,value=None):
        self.value = value
        self.next=None
        self.prev=None
    def __str__(self):
        return str(self.value)
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def __iter__(self):
        curr=self.head
        while curr:
            yield curr
            curr=curr.next
    def __str__(self):
        values=[]
        for item in self:
            values.append(str(item))
        return ' -> '.join(values)
    def __len__(self):
        len=0
        for i in self:
            len+=1
        return len
    def add(self,value):
        if self.head==None:
            newNode=Node(value)
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=Node(value)
            self.tail=self.tail.next
        return self.tail
    def poulateRandom(self,n,min,max):
        self.head=None
        self.tail=None
        for i in range(n):
            self.add(random.randint(min,max))
        return self