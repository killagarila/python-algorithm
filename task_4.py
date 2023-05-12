# imports 
import csv
import heapq


fp = 'dataset/task1_4_railway_network.csv'  # CSV Path


# Sorting Algorithms

def csv_to_graph(file_path):
    graph = {}
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            start = row[0].lower()
            end = row[1].lower()
            cost = float(row[2])
            if start not in graph:
                graph[start] = {}
            if end not in graph:
                graph[end] = {}
            graph[start][end] = cost
            graph[end][start] = cost
    return graph


def dijkstra(graph, start):
    costs = {node: float('inf') for node in graph}
    costs[start] = 0
    heap = [(0, start)]
    while heap:
        current_cost, current_node = heapq.heappop(heap)
        if current_cost > costs[current_node]:
            continue
        neighbors = graph[current_node]
        for neighbor in neighbors:
            cost = neighbors[neighbor]
            new_cost = current_cost + cost
            if new_cost < costs[neighbor]:
                costs[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))
    return costs


def shortest_path(graph, start, end):
    costs = dijkstra(graph, start)
    if costs[end] == float('inf'):
        return [], float('inf')
    path = [end]
    current_node = end
    while current_node != start:
        neighbors = graph[current_node]
        for neighbor in neighbors:
            cost = neighbors[neighbor]
            if costs[current_node] == costs[neighbor] + cost:
                path.append(neighbor)
                current_node = neighbor
                break
    return path[::-1], costs[end]

def main():
    g = csv_to_graph(fp)
    cities = []
    with open(fp,'r') as f:
        read = csv.reader(f)
        for row in read:
            if row[0] not in cities:
                cities.append(row[0])
    # print(*cities, sep = "\n") # PRINT LIST OF ALL CITIES
    start = input("Starting City: ").lower()
    end = input("Destination City: ").lower()
    path,cost = shortest_path(g, start, end)
    if shortest_path:
        print(f"Shortest path from {start} to {end}: {' -> '.join(path)} \nWith a cost of: £{cost}")
    else:
        print("No path found between the given locations.")

if __name__ == "__main__":
    main()