# Good morning! Here's your coding interview problem for today.

# This problem was asked by Google.

# Given a binary search tree and a range [a, b] (inclusive), return the sum of the elements of the binary search tree within the range.



class BinaryTreeSum:

    def __init__(self, data):

        self.data = data
        self.left = None
        self.right = None


    def naive_traversal(self, root, lower_bound, upper_bound, value_list):

        temp_list = value_list
        if (root.data is not None):
            if (root.data <= upper_bound and root.data >= lower_bound):
                temp_list.append(root.data)
            self.naive_traversal(root.left, lower_bound, upper_bound, temp_list)
            self.naive_traversal(root.right, lower_bound, upper_bound, temp_list)

    def tree_sum(self, root, lower_bound, upper_bound, value_list):

        temp_list = value_list
        if root == None:
            return temp_list

        if (root.data <= upper_bound and root.data >= lower_bound):
            temp_list.append(root.data)
            self.tree_sum(root.left, lower_bound, upper_bound, temp_list)
            self.tree_sum(root.right, lower_bound, upper_bound, temp_list)

        elif root.data > upper_bound:
            return self.tree_sum(root.left, lower_bound, upper_bound, temp_list)

        else:
            return self.tree_sum(root.right, lower_bound, upper_bound, temp_list)


root = BinaryTreeSum(5)
root.left = BinaryTreeSum(3)
root.right = BinaryTreeSum(30)
root.left.left = BinaryTreeSum(1)
root.left.right = BinaryTreeSum(4)
root.right.right = BinaryTreeSum(100)
root.right.left = BinaryTreeSum(20)

temp_list = []
l = BinaryTreeSum
l = BinaryTreeSum.tree_sum(root, 4, 15, temp_list)
print(l)




        

