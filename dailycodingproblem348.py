# A ternary search tree is a trie-like data structure where each node may have up to three children. 
# Here is an example which represents the words code, cob, be, ax, war, and we.
# Implement insertion and search functions for a ternary search tree.

#Did not test but the logic should be OK
class TernaryTree:

    def __init__(self, left, middle, right):

        self.left = left
        self.middle = middle
        self.right = right

    #function is called recursively and traverses the tree. 
    def search(s, root):

        not_found = "This word is not in the ternary tree"
        found = "This word is in the ternary tree"

        #Recursion here
        if (len(s) > 1):
            if (s[0] == root):
                TernaryTree.search(s[1:], root.middle)

            elif (s[0] < root):
                if (root.left is None):
                    print(not_found)
                else:
                    TernaryTree.search(s, root.left)

            else:
                if (root.right is None):
                    print(not_found)
                else:
                    TernaryTree.search(s, root.right)

        #Base case
        else:
            if (root.right == s or root.left == s or root.middle == s):
                print(found)
            else: 
                print(not_found)

    def insert(s, root):
        
        if (len(s) > 1):
            if (s[0] < root):
                if (root.left is None):
                    root.left = s[0]
                TernaryTree.insert(s, root.left)
            elif (s[0] > root):
                if (root.right is None):
                    root.right = s[0]
                TernaryTree.insert(s, root.right)
            else:
                if (root.middle is None):
                    root.middle = s[1]
                if (root.middle == s[1]):
                    TernaryTree.insert(s[1:], root.middle)

        else:
            if (s[0] == root):
                print("inserted")
            elif (s[0] < root):
                root.left = s[0]
                print("inserted")
            else:
                root.right = s[0]
                print("inserted")


