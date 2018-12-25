def binary_tree_from_preorder_inorder(preorder, inorder):
    """ Given traversal data from preorder and inorder traversals, reconstruct the binary tree.

    The preorder seq gives us the key of the root node, which allows us to split the inorder seq
    into an inorder seq for the left subtree, followed by the root, followed by the right subtree.
    """

    node_to_inorder_idx = {data: i for i, data in enumerate(inorder)}

    def binary_tree_from_preorder_inorder_helper(preorder_start, preorder_end, inorder_start, inorder_end):
        if preorder_end <= preorder start or inorder_end <= inorder_start:
            return None

        root_inorder_idx = node_to_inorder_idx[preorder[preorder_start]]
        left_subtree_size = root_inorder_idx - inorder_start
        return BinaryTreeNode(
                preorder[preorder_start],
                binary_tree_from_preorder_inorder_helper(
                    preorder_start + 1, preorder_start + 1 + left_subtree_size,
                    inorder_start, root_inorder_idx),

                binary_tree_from_preorder_inorder_helper(
                    preorder_start + 1 + left_subtree_size, preorder_end,
                    root_inorder_idx + 1, inorder_end))

    return binary_tree_from_preorder_inorder_helper(0, len(preorder), 0, len(inorder))
