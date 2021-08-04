class BinaryTree:
    def __init__(self, size):
        self.customList=size*[None]
        self.lastUseIndex=0
        self.size=size
    def insertNode(self, value):
        if self.lastUseIndex+1==self.size:
            return False
        self.lastUseIndex+=1
        self.customList[self.lastUseIndex]=value
        return True
    def searchNode(self, value):
        return value in self.customList

newBT=BinaryTree(8)
newBT.insertNode("aziz")
newBT.insertNode("left")
newBT.insertNode("right")
print(newBT.searchNode("left"))