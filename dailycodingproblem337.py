# Given a linked list, uniformly shuffle the nodes. 
# What if we want to prioritize space over time?


#this should use O(1) space
import random

class Node:

    def __init__(self, data=None):
        self.data = data
        self.nextdata = None

class LinkedList:

    def __init__(self, data=None):

        self.head = None

    def print_list(self):

        temp = self.head
        while temp is not None:
            print(temp.data)
            temp = temp.nextdata

    def get_length(self):

        i = 1
        temp = self.head
        while temp is not None and temp.nextdata is not None:
            i+=1
            temp = temp.nextdata
        return i

    def shuffle_list(self,linked_list):

        l = self.get_length() - 1
        if l == 0:
            return linked_list

        for _ in range(l):
            i = random.randint(0, l)
            j = random.randint(0, l)
            temp1 = linked_list.head
            temp2 = linked_list.head

            for _ in range(i):
                temp1 = temp1.nextdata

            for _ in range(j):
                temp2 = temp2.nextdata

            holder = Node(temp1.data)
            temp1.data = temp2.data
            temp2.data = holder.data

        return linked_list

    
if __name__ == "__main__":
    test = LinkedList()
    test.head = Node(0)
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    test.head.nextdata = node1
    node1.nextdata = node2
    node2.nextdata = node3
    node3.nextdata = node4

    test.print_list()
    test.shuffle_list(test)
    test.print_list()




            



