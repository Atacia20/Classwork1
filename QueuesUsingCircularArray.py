
class CIRCULARARRAYQUEUE:
    """"
    A queue will use the FIFO principle
    This is a circular queue - imagine the array as a circle here after the last position,
     we wrap back to the first position. This prevents us from having to shift all the elements when we remove/dequeue
    """

    #We start by defining the max number of elements the queue will hold
    DEFAULT_CAPACITY = 10

    def __init__(self):
        """"
        We continue to create an empty queue by initializing three important things:
        i. _data: which is the list filled with None values, the array...
        ii. _size: How many actual elements are at a given timestamp, we will initialize it to zero.
        iii. _front: The index or the position where the first element is located. We initialize it to zero too
        """

        #Create the array with a default capacity slots, all filled with None
        self._data = [None] *CIRCULARARRAYQUEUE.DEFAULT_CAPACITY

        #We keep track of how many elements are in our array
        self._size = 0

        #We keep track of the first car we parked
        self._Front = 0

    def __len__(self):
        """"
        This is a dunder method.
        It returns the size of an attribute created in the primary constructor
        In this case, it is the elements currently in the queue
        """
        return self._size

    def is_empty(self):
        """"
        This method will return a boolean, denoted by the double equal sign, which is a comparison operator
        It will return true if the array is empty, and false if the array has at least one element
        """
        return self._size == 0

    def first(self):
        """"
        This method is like the PEEK() in the stacks. It will return the element at the front of the queue without removing it
        The method will raise an empty exemption if the queue is empty
        """
        if self.is_empty():
            raise Empty('Queue is empty') # This exception is raised by calling the class empty that is lower in the code.

        #Return the first element is at position self._front in the array
        return self._data [self._Front]

    def dequeue(self):
        """"
        This method will remove and return the first element of the queue.

        Here we have another concept of circular linked lists, where instead of shifting all elements left which is slow,
        we just move the _front pointer to the next position and use MODULUS(%) arithmetic to wrap around when we reach the end of the array.
        """

        if self.is_empty():
            raise Empty('Queue is empty')

        #Here we get to the element at the front of the queue and save it in an attribute
        item_to_dequeue = self._data[self._Front]

        """"
        We then clear the old front position to help with garbage collection
        
        GARBAGE COLLECTION - A technique/process/procedure manual or autonomous, that handles memory allocation and deallocation,
        ensuring efficient use of memory
        """

        self._data[self._Front] = None

        """"
        We now move the pointer to the next position.
        We do this by using the modulus operator
        """
        self._Front = (self._Front + 1) % len(self._data)

        #We then resize the queue/array.
        self._size -= 1

        # return the dequeued element
        return item_to_dequeue

    def enqueue(self, element):
        """"
        This is adding an element to the back of the queue.
        """

        # we will start by checking if the queue is full. If it is full we increase the size of the queue
        if self._size == len(self._data):
            self._resize(2 * len(self._data)) #double the capacity

        #Calculate where to put the new element, which is at the back of the queue.
        """"
        This is how we calculate the position where to enqueue, which is the last position:
        
        assume the head is at position 3 and the number of elements in the queue at that
        particular time is 4, and the default capacity of the queue is 10: (3+4) % 10 = 7: which 
        means that we will now enqueue at position 7
        """
        back_of_the_queue = (self._Front + self._size) % len(self._data)

        #Place the element in the position gotten after the "calculation"
        self._data[back_of_the_queue] = element

        #We now increment the size of our array/queue.
        self._size += 1

        #WHAT IF THE QUEUE IS FULL AND YOU NEED TO RESIZE? NO WORRIES! HERE'S HOW WE DO IT
    def _resize(self, new_capacity):
        """"
        This method will double the size of our queue only when there are no available slots, and we want to enqueue
        The current size is multiplied by a factor specified by the user, in our case; new_capacity
        """

        #reate a new, bigger array
        old_data = self._data # hold all the existing data in our queue in the variable old_Data
        self._data = [None] * new_capacity #resizing by new_capacity factor

        """
        we then copy all elements from the old array/queue to the new one, 
        starting from the front and going in the queue order. 
        """
        current_index = self._Front
        for item in range (self._size):
            #copy each element to the new array in order
            self._data[item] = old_data [current_index]

            #Move to the next index and remember to wrap if necessary
            current_index = (current_index + 1) % len(old_data)

        #we reset the front to position 0
        self._front = 0

#Now wwe create the exception class talked about earlier.
class Empty(Exception):
    def __init__(self, message = "Queue is empty"):
        self.message = message
        super().__init__(self.message)


#THE MAIN BLOCK
if __name__ == "__main__":
    #create a new queue
    queue = CIRCULARARRAYQUEUE()

    print("QUEUES USING CIRCULAR ARRAYS")
    print(f"The initial queue size is {len(queue)}")
    print(f"Is the queue empty? {queue.is_empty()}")

    #ENQUEUE OUR ARRAY/QUEUE
    print("\n Enqueueing our queue")
    elements_to_enqueue = ['Alice', 'Bob', 'William', 'Dorothy', 'Jessica']

    for person in elements_to_enqueue:
        queue.enqueue(person)
        print(f"Added {person}. Queue size is now: {len(queue)}")

    #show the front element without removing it
    print(f"\n Person at the front of the queue is: {queue.first()}")

    #Dequeueing operation
    print(f"\nServing people from the front of the queue.")
    for i in range(3):
        served_person = queue.dequeue()
        print(f"Served: {served_person}. Queue size is now: {len(queue)}")

    #to demonstrate the circular nature of the array, we induce an overflow to see if it behaves correctly
    print("\n Adding more people to induce a wrap around in the array")
    more_people = ['Frank', 'Linda', 'Ford', 'John', 'Doe', 'Shakespear']
    for person in more_people:
        queue.enqueue(person)
        print(f"Added {person}. The queue size is now: {len(queue)}")

    #show what's left in the queue
    print(f"\nPerson currently at the front is: {queue.first()}")
    print(f"Total people still in the queue: {len(queue)}")

    # Demonstrate the wrap around by showing the internal state
    print(f"\n Internal details")
    print(f"Front Index: {queue._Front}")
    print(f"Array Contents: {queue._data}")

    # NB: None value are empty slots in our circular array.
