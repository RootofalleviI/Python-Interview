def lca(node_0, node_1):
    """ Given two nodes, compute their lowest common ancestor.

    Time(D0+D1) space and time, where D0 is the distance from the LCA to the first
    node and D1 is the distance from LCA to the second node.
    """

    iter_0, iter_1 = node_0, node_1
    nodes_on_path_to_root = set()
    while iter_0 or iter_1:
        if iter_0:
            if iter_0 in nodes_on_path_to_root:
                return iter_0
            nodes_on_path_to_root.add(iter_0)
            iter_0 = iter_0.parent
        if iter_1:
            if iter_1 in nodes_on_path_to_root:
                return iter_1
            nodes_on_path_to_root.add(iter_1)
            iter_1 = iter_1.parent
    raise ValueError('node_0 and node_1 are not in the same tree')
        
