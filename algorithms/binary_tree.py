"""
# Binary Tree
Formally, a binary tree is either empty, or a root node r together with a left binary tree and a
right binary tree. The subtrees themselves are binary trees. Binary trees most commonly occur in 
the context of BST, wherein keys are sorted in a sorted fashion.

# Terminology
- A full binary tree is a binary tree in which every node other than the leaves has two children.
- A perfect binary tree is a full binary tree in which all leaves are at the same depth, and in 
  which every parent has two children.
  - A prefect binary tree of height h has exactly 2^{h+1}-1 nodes, of which 2^h are leaves.
- A complete binary tree is a binary tree in which every level, except possibly the last, is
  completely filled, and all nodes are as far left as possible.
  - A complete binary tree on n nodes has height math.floor(log n).

# Traversing
- In-order: left subtree -> root -> right subtree
- Pre-order: root -> left subtree -> right subtree
- Post-order: left subtree -> right subtree -> root

# Time and space complexity
- Let T be a binary tree of n nodes with height h.
- Implemented recursively, these traversals have O(n) time complexity and O(h) additional space 
  complexity.
"""

class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


