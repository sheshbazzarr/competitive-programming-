// java program to print DFS traversal 
// from a given graph
import java.io.*;
import java.util.*;

// this class represent a directed graph using adjacency list representation

class Graph{
	private int V;
	// Array of lists for adjacency list representation
	private LinkedList<Integer> adj[];
	// constructor 
	@SuppressWarnings("Unchecked")Graph(int v)
	{
		V=v;
		adj = new LinkedList[v];
		for (int i=0; i<v; ++i)
			add[i]= new LinkedList();
	}
	// function to add an edge into the graph
	void addEdge(int v, int w)
	{
		// Add w to v's list.
		add[V].add(w);
	}
	// a function used by DFS
	void DFSUtil(int v,boolean visited[])
	{
		// mark the current node as visited and print it
		visited[v]=true;
		System.out.print(v+"");
		// Recur for all the vertices adjacent to this vertex
		Iterator<Integer> i = add[v].listIterator();
		while (i.hasNext()){
			int n=i.next();
			if(!visited[n])
				DFSUtil(n,visited);
		}
	}

	// the function to do DFS traversal .it uses recursive DFSUtil()
	void DFS(int v)
	{
		// mark all the vertices as 
		// not visited (set as false by default in java)
		boolean visited[]=new boolean[V];
		// call the recursive helper function to Dfs traversal
		DFSUtil(v,visited);
	}
	// Driver code
	public static void main(String args[])
	{
		Graph g = new Graph(4);
		g.addEdge(0,1);
		g.addEdge(0,2);
		g.addEdge(1,2);
		g.addEdge(2,0);
		g.addEdge(2,3);
		g.addEdge(3,3);

		System.out.println("following is depth first traversal");
		g.DFS(2);
	}
}

