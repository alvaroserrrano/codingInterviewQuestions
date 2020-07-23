"""
Given a matrix of 1s and 0s, return the number of "islands" in the matrix.
A 1 represents land and 0 represents water, so an island is a group of 1s that
are neighboring whose perimeter is surrounded by water.
Input : mat[][] = {{1, 1, 0, 0, 0},
                   {0, 1, 0, 0, 1},
                   {1, 0, 0, 1, 1},
                   {0, 0, 0, 0, 0},
                   {1, 0, 1, 0, 1}
Output : 5
"""

#The goal is to count the number of connected components in an undirected graph

class Graph:

    def __init__(self, row, col, graph):
        self.ROW = row
        self.COL = col
        self.graph = graph

    #Utility function to check if a given cell can be included in do_dfs
    def is_safe(self, i, j, visited):
        #make sure position is valid
        return (i >= 0 and i < self.ROW and
               j >= 0 and j < self.COL and
               not visited[i][j] and self.graph[i][j])

    #Utility do_dfs that considers 8 neighbors for a 2d matrix
    def do_dfs(self, i, j, visited):
        #utility arrays to check for neighbors
        row_neighbors = [-1, -1, -1, 0, 0, 1, 1, 1]
        col_neighbors = [-1, 0, 1, -1, 1, -1, 0, 1]
        #Mark cell with 1 as visited
        visited[i][j] = True
        #Recur for all neighbors
        for k in range(8):
            if self.is_safe(i + row_neighbors[k], j + col_neighbors[k], visited):
                self.do_dfs(i + row_neighbors[k], j + col_neighbors[k], visited)

    #Main function that returns the count of islands
    def count_islands(self):
        #first all cells are unvisited
        visited = [[False for j in range(self.COL)] for i in range(self.ROW)]
        #starting number of islands is 0
        count = 0
        for i in range(self.ROW):
            for j in range(self.COL):
                if visited[i][j] == False and self.graph[i][j] == 1:
                    #visit all cells in this island and increment count
                    self.do_dfs(i, j, visited)
                    count += 1
        return count


graph = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0],
        [1, 0, 1, 0, 1]]

row = len(graph)
col = len(graph[0])
g = Graph(row, col, graph)
print('Solution: There are %d islands' % g.count_islands())
