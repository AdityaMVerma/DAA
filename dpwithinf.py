import numpy as np
def floyd_warshall(graph):
    V = len(graph)
    distance = np.copy(graph)

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]

    return distance

# Get the number of vertices (V)
V = int(input("Enter the number of vertices: "))

# Initialize an empty adjacency matrix
adjacency_matrix = np.zeros((V, V), dtype=float)

# Input the matrix from the user
print("Enter the adjacency matrix (use 'inf' for infinity):")
for i in range(V):
    row = input().split()
    for j in range(V):
        if row[j] == 'inf':
            adjacency_matrix[i][j] = float('inf')
        else:
            adjacency_matrix[i][j] = float(row[j])

# Compute the shortest distances using Floyd-Warshall
shortest_distances = floyd_warshall(adjacency_matrix)

# Print the result
print("\nShortest distance matrix:")
for i in range(V):
    for j in range(V):
        if shortest_distances[i][j] == float('inf'):
            print("inf", end="\t")
        else:
            print(int(shortest_distances[i][j]), end="\t")
    print()
