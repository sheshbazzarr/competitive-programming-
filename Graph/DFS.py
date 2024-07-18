from collections import defaultdict

class Graph:
    # constructor 
    def __init__(self):
        #default dictionary to store graph
        self.graph=defaultdict(list)
    #function to add an edge to graph
    def addEdge(self,u,v):
        self.graph[u].append(v)

    # a function used by DFS
    def DFSUtill(self,v,visted):
        # mark the current node as visted 
        #and print it 
        visted.add(v)
        print(v,end=" ")
        #Recur for all the vertices
        #adjacent to this vertex
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtill(neighbour,visited)
    # the function to do DFS traversal .It uses 
    # recursive DFSUtil()
    def DFS(self,v):
        # create a set to store visitied vertices
        visited=set()
        #call the recurisve helper function 
        #to print DFS traversal
        self.DFSUtil(v,visited)

    # Driver's code 
    if __name__=="__main__":
        g=Graph()
        g.addEdge(0,1)
        g.addEdge(0,2)
        g.addEdge(1,2)
        g.addEdge(2,0)
        g.addEdge(2,3)
        g.addEdge(3,3)

        g.DFS(2)

        # this code is contributed by sheshbazzar

