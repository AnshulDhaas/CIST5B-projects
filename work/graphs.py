class Graph:
    def __init__(self):
        self.graph_matrix = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, vertex, edge):
        if vertex not in self.graph:
            self.graph[vertex] = []
        if edge not in self.graph:
            self.graph[edge] = []
        if edge not in self.graph[vertex]:
            self.graph[vertex].append(edge)
        if vertex not in self.graph[edge]:
            self.graph[edge].append(vertex)
    
    def display(self):
        print(self.graph)

    def adjacency_matrix(self):
        vertices = sorted(self.graph.keys())
        num_vertices = len(vertices)

        matrix = [[0] * num_vertices for _ in range(num_vertices)]

        vertex_index = {vertex: idx for idx, vertex in enumerate(vertices)}
        
        for vertex in self.graph:
            for edge in self.graph[vertex]:
                i = vertex_index[vertex]
                j = vertex_index[edge]
                matrix[i][j] = 1
                matrix[j][i] = 1
        
        print("Adjacency Matrix:")
        print("   " + " ".join(map(str, vertices)))
        for i, row in enumerate(matrix):
            print(vertices[i], row)
        
        return matrix
    
    from collections import deque, defaultdict

    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        
        visited.add(start_vertex)
        
        while queue:
            current_vertex = queue.popleft()
            print(current_vertex)
            for neighbor in self.graph_matrix[current_vertex]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)
