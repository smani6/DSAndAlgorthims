from DS.BinarySearchTree import BinarySearchTree
from DS.TreeTraversal import TreeTraversal

def node_height(node):
    if node is None:
        return 0
    else:
        return 1 + max(node_height(node.leftChild), node_height(node.rightChild))

def height(bst):
    return node_height(bst.root)


if __name__ == "__main__":
    no_of_elements = int(raw_input())
    input_array = raw_input().split(' ')
    print input_array
    array_elements = map(int, input_array)

    binary_tree = BinarySearchTree()
    for ele in array_elements:
        binary_tree[ele] = ele

    print TreeTraversal().preorder(binary_tree.root)
    print TreeTraversal().postorder(binary_tree.root)
    print TreeTraversal().inorder(binary_tree.root)
    height = height(binary_tree)

    print height