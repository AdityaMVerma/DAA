import math
import numpy as np

size = int(input("Please input the size fo matrix: "))
matrix =np.zeros((size,size))
#intial condition of matrix
print(matrix)
print("Write the distances between the places")
for i in range(0,size):
    for j in range(0,size):
        matrix[i][j]=int(input())

#weighted matrix
print(matrix)


def floyd_warshall(graph):
    V = len(graph)
    distance = np.copy(graph)

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if distance[i][k] + distance[k][j] < distance[i][j]:
                    distance[i][j] = distance[i][k] + distance[k][j]
    return distance


shortest_distances = floyd_warshall(matrix)


print("\nShortest distance matrix:")
for i in range(size):
    for j in range(size):
            print(int(shortest_distances[i][j]), end="\t")
    print()