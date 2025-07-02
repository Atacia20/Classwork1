#We will use the first python inbuilt method
#It supports the append() push() and pop()

stack = []

#Creating an empty stack and appending data onto the stack
stack.append(10)
stack.append(20)
stack.append(30)

# print("Stack after the pushes: ", stack)

#peek at the last element of the stack
top_element = stack[-1]  #Access the last element without deleting it
# print(f"top element is: {top_element}")

#Checking if the stack is empty
# if len(stack) == 0:
#     print("Stack is empty")
# else:
#     print("The stack is not empty")


#The second method: using custom classes we implement all key attributes
class SimpleStack:
    def __init__(self):
        self.items = [] #Initialize an empty list to hold items

    def is_empty(self):
        return len(self.items) == 0 #return true if the stack is empty and false otherwise

    #add items to the stack
    def push(self, item):
        self.items.append(item)

    #remove an item from the top and return it
    def pop(self):
        if self.is_empty():  #if the stack is empty return an error to avoid an invalid operatiion
            raise Exception("Cannot pop an empty stack")
        return self.items.pop()

    #PEEK: return the top item without removing it
    def peek(self):
        if self.is_empty():
            raise Exception("STACK IS EMPTY")
        return self.items[-1]

    #Return the number of all the items in the stack
    def size(self):
        return len(self.items)

    def print_stack(self):
        print("Stack from bottom to top:",self.items)
        return

    #main meal
if __name__ == "__main__":
        stack1 = SimpleStack()

        stack1.push(1000)
        stack1.push(2000)
        stack1.push(3000)

        #print the elements
        stack1.print_stack()

        #peek top element
        print("The top element: ",stack1.peek())

        #pop elements
        print("Popped: ", stack1.pop())
        stack1.print_stack()

        #checkk if the stack is empty
        print("Is stack empty? ", stack1.is_empty())

        #pop all to empty
        stack1.pop()
        stack1.pop()
        print("Is stack empty after popping all? ", stack1.is_empty())






