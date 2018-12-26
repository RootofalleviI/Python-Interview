class BSTNode:
    def __init__(self, data=None, left=None, right=None):
        self.data, self.left, self.right = data, left, right


def search_bst(tree, key):
    if tree.data == key:
        return tree
    elif tree.data < key:
        search_bst(tree.right, key)
    elif tree.data > key:
        search_bst(tree.left, key)
    else:
        return None


# bintrees module
# - insert(e): inserts new element e in the BST
# - discard(e): removes e from the BST if present
# - min_item()/max_item(): yields the smallest and largest key-value pair in the BST
# - min_key()/max_key(): yields the smallest and largest key in the BST
# - pop_min()/pop_max(): remove and return the smallest and largest key in the BST

def is_binary_tree_bst_one(tree, low=float('-inf'), high=float('inf')):
    """ Given a binary tree, test if it satisfies the bst property left <= data <= right. """
    if not tree:
        return True
    elif not low <= tree.data <= high:
        return False
    return (is_binary_tree_bst(tree.left, low, tree.data) 
            and is_binary_tree_bst(tree.right, tree.data, high))


def is_binary_tree_bst_two(tree):
    """ Given a binary tree, test if it satisfies the bst property left <= data <= right. 
    This approach is essentially an inorder traversal.
    """
    QueueEntry = collections.namedtuple('QueueEntry', ('node', 'lower', 'upper'))

    bfs_queue = collections.deque([QueueEntry(tree, float('inf'), float('inf'))])

    while bfs_queue:
        front = bfs_queue.popleft()
        if front.node:
            if not front.lower <= front.node.data <= front.upper:
                return False
            bfs_queue += [
                    QueueEntry(front.node.left, front.lower, front.node.data),
                    QueueEntry(front.node.right, front.node, front.upper)
                    ]

    return True


def find_first_greater_than_k(tree, k):
    """ Find the first entry in a BST that is greater than k. 

    If current data is greater than k, cache the current data and search in its left
    subtree. If nothing found, the current key is the result; if found, update it.

    If current data is less than k, we can discard current key and the left subtree,
    go into the right subtree. """
    subtree, first_so_far = tree, None
    while subtree:
        if subtree.data > k:
            first_so_far, subtree = subtree, subtree.left
        else:
            subtree = subtree.right
    return first_so_far


def find_k_largest_in_bst(tree, k):
    """ Find the k largest element in bst.

    Time O(h+k), where h = height. """

    def find_k_largest_in_bst_helper(tree):
        """ Perform reverse inorder traversal. """
        if tree and len(k_largest_elements) < k:
            find_k_largest_in_bst_helper(tree.right)
            if len(k_largest_elements) < k:
                k_largest_elements.append(tree.data)
                find_k_largest_in_bst_helper(tree.left)

    k_largest_elements = []
    find_k_largest_in_bst_helper(tree)
    return k_largest_elements


def find_LCA_bst(tree, s, b):
    """ Find the LCA of two nodes in a bst. """
    while tree.data < s.data or tree.data > b.data:
        # Keep searching since tree is outside of [s, b]
        while tree.data < s.data:
            tree = tree.right # Go larger
        while tree.data > b.data:
            tree = tree.left # Go smaller

    # Now: s.data <= tree.data && tree.data <= b.data
    return tree
