from TreeNode import TreeNode
class BinarySearchTree(object):

    def __init__(self):
        self.size = 0
        self.root = None

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self,key,val):
        if self.root:
            self._put(key,val,self.root)
        else:
            self.root = TreeNode(key,val)

        self.size = self.size + 1

    def _put(self,key,value,currentNode):

        if key < currentNode.key:
            if currentNode.hasLeftChild():
                self._put(key,value,currentNode.leftChild)
            else:
                currentNode.leftChild = TreeNode(key,value,parent=currentNode)
        else:
            if currentNode.hasRightChild():
                self._put(key,value,currentNode.rightChild)
            else:
                currentNode.rightChild = TreeNode(key,value,parent=currentNode)

    def __setitem__(self, key, value):
        self.put(key,value)

    def get(self,key):
        if self.root:
            res = self._get(key,self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, currentNode):

        if not currentNode:
            return None
        if currentNode.key == key:
            return currentNode
        if key < currentNode.key:
            return self._get(key,currentNode.leftChild)
        else:
            return self._get(key,currentNode.rightChild)

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        if self._get(key,self.root):
            return True
        else:
            return False

    def delete(self,key):
        if self.size > 1:
            nodeToRemove = self._get(key,self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size - 1
            else:
                raise KeyError("key not in tree")

        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1

        else:
            raise KeyError("key not in tree")

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            succ = self.rightChild.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    succ = self.parent
                else:
                    self.parent.rightChild = None
                    succ = self.parent.findSuccessor()
                    self.parent.rightChild = self

        return succ

    def findMin(self):

        current = self
        while current.hasLeftChild():
            current = current.leftChild

        return current

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None

        elif self.hasAnyChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.leftChild = self.leftChild
                else:
                    self.parent.rightChild = self.leftChild
                self.leftChild.parent = self.parent

            else:
                if self.isLeftChild():
                    self.parent.leftChild = self.rightChild
                else:
                    self.parent.rightChild = self.rightChild
                self.rightChild.parent = self.parent



    def remove(self,currentNode):

        if currentNode.isLeaf():
            if currentNode == currentNode.parent.leftChild:
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None

        elif currentNode.hasBothChildren():
            succ = currentNode.findSuccessor()
            succ.spliceOut()
            currentNode.payload = succ.payload
            currentNode.key = succ.key

        else:
            if currentNode.hasLeftChild():
                if currentNode.isLeftChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.leftChild
                elif currentNode.isRightChild():
                    currentNode.leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.leftChild
                else:
                    currentNode.replaceNodeData(currentNode.leftChild.key,currentNode.leftChild.payload,
                                                currentNode.leftChild.leftChild,currentNode.leftChild.rightChild)
            else:
                if currentNode.isLeftChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = currentNode.rightChild
                elif currentNode.isRightChild():
                    currentNode.rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = currentNode.righChild
                else:
                    currentNode.replaceNodeData(currentNode.rightChild.key, currentNode.rightChild.payload,
                                                currentNode.rightChild.leftChild, currentNode.rightChild.rightChild)


if __name__ == "__main__":

    mytree = BinarySearchTree()
    mytree[3] = 'red'
    mytree[4] = 'blue'
    mytree[5] = 'yellow'
    mytree[6] = 'meuroon'
    mytree[1] = 'orange'
    mytree[2] = 'rose'

    print mytree[6]
    print mytree[2]



















