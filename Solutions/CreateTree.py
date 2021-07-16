class TreeNode:
    def __init__(self,value,children=[]):
        self.value=value
        self.children=children
    def __str__(self,level=0):
        ret="  "*level+"-"+str(self.value)+"\n"
        for child in self.children:
            ret+=child.__str__(level+1)
        return ret
    def addChild(self,child):
        self.children.append(child)

tree=TreeNode('God',[])
angels=TreeNode('angels',[])
demons=TreeNode('demons',[])
beelzbub=TreeNode('beelzbub',[])
lucifer=TreeNode('lucifer',[])
aziz=TreeNode('aziz',[])
angels.addChild(aziz)
demons.addChild(lucifer)
demons.addChild(beelzbub)
tree.addChild(angels)
tree.addChild(demons)
print(tree)
