#Dijkstra's algorithm finds the shortest path from a start node to all other nodes in a weighted directed graph assuming : all edge weights are non negative and you want the shortest distance
class DirectedWeightedGraph2:
    def __init__(self):
        self.adjacencyList={}  #  {vertex:[(neighbour,weight)]}

    def addVertex(self,vertex):
        if vertex not in self.adjacencyList:
            self.adjacencyList[vertex]=[]
        else:
            print(f"Vertex {vertex} already exists")

    def addEdge(self,fromVertex,toVertex,weight):
        if fromVertex not in self.adjacencyList:
            print(f"{fromVertex} does not exist")
            return
        if toVertex not in self.adjacencyList:
            print(f"{toVertex} does not exist")
            return

        self.adjacencyList[fromVertex].append((toVertex,weight))

    def removeEdge(self,fromVertex,toVertex):
        newNeighbours=[]
        for neighbourPair in self.adjacencyList[fromVertex]:
            neighbourVertex=neighbourPair[0]
            weight=neighbourPair[1]

            if neighbourVertex != toVertex:
                newNeighbours.append((neighbourVertex,weight))
        self.adjacencyList[fromVertex]=newNeighbours


    def printGraph(self):
        for vertex in self.adjacencyList:
            print(f"{vertex} --> {self.adjacencyList[vertex]}")

    def dijkstraShortestPaths(self,startingVertex):
        import heapq #Importing priority queues
        distances={}
        for vertex in self.adjacencyList:
            distances[vertex]=float('inf')
        distances[startingVertex]=0

        visitedVertices=set()
        priorityQueue=[]
        heapq.heappush(priorityQueue,(0,startingVertex))  #(cost,vertex)

        while len(priorityQueue)>0:
            currentCost,currentVertex=heapq.heappop(priorityQueue)
            if currentVertex in visitedVertices:
                continue
            else:
                visitedVertices.add(currentVertex)
            neighbours=self.adjacencyList[currentVertex]
            for neighbourPair in neighbours:
                neighbourVertex=neighbourPair[0]
                edgeWeight=neighbourPair[1]

                newDistance=currentCost+edgeWeight
                if newDistance<distances[neighbourVertex]:
                    distances[neighbourVertex]=newDistance
                    heapq.heappush(priorityQueue,(newDistance,neighbourVertex))

        return distances


exampleGraph=DirectedWeightedGraph2()
exampleGraph.addVertex("A")
exampleGraph.addVertex("B")
exampleGraph.addVertex("C")
exampleGraph.addVertex("D")
exampleGraph.addVertex("E")
exampleGraph.addVertex("F")



exampleGraph.addEdge("A","B",5)
exampleGraph.addEdge("A","C",2)
exampleGraph.addEdge("B","D",1)
exampleGraph.addEdge("D","E",11)
exampleGraph.addEdge("D","F",4)





exampleGraph.printGraph()
distancesFromNode=exampleGraph.dijkstraShortestPaths("A")
print("Shortest distances from A")
for node,distance in distancesFromNode.items():
    print(f"A-->{node}:{distance}")
