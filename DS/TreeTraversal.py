class TreeTraversal(object):

    def __init__(self):
        pass

    def preorder(self,tree):

        if tree:
            print tree.getRootValue()
            self.preorder(tree.getLeftChild())
            self.preorder(tree.getRightChild())


    def postorder(self,tree):

        if tree:
            self.postorder(tree.getLeftChild())
            self.postorder(tree.getRightChild())
            print tree.getRootValue()

    def inorder(self,tree):

        if tree:
            self.inorder(self.getLeftChild())
            print tree.getRootValue()
            self.inorder(self.getRightChild())