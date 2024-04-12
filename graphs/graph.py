#Graphs are data structures which contain nodes or vertices, which are connected to each other through edges.
#Tress and Linked Lists are basically graphs having nodes and connections between the nodes.
#Now, graphs are primarily classified by three properties - Cyclic/Acyclic, Weighted/Unweighted/, Directed/Undirected Graphs
#There are many many applications of graphs and many opertions can be performed on them.
#A graph can be represented in 3 ways - Adjacency List, Adjacency Matrix, Edge List.
#Adjacency list stores the nodes with which a particular node is connected to in a linked list or array.
#All these lists or arrays can be stored in a hash table with the keys being the nodes and the values being their respective lists
#Adjcaency matrix is a nXn matrix where n is the number of nodes. M[i][j] = 1 if nodes i and j are connected otherwise 0
#Edge list contains all the pairs of nodes which are connected, and if the graph is weighted, then the weight of each edge as well
#Here we will build an undirected graph using an adjacency list.


class Graph:
    def __init__(self):
        self.adjacency_list = {}
        self.number_of_nodes = 0
    def insert_node(self,data):
        if data not in self.adjacency_list:
            self.adjacency_list[data] = []
            self.number_of_nodes += 1
            return
        #print("node already exsists") 
    def insert_edge(self,vertex1,vertex2):
        if vertex2 not in self.adjacency_list[vertex1]:
            self.adjacency_list[vertex1].append(vertex2)
            self.adjacency_list[vertex2].append(vertex1)
            return
        print("Edge already exists")
    def show_connections(self):
        for node in self.adjacency_list:
            print(node,end = "-->")
            for vertex in self.adjacency_list[node]:
                print(vertex,end = ' ')
            print()
        
    
g = Graph()
g.insert_node(0)
g.insert_node(1)
g.insert_node(2)
g.insert_node(3)
g.insert_node(4)
g.insert_node(5)
g.insert_edge(0,1)
g.insert_edge(0,2)
g.insert_edge(1,2)
g.insert_edge(1,3)
g.insert_edge(2,4)
g.insert_edge(3,4)
g.insert_edge(4,5)

g.show_connections()
