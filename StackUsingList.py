class StackNode:
    def __init__(self, value):
        self.value = value
        self.next = None

#Stack implemented using a linked list
class LinkedListStack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None  #Stack is empty if the pointer is None

    def push(self, value):
        new_node = StackNode(value) #cteate a new node with the value
        new_node.next = self.top #new nodes next pointer should be the current top node
        self.top = new_node #update the pointer to new node (new node of the stack)


    def pop(self):
        if self.is_empty(): # if the stack is empty raise an error
            raise Exception("Cannot pop from an empty stack!")

        popped_value = self.top.value # retrieve the value from the top node

        self.top = self.top.next #move the pointer to the next node down the stack
        return popped_value

    def peek(self):
        if self.is_empty(): #Return the top element without removing it.
            raise Exception("Cannot peek an empty stack!")
        return self.top.value

    def display(self):
        current = self.top
        values = []
        while current:
            values.append(str(current.value))
            current = current.next
        print("Stack from top to bottom: ", " -> ".join(values))

#Example usage
if __name__ == "__main__":
    stack_11 = LinkedListStack()
    stack_11.push(5)
    stack_11.push(10)
    stack_11.push(15)

    stack_11.display() #Expected stack from the top to bottom; 15 -> 10 -> 5

    print('Peek top: ', stack_11.peek())

    print("Pop: ", stack_11.pop())

    stack_11.display()
