class SLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
class Node:
    def __init__(self, value=None):
        self.value=value
        self.next=None

sList=SLinkedList()
no1=Node(15)
no2=Node(69)

no1.next=no2
sList.head=no1
sList.tail=sList.head.next
