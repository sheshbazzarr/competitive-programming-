// javascript program to print dfs traversal from a given grpah
// this class represents a directed graph using adjacency list representation
//
class Graph
{
	// constructor 
	constructor(v)
	{
		this.V=v;
		this.adj = new Array(v);
		for (let i=0;i<v;i++)
			this.adj[i]=[];
	}
	// function to add an edge into the graph
	addEdge(v,w)
	{
		// And w to v's list.
		this.adj[v].push(w);
	}
	// A function used by DFS
	DFSUtil(v,visited)
	{
		// mark the current node as visited and print it
		visited[v]=true;
		console.log(v+"");
		// Recur for all the verices adjacent to this vertex
		for (let i of this.adj[v].values())
		{
			let n=i
			if(!visited[n])
				this.DFSUtil(n,visited);
		}
	}
	//the function to do DFS traversal . it uses recursive DFSUtil()
	DFS(v)
	{
		// mark all the verices as not visited (set as false by default in java)
		let visited = new Array(this.V);
		for (let i=0;i<this.v;i++)
			visited[i]=false;
		// call the recursive helper function to print DFS
		// traversal
		this.DFSUtil(v,visited);
	}
}
// Driver Code
g= new Graph(4);
g.addEdge(0,1);
g.addEdge(0,2);
g.addEdge(1,2);
g.addEdge(2,0);
g.addEdge(2,3);
g.addEdge(3,3);
console.log("followeing is Depth First Traversal");
g.DFS(2);
// This code is contributed by sheshbazzar byjuly 18,2024
