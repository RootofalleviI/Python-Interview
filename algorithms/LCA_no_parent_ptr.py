def lca(tree, node0, node1):
    """ Design an algorithm for computing the LCA of two nodes in a binary tree in which nodes do not
    have a parent field. 

    Time O(n), Space O(h)
    """

    Status = collections.namedtuple('Status', ('num_target_nodes', 'ancestor'))

    # Returns an object consisting of an int and a node.
    # The int field is 0, 1, 2 depending on how many of {node0, node1} are present in the tree.
    # If both present and ancestor is non-null, it is the LCA

    def lca_helper(tree, node0, node1):
        if not tree:
            return Status(0, None)

        left_result = lca_helper(tree.left, node0, node1)
        if left_result.num_target_nodes == 2:
            return left_result

        right_result = lca_helper(tree.right, node0, node1)
        if right_result.num_target_nodes == 2:
            return right_result

        num_target_nodes = (
                left_result.num_target_nodes + right_result.num_target_nodes + 
                int(tree is node0) + int(tree is node1))

        return Status(num_target_nodes, tree if num_target_nodes == 2 else None)

    return lca_helepr(tree, node0, node1).ancestor
