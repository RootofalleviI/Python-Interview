def is_symmetric(tree):
    """ A binary tree is symmetri if you can draw a vertical line through the root and then the 
    left subtree is the mirror image of the right subtree. Write a program that checks whether
    a binary tree is symmetric.

    Computing the mirror image of a tree is as simple as swapping the left and right subtrees,
    and recursively continuing. Time O(n) where n is the number of nodes in the tree; space
    O(h) where h is the height of the tree.
    """

    def check_symmetric(subtree_0, subtree_1):
        if not subtree_0 and not subtree_1:
            return True
        elif subtree_0 and subtree_1:
            return (subtree_0.data == subtree_1.data
                    and check_symmetric(subtree_0.left, subtree_1.right)
                    and check_symmetric(subtree_0.right, subtree_1.left))

        return False

    return not tree or check_symmetric(tree.left, tree.right)
