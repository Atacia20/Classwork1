class binarySearchTreeNode:
    def __init__(self,data):
        self.data=data
        self.leftChildNode=None
        self.rightChildNode=None

    def insert(self,value):
        #Disallow duplicate values
        if value<self.data:
            if self.leftChildNode is None:
                self.leftChildNode=binarySearchTreeNode(value)
            else:
                self.leftChildNode.insert(value)
        elif value>self.data:
            if self.rightChildNode is None:
                self.rightChildNode=binarySearchTreeNode(value)
            else:
                self.rightChildNode.insert(value)
        else:
            raise ValueError(f"Duplicate value {value} cannot be inserted into the Binary Search Tree")


    def search(self,value):
        if self.data==value:
            return self
        elif value<self.data:
            if self.leftChildNode is None:
                return None
            else:
                return self.leftChildNode.search(value)
        else:
            if self.rightChildNode is None:
                return None
            else:
                return self.rightChildNode.search(value)

    def findMinimum(self):
        if self.leftChildNode is None:
            return self
        else:
            return self.leftChildNode.findMinimum()

    def delete(self,value):
        if value<self.data:
            if self.leftChildNode is not None:
                self.leftChildNode.delete(value)
        elif value>self.data:
            if self.rightChildNode is not None:
                self.rightChildNode.delete(value)
        else:
            #Node to delete found
            if self.leftChildNode is None:
                return self.rightChildNode
            elif self.rightChildNode is None:
                return self.leftChildNode
            else:
                #Node has two children: find the minimum in the right
                minimumLargerNode=self.rightChildNode.findMinimum()
                self.data=minimumLargerNode.data
                self.rightChildNode=self.rightChildNode.delete(minimumLargerNode.data)
            return self

    def inOrderTraversal(self):
        result=[]
        if self.leftChildNode is not None:
            result+=self.leftChildNode.inOrderTraversal()
        result.append(self.data)
        if self.rightChildNode is not None:
            result+=self.rightChildNode.inOrderTraversal()
        return result

    def preOrderTraversal(self):
        result=[self.data]
        if self.leftChildNode is not None:
            result+=self.leftChildNode.preOrderTraversal()
        if self.rightChildNode is not None:
            result+=self.rightChildNode.preOrderTraversal()
        return result


    def postOrderTraversal(self):
        result=[]
        if self.leftChildNode is not None:
            result+=self.leftChildNode.postOrderTraversal()
        if self.rightChildNode is not None:
            result+=self.rightChildNode.postOrderTraversal()
        result.append(self.data)
        return result

    def height(self):
        if self.leftChildNode is not None:
            leftHeight=self.leftChildNode.height()
        else:
            leftHeight=0

        if self.rightChildNode is not None:
            rightHeight=self.rightChildNode.height()
        else:
            rightHeight=0

        return 1+max(leftHeight,rightHeight)


rootNode=binarySearchTreeNode(50)
rootNode.insert(30)
rootNode.insert(70)
rootNode.insert(20)
rootNode.insert(40)
rootNode.insert(60)
rootNode.insert(80)

try:
    rootNode.insert(30) # Test error handling for duplicate values
except Exception as e:
    print("Error: ", e)

found=rootNode.search(60)
if found is not None:
    print("Search 60: ",found.data)
else:
    print("Search 60: Not found")

print("Height of the Binary Search Tree: ",rootNode.height())

print("Pre-Order Traversal")
for i in rootNode.preOrderTraversal():
    print(i)

print("In-Order Traversal")
for i in rootNode.inOrderTraversal():
    print(i)

print("Post-Order Traversal")
for i in rootNode.postOrderTraversal():
    print(i)

rootNode.delete(70)
print("In order traversal after deleting 70:",rootNode.inOrderTraversal())
