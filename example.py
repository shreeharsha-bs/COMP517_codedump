# Graph generation
import pdb
import numpy as np
# Bonus (no cycles allowed): Modify your program above to check whether the edges that the user selects at each step are about to introduce a cycle in the graph. If that is the case, then an error message should be printed and the user should be asked to start the whole process of selecting edges again.

# A cycle is created if there's an interconnection between 3 or more elements in the graph.
# Cycles in the adjacency matrix can be checked by examining higher powers of the adjacency matrix. With the trace of the Nth power we can identify if a cycle has been introduced
#
def adjacencyList(tempMatrix):
    newList = []
    for row in tempMatrix:
        #pdb.set_trace()
        row = np.array(row)
        newList += [np.where(row==1)[0]]
    return newList

def cycleCheck(graph, locations):
    cycleCreated = 0
    if(len(graph) <= 2):
        return cycleCreated
    
    tempMatrix = matrixMaker(graph, locations)
    pdb.set_trace()
    tempList = list(adjacencyList(tempMatrix))
    tempList = [list(x) for x in tempList]
    print(tempList)
    return cycleCreated

def matrixMaker(graph, locations):
    adjacencyMatrix = [[0]*len(graph) for x in range(len(graph))]

    for i in range(len(graph)):
        adjacencyMatrix[i][i] = 0

    if(locations != [[]]):
        for loc in locations:
            adjacencyMatrix[loc[0]][loc[1]] = 1 # The locations where the connections are made were stored when the user entered the edges
            adjacencyMatrix[loc[1]][loc[0]] = 1 # Because the connections are two way, the matrix is symmetric

    return adjacencyMatrix

graph = dict()
id = 0
adjacencyMatrix = [[]] # The adjacency matrix is known to be a square matrix, nested lists here
locations = []
while True:
    edgeDefinition = False
    try:
        newNode = int(input("Enter a new node\n"))
        if(newNode == 0):
            break
        elif(newNode not in graph):
            graph[newNode] = id 
            id += 1
            print("Node successfully created")
            if(len(graph) > 1):
                edgeDefinition = True
        else:
            raise ValueError
    except ValueError:
        print("Enter a new integer which will represent a new node")


    if(edgeDefinition == True):
        print("You've created a new Node. Which nodes do you want to connect it to?\n")
        print("Here's the list of nodes:\n")
        print(list(graph.keys())[:-1])
        while True:
            try:
                connections = int(input("Enter the node to connect " + str(newNode) +" to. If you don't want to connect this node to any other node, press 0\n"))
                if(connections == 0):
                    break
                elif(connections in graph):
                    locations += [[id-1,graph[connections]]]
                    cycleCreated = cycleCheck(graph,locations)
                    if(cycleCreated == 0):
                        continue
                    else:
                        print("You've created a cycle in the graph!\n")
                        print("Resetting the connections made so far for this node, sorry...")
                        locations = []
                        raise ValueError
                else:
                    raise ValueError
            except ValueError:
                print("Try again, here's the node list. Press 0 if you don't want any more connections\n")
                print(list(graph.keys())[:-1])
    
if(len(graph) == 0):
    adjacencyMatrix = [[1]]
else:
    #pdb.set_trace()
    adjacencyMatrix = matrixMaker(graph,locations)

print(*list(graph.keys()))
print ("______")
for line in adjacencyMatrix:
    print(*line)
