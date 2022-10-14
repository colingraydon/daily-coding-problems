# Given a linked list and an integer k, remove the k-th node from the end of the list and return the head of the list.

# k is guaranteed to be smaller than the length of the list.


class Node:
    def __init__(self, val):

        self.val = val
        self.next = None


class LinkedList:
    def __init__(self):

        self.head = None

    def print_list(self):

        current = self.head
        while current is not None:

            print(current.val)
            current = current.next
        print("----------")

    def remove_kth(self, k):

        if k == 0:
            ans = self.head
            new_head = self.head.next
            self.head = new_head
        else:
            ans = self.head

        count = 0
        current = self.head

        while count < (k - 1):

            next = current.next
            current = next
            count += 1

        temp = current.next.next
        current.next = temp
        return ans


l = LinkedList()
e1 = Node(1)
e2 = Node(2)
e3 = Node(3)
e4 = Node(4)
l.head = e1
e1.next = e2
e2.next = e3
e3.next = e4
l.print_list()
print(l.remove_kth(2).val)
print("--------")
l.print_list()
