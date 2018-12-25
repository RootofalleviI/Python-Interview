def is_balanced_binary_tree(tree):
    """ Given as input the root of a binary tree, determine whther the tree is height-balanced.

    A binary tree is height balanced if for each node in the tre, the difference in the height
    of its left and right subtrees is at most one.

    The program implements a post-order traversal with early termination. The function call 
    stack corresponds to a sequence of calls from the root through the unique path to the current
    node, and the stack height is therefore bounded by the height of the tree, leading to an 
    O(h) space bound. The time complexity is the same as that for a post-order traversal, namely O(n).
    """

    BalancedStatusWithHeight = collections.namedtuple(
            'BalancedStatusWithHeight', ('balanced', 'height'))

    def check_balanced(tree):
        """ First value returned indicates if tree is balanced; if it is, the second value of 
        the return value is the height of tree."""
        if not tree:
            return BalancedStatusWithHeight(True, -1) # base case

        left_result = check_balanced(tree.left)
        if not left_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        right_result = check_balanced(tree.right)
        if not right_result.balanced:
            return BalancedStatusWithHeight(False, 0)

        is_balanced = abs(left_result.height - right_result.height) <= 1
        height = max(left_result.height, right_result.height) + 1
        return BalancedStatusWithheight(is_balanced, height)

    return check_balanced(tree).balanced
