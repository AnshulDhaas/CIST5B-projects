import heapq

def dijkstra(self, startVert):
    pq = [(0, startVert)]
    distances = {vertex: float('inf') for vertex in self.adj_list}
    distances[startVert] = 0

    while pq:
        currentDist, currentVert = heapq.heappop(pq)

        if currentDist > distances[currentVert]:
            continue
        #relaxation
        for neighbor, weight in self.adj_list[currentVert]:
            distance = currentDist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

def kruskal(self):
    mst = []
    self.edges.sort()
    parent = {}
    rank = {}
    
    def makeSet(vertex):
        parent[vertex] = vertex
        rank[vertex] = 0
        
    def findSet(vertex):
        if parent[vertex] != vertex:
            parent[vertex] = findSet(parent[vertex])
        return parent[vertex]
    
    def union(vertex1, vertex2):
        root1 = findSet(vertex1)
        root2 = findSet(vertex2)
        
        if root1 != root2:
            if rank[root1] > rank[root2]:
                parent[root2] = root1
            elif rank[root1] < rank[root2]:
                parent[root1] = root2
            else:
                parent[root1] = root2
                rank[root2] += 1
    
    #initialize disjoint sets with makeSet
    #iterate through sorted edges
    #if cycle wont be formed, add to mst and union sets
    for vertex in self.adj_list:
        makeSet(vertex)
        
    for weight, vertex1, vertex2 in self.edges: #iterate through sorted edges
        if findSet(vertex1) != findSet(vertex2): #if cycle wont be formed, add mst and union sets
            mst.append((weight, vertex1, vertex2))
            union(vertex1, vertex2)

    return mst
    
    
    
    
    