def tsp_dp(graph):
    n = len(graph)
    # DP table initialization
    dp = [[float('inf')] * n for _ in range(1 << n)]

    # Base case: DP[S, i] = 0 for all i in S containing only the start city
    dp[1][0] = 0

    # DP recurrence
    for mask in range(1, 1 << n, 2):  # Iterate over odd subsets
        for u in range(1, n):
            if mask & (1 << u):
                for v in range(n):
                    if mask & (1 << v) and u != v:
                        dp[mask][u] = min(dp[mask][u], dp[mask ^ (1 << u)][v] + graph[v][u])

    # Reconstruct optimal tour
    mask = (1 << n) - 1
    u = min(range(1, n), key=lambda x: dp[mask][x] + graph[x][0])
    tour = [u]
    while mask:
        v = min(range(n), key=lambda x: dp[mask][x] + graph[x][u])
        tour.append(v)
        mask ^= 1 << v
        u = v

    return tour

# Example Usage:
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

optimal_tour = tsp_dp(graph)
print("Optimal Tour:", optimal_tour)
