# Topological Sorting
# https://www.geeksforgeeks.org/topological-sorting/
# Topological sorting for Directed Acyclic Graph (DAG) is a linear ordering of vertices such that for every
# directed edge (u,v), vertex 'u' comes before 'v' in the ordering. Topological Sorting for a graph is not
# possible if the graph is not a DAG.
# The first vertex in topological sorting is always a vertex with in-degree as 0 (a vertex with no incoming
# edges).
# https://youtu.be/Q9PIxaNGnig

# Algorithm to find Topological Sorting:
# In DFS, we start from a vertex, we first print it and then recursively call DFS for its adjacent vertices.
# In topological sorting, we use a temporary stack. We don’t print the vertex immediately, we first recursively
# call topological sorting for all its adjacent vertices, then push it to a stack. Finally, print contents of
# the stack. Note that a vertex is pushed to stack only when all of its adjacent vertices (and their adjacent
# vertices and so on) are already in the stack. (Check image)

# Python program to print topological sorting of a DAG
from collections import defaultdict

# Class to represent a graph


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # dictionary containing adjacency List
        self.V = vertices  # No. of vertices

    # function to add an edge to graph
    def addEdge(self, u, v):
        self.graph[u].append(v)

    # A recursive function used by topologicalSort
    def topologicalSortUtil(self, v, visited, stack):

        # Mark the current node as visited.
        visited[v] = True

        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)

        # Push current vertex to stack which stores result
        stack.append(v)

    # The function to do Topological Sort. It uses recursive
    # topologicalSortUtil()
    def topologicalSort(self):
        # Mark all the vertices as not visited
        visited = [False]*self.V
        stack = []

        # Call the recursive helper function to store Topological
        # Sort starting from all vertices one by one
        for i in range(self.V):
            if visited[i] == False:
                self.topologicalSortUtil(i, visited, stack)
            # print(stack)


        # Print contents of the stack
        print(stack[::-1])  # return list in reverse order


# Driver Code
g = Graph(6)
g.addEdge(5, 2)
g.addEdge(5, 0)
g.addEdge(4, 0)
g.addEdge(4, 1)
g.addEdge(2, 3)
g.addEdge(3, 1)

print("Following is a Topological Sort of the given graph")
g.topologicalSort()
# print(g.graph)


# Complexity Analysis:

# Time Complexity: O(V+E).
# The above algorithm is simply DFS with an extra stack. So time complexity is the same as DFS.
# Auxiliary space: O(V).
# The extra space is needed for the stack.

# Applications:
# Build Systems - in IDE's.
# Task scheduling.
# pre-requisite problems.
