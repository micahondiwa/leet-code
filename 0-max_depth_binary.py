""" Given the root of a binary tree, return its maximum depth."""
def maxdepth(root):
    if root == Node:
        return 0
    left = 0
    right = 0
    if root.left:
        left = maxdepth(root.left) + 1
    if root.right:
        right = maxdepth(root.right) + 1
    return max(left, right)