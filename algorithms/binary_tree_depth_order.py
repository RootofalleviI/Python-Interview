def binary_tree_depth_order(tree):
    """ Given a binary tree, return an array consisting of the keys at the same level.
    Keys should appear in the order of the corresponding nodes' dpeths, breaking ties
    from left ro right.

    We use a queue of nodes to store nodes at depth i and a queue of nodes at depth i+1.
    All all nodes at depth i are processed, we are done with that queue, and can start
    processing the queue with nodes at depth i+1, putting the depth i+2 nodes in the 
    new queue.

    Time: O(n).
    Space: O(m), where m is the max number of nodes at any single depth.
    """
    result = []
    if not tree:
        return result
    
    curr_depth_nodes = [tree]
    while curr_depth_nodes:
        result.append([curr.data for curr in curr_depth_nodes])
        curr_depth_nodes = [
                child
                for curr in curr_depth_nodes for child in (curr.left, curr.right)
                if child
        ]
    return result
