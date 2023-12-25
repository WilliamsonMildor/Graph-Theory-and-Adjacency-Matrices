#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Graph:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        # creates v^2 matrix
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]

    def display_matrix(self):
        result = ""
        for row in self.matrix:
            result += " ".join(map(str, row)) + "\n"
        return result

    # adding edges
    def add_edge(self, u, v):
        self.matrix[u][v] = 1
        self.matrix[v][u] = 1

    # removing edges
    def remove_edge(self, u, v):
        self.matrix[u][v] = 0
        self.matrix[v][u] = 0

    # degree of vertex
    def degree_of_vertex(self, vertex):
        while True:
            user_vertex = int(input("Enter the vertex (0 to N-1):"))
            if 0 <= user_vertex < self.num_vertices:
                vertex = user_vertex
                break
            else:
                print("Invalid vertex. Please enter a valid vertex index.")
        # retrieves the row in the adjacency matrix
        # corresponding to the given vertex. Thus row represents the
        # connections of the vertex to other vertices. e.g self.matrix[vertex]
        # the sum(self.matrix[vertex]) calculates the sum of the
        # values in that row. Since the matrix represents an undirected graph
        # the sum represents the total number of the edges connected to the given vertex
        return sum(self.matrix[vertex])

    def is_connected(self):
        visited = [False] * self.num_vertices

        def dfs(v):
            visited[v] = True
            for neighbor in range(self.num_vertices):
                if self.matrix[v][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)

        dfs(0)
        return all(visited)

    def degree_of_graph(self):
        total_degree = 0
        for vertex in range(self.num_vertices):
            total_degree += self.degree_of_vertex(vertex)
        return total_degree

# input the number of vertices and edges with validation
while True:
    num_vertices = int(input("Enter the number of vertices: "))
    if num_vertices >= 0:
        break
    else:
        print("Please enter a non-negative number of vertices.")

graph = Graph(num_vertices)

# input the edges
edges_input = input(f"Enter the edges (e.g., AB for an edge between A and B): ")

# Iterate over pairs of characters in the input string
for i in range(0, len(edges_input) - 1, 2):
    u, v = edges_input[i], edges_input[i + 1]

    # Convert vertices to indices (A=0, B=1, ..., G=6)
    u = ord(u) - ord('A')
    v = ord(v) - ord('A')

    # Update the adjacency matrix for an undirected graph
    graph.add_edge(u, v)

# Display the matrix
print(graph.display_matrix())
print(graph.is_connected())
print(graph.degree_of_graph())

