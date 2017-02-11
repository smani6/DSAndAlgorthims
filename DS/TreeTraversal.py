class TreeTraversal(object):

    def __init__(self):
        pass

    def preorder(self,tree):

        if tree:
            print tree.getRootValue()
            self.preorder(tree.getLeftChild())
            self.preorder(tree.getRightChild())

    def preorder_list(self,tree):
        if not tree:
            return []

        return [self.preorder_list[tree.getRootValue()] + self.preorder_list[tree.getLeftChild()] + self.preoder_list(tree.getRightChild())]


    def postorder(self,tree):

        if tree:
            self.postorder(tree.getLeftChild())
            self.postorder(tree.getRightChild())
            print tree.getRootValue()

    def inorder(self,tree):

        if tree:
            self.inorder(tree.getLeftChild())
            print tree.getRootValue()
            self.inorder(tree.getRightChild())