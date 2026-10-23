# Travelling Salesman Problem (TSP)
# Find the shortest tour that visits every city exactly once and returns to the start city.
# Method 1: Brute force (checks every tour, always gives the optimal answer)
# Method 2: Nearest Neighbour (fast greedy heuristic, may not be optimal)
from itertools import permutations

cities = ["A", "B", "C", "D", "E"]
dist = [            # dist[i][j] = distance between city i and city j
    [0, 12, 10, 19, 8],
    [12, 0, 3, 7, 2],
    [10, 3, 0, 6, 20],
    [19, 7, 6, 0, 4],
    [8, 2, 20, 4, 0],
]

def tour_cost(tour):
    return sum(dist[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

def brute_force(start=0):
    others = [c for c in range(len(cities)) if c != start]
    best_tour, best_cost = None, float("inf")
    for perm in permutations(others):
        tour = (start,) + perm + (start,)
        cost = tour_cost(tour)
        print("  " + " -> ".join(cities[c] for c in tour) + f"   cost = {cost}")
        if cost < best_cost:
            best_tour, best_cost = tour, cost
    return best_tour, best_cost

def nearest_neighbour(start=0):
    tour, current = [start], start
    unvisited = set(range(len(cities))) - {start}
    while unvisited:
        current = min(unvisited, key=lambda c: dist[current][c])   # closest unvisited city
        unvisited.remove(current)
        tour.append(current)
    tour.append(start)
    return tour, tour_cost(tour)

if __name__ == "__main__":
    print("All possible tours starting from city A:")
    tour, cost = brute_force()
    print("\nBrute force (optimal) tour:", " -> ".join(cities[c] for c in tour))
    print("Minimum cost              :", cost)
    nn_tour, nn_cost = nearest_neighbour()
    print("\nNearest neighbour tour    :", " -> ".join(cities[c] for c in nn_tour))
    print("Nearest neighbour cost    :", nn_cost)
