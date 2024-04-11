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


