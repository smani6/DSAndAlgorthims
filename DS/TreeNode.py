class TreeNode(object):

    def __init__(self,key=None,payload=None,left=None,right=None,parent=None):

        self.key = key
        self.payload=payload
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def getRootValue(self):
        return self.payload

    def getLeftChild(self):
        return self.leftChild

    def getRightChild(self):
        return self.rightChild

    def hasLeftChild(self):
        return self.leftChild

    def hasRightChild(self):
        return self.rightChild

    def isLeftChild(self):
        return self.parent and self.parent.leftChild == self

    def isRightChild(self):
        return self.parent and self.parent.rightChild == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.leftChild or self.rightChild)

    def hasAnyChildren(self):
        return self.leftChild or self.rightChild

    def hasBothChildren(self):
        return self.leftChild and self.rightChild

    def replaceNodeData(self,key,value,lc,rc):
        self.key = key
        self.payload = value
        self.leftChild = lc
        self.rightChild = rc
        if self.hasLeftChild():
            self.leftChild.parent = self
        if self.hasRightChild():
            self.rightChild.parent = self


    def preorder(self):
        print self.key
        if self.leftChild:
            self.leftChild.preorder()
        if self.rightChild:
            self.rightChild.preorder()

    def postorder(self):

        if self.leftChild:
            self.leftChild.postorder()
        if self.rightChild:
            self.rightChild.postorder()
        print self.key

    def inorder(self):

        if self.leftChild:
            self.leftChild.inorder()
        print self.key
        if self.rightChild:
            print self.rightChild.inorder()


