# A quack is a data structure combining properties of both stacks and queues. It can be viewed as a list of elements written left to right such that three operations are possible:

# push(x): add a new item x to the left end of the list
# pop(): remove and return the item on the left end of the list
# pull(): remove the item on the right end of the list.
# Implement a quack using three stacks and O(1) additional memory, so that the amortized time for any push, pop, or pull operation is O(1).

#stack 1 and 2 will both push elements onto the back end whenever an element is pusehd in the quack
# stack will will remain empty, until pull is called. at that point, stack2 will be reversed onto stack3
# stack 3 will then pop an element for the pull
#this works because elements pushed on will go both on stack 1 and 2, so it is OK that 2 is empty, as we return the value from stack 1


class quack:

    def __init__():

        stack1 = []
        stack2 = []
        stack3 = []
        size = 0

    def push(self,element):

        self.stack1.append(element)
        self.stack2.append(element)
        self.size += 1

    def pop(self):

        self.stack2.pop()
        temp = self.stack1.pop()
        self.size -= 1
        return temp

    def pull(self):

        if (len(self.stack3) == 0):
            while(len(self.stack2) > 0):
                self.stack3.append(self.stack2.pop())
        self.size -= 1
        return self.stack3.pop()





