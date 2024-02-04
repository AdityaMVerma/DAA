#floyd warshall algorithm

import numpy as np

def floyd_warshall_algo(graph):
    V = len(graph)
    distance=np.copy(graph)

    for i in range (V):
        for j in range(V):
            for k in range(V):
                if distance[i][k]+distance[k][j]<distance[i][j]:
                    distance[i][j]=distance[i][k]+distance[k][j]

    return distance

if __name__=="__main__":
    V=int(input("Enter the number of cities"))
    adjacency_matrix=np.zeros((V,V),dtype=float)

    #take the input form user
    print("Enter the values for the adjacency matrix")
    for i in range (V):
        row=input().split()
        for j in range (V):
            if row[j]=='inf':
                adjacency_matrix[i][j]=float('inf')
            else:
                adjacency_matrix[i][j]=float(row[j])
    shortest_distance=floyd_warshall_algo(adjacency_matrix)

    for i in range (V):
        for j in range (V):
            if shortest_distance[i][i]==float('inf'):
                print("inf")
            else:
                print(int(shortest_distance[i][j]), end="\t")
        print()




