#Implement a queue using a set of fixed-length arrays.

#The queue should support enqueue, dequeue, and get_size operations.

#I implemented a pseudo linked list of arrays, with each array pointing to the previous and next arrays. 
#ignore the naming convention of head/tail, should be prev/next
class queue_implementation:

    def __init__(self, length, head=None, tail=None):

        self.length = length
        self.arr = []
        self.head = head
        self.tail = tail

    def enqueue(self, data):

        #traverse until arrive at the last array
        l = self.length
        temp_obj = self
        temp_arr = self.arr
        temp_tail = self.tail
        while (temp_tail is not None):
            temp_obj = temp_obj.tail
            temp_arr = temp_obj.arr
            temp_tail = temp_obj.tail
        #should now be in the last array
        #adds the element in to the last array, if another array need not be created
        i = 0
        while (temp_arr[i] is not None):
            i += 1
        if (i < (l -2)):
            temp_arr[i] = data
        #creates a new array if necessary
        else:
            new_obj = queue_implementation(length=l, head=temp_obj)
            temp_arr[l-1] = new_obj
            new_obj.arr[0] = temp_obj
            new_obj.arr[1] = data
        
    def get_size(self):

        counter = 0
        l = self.length
        temp_obj = self
        temp_arr = self.arr
        temp_tail = self.tail
        while (temp_tail is not None):
            temp_obj = temp_obj.tail
            temp_arr = temp_obj.arr
            temp_tail = temp_obj.tail
            counter += 1
        small_counter = 0
        while (temp_arr[small_counter] is not None):
            small_counter += 1
        size = (l - 2) * (counter) + (small_counter)
        return size
    
    def dequeue(self):

        result = self.arr[1]

        l = self.length
        temp_obj = self
        temp_arr = self.arr
        temp_tail = self.tail
        #traverse and adjust elements
        while (temp_tail is not None):
            i = 1
            if (i < (l-2)):
                temp_arr[i] = temp_arr[i+1]
                i += 1
            temp_arr[i] = temp_obj.tail.arr[1]
            temp_obj = temp_obj.tail
            temp_arr = temp_obj.arr
            temp_tail = temp_obj.tail
        #arrive at last array
        #check if there is only one element, delink the last array if so

        if (temp_arr[2] is None):
            temp_obj.tail = None
        else:
            i = 1
            temp_arr[i] = temp_arr[i+1]
        return result
        

            




