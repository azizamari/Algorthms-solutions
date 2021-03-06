class BinaryTree:
    def __init__(self, size):
        self.customList=size*[None]
        self.lastUsedIndex=0
        self.size=size
    def insertNode(self, value):
        if self.lastUsedIndex+1==self.size:
            return False
        self.lastUsedIndex+=1
        self.customList[self.lastUsedIndex]=value
        return True
    def searchNode(self, value):
        return value in self.customList
    def preOrder(self,index=1):
        if index>self.lastUsedIndex:
            return
        print(self.customList[index],end='')
        self.preOrder(index*2)
        self.preOrder(index*2+1)
    def inOrder(self,index=1):
        if index>self.lastUsedIndex:
            return
        self.inOrder(index*2)
        print(self.customList[index],end='')
        self.inOrder(index*2+1)
    def postOrder(self,index=1):
        if index>self.lastUsedIndex:
            return
        self.inOrder(index*2)
        self.inOrder(index*2+1)
        print(self.customList[index],end='')
    def levelOrder(self):
        for i in range(1,self.lastUsedIndex+1):
            print(self.customList[i],end='')

newBT=BinaryTree(8)
newBT.insertNode("aziz")
newBT.insertNode("left")
newBT.insertNode("right")
print(newBT.searchNode("left"))
newBT.preOrder()
print()
newBT.inOrder()
print()
newBT.postOrder()
print()
newBT.levelOrder()