#Write a program to merge two binary trees. Each node in the new tree should hold a value equal to the sum of the values of the corresponding nodes of the input trees.

#If only one input tree has a node in a given position, the corresponding node in the new tree should match that input node.


class BinaryTreeSum:

    def __init__(self, data, left, right):
        self.data = data
        self.left = None
        self.right = None

    def traverse(self, n, m):
        if n == None:
            return m
        if m == None:
            return n
        n.data = n.data + m.data
        n.left.data = self.traverse(n.left, m.left)
        n.right.data = self.traverse(n.right, m.right)
        
        return n

#have not tested this but it seems pretty straightforward

        