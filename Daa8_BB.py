import heapq

def tsp_branch_and_bound(graph):
    n = len(graph)
    visited = set()
    pq = [(0, 0, 1, {0})]  # (lower bound, current cost, current city, visited cities)

    while pq:
        lower_bound, cost, current_city, visited_cities = heapq.heappop(pq)

        if len(visited_cities) == n:
            return list(visited_cities) + [0]  # Return the complete tour

        for next_city in range(n):
            if next_city not in visited_cities:
                new_cost = cost + graph[current_city][next_city]
                new_lower_bound = new_cost + min(graph[next_city])  # Minimum edge cost from next city
                new_visited = visited_cities.union({next_city})
                heapq.heappush(pq, (new_lower_bound, new_cost, next_city, new_visited))

    return None  # No valid tour found

# Example Usage:
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

optimal_tour_bb = tsp_branch_and_bound(graph)
print("Optimal Tour:", optimal_tour_bb)
