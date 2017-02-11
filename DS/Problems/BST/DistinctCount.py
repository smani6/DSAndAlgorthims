from DS.BinarySearchTree import BinarySearchTree
from DS.TreeNode import TreeNode
from DS.TreeTraversal import TreeTraversal

def binary_root(node):
    return [node.getRootValue()]

def preorder_list(tree):
    if not tree:
        return []
    return [binary_root(tree) + preorder_list(tree.getLeftChild()) + preorder_list(tree.getRightChild())]

if __name__ == "__main__":

    no_of_test_cases = int(raw_input())
    for i in xrange(no_of_test_cases):
        n, x = map(int,raw_input().split(' '))
        array_elements = map(int,raw_input().split(' '))
        bst = BinarySearchTree()
        for ele in array_elements:
            bst[ele] = ele

        #print preorder_list(bst.root)
        dis_vals = preorder_list(bst.root)
        # dis_vals = []
        # dis_vals.append(TreeTraversal().preorder(bst.root))
        print dis_vals


        if len(dis_vals) == x:
            print "Good"
        elif len(dis_vals) < x:
            print "Bad"
        else:
            print "Average"