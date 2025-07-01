from symtable import Class

class SinglyLinkedList:
    def _init_(self, value, nextNode = None):
        self.value = value
        self.nextNode = nextNode

snode1 = SinglyLinkedList("1")
snode2 = SinglyLinkedList("2")
snode3 = SinglyLinkedList("3")
snode4 = SinglyLinkedList("4")
snode5 = SinglyLinkedList("5")

snode1.nextNode = snode2
snode2.nextNode = snode3

currentNode = snode1
while True:
    print(currentNode.value, ">>>", end= '')

    if currentNode.nextNode is None:
        print("None")
        break
    currentNode = currentNode.nextNode

class Node:
    def _init_(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def _init_(self):
        self.head = None

    def deleteFromTheBegining(self):
        if self.head is None:
            return "List is Empty"
        self.head = self.head.next

    def deleteFromTheEnd(self):
        if self.head is None:
            return "List is Empty"
        if self.head.next is None:
            self.head = None
            return
        temp = self.head
        while temp.next.next:
            temp = temp.next
        temp.next = None


    def insertAtTheEnd(self, new_data):
        new_node = Node(new_data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insertAtTheBeginning(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head

        self.head = new_node

    def printLinkedList(self):
        temp = self.head
        while temp:
            print(temp.data, end= ' ')
            temp = temp.next
        print()

if _name_ == '_main_':
    llist = LinkedList()
    llist.insertAtTheBeginning('Fox')
    llist.insertAtTheBeginning('Brown')
    llist.insertAtTheBeginning('Quick')
    llist.insertAtTheBeginning('The')
    llist.insertAtTheEnd('Jumps')
    llist.deleteFromTheEnd()
    llist.deleteFromTheBegining()
    llist.insertAtTheBeginning('A')
    llist.printLinkedList()
