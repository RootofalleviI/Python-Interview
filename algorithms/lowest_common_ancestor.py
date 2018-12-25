def lca(node_0, node_1):
    """ Given two nodes in a binary tree, design an algorithm that computes their LCA.
    Assume that each node has a parent pointer. """

    def get_depth(node):
        """ Compute a node's depth, i.e., the distance from it to root. """
        depth = 0
        while node:
            depth += 1
            node = node.parent
        return depth

    depth_0, depth_1 = get_depth(node_0), get_depth(node_1)

    # Makes node_0 the deeper node to simplify the code
    if depth_1 > depth_0:
        node_0, node_1 = node_1, node_0

    # Ascends from the deeper node
    depth_diff = abs(depth_0 - depth_1)
    while depth_diff:
        node_0 = node_0.parent
        depth_diff -= 1

    # Now ascends both nodes until we reach the LCA
    while node_0 is not node_1:
        node_0, node_1 = node_0.parent, node_1.parent

    return node_0
