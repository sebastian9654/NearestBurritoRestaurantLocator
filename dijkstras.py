import networkx as nx
import matplotlib.pyplot as plt
import heapq
import argparse

from locations import Locations

def dijkstra(graph: nx.Graph, start: str) -> list[str]:
    """Dijkstra's Algorithm. Used to find shortest path within a graph from a start point.

    Args:
        graph (graph): Graph used to traverse and find shortest path
        start (str): Start Node

    Returns:
        list[str]: returns a list with the shortest paths
    """

    distance = {node: float('infinity') for node in graph}
    distance[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip if the current_node is the start node
        if current_distance > distance[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            if neighbor.startswith("GSU"):
                continue
            new_distance = distance[current_node] + weight['weight']
            if new_distance < distance[neighbor]:
                distance[neighbor] = new_distance
                heapq.heappush(priority_queue, (new_distance, neighbor))

    #removes the start variable so that start does not have a 0 distance to itself.
    del distance[start]

    return distance


def visualize_graph(graph) -> None:
    """Plots the graph using MatPlotLib library. 

    Args:
        graph (graph): Input graph from NetworkX library that contains edges and vertices, mimicking the actual graph data structure. Implemented using an
        adjacency list.
    Returns:
        None
    """
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, font_weight='bold')
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.show()


def main():
    parser = argparse.ArgumentParser(description="Options for choosing which restaurants to add")
    parser.add_argument('-all', action='store_true', help='Include all restaurants: chipotle, willys, and moes')
    parser.add_argument('-c', action='store_true', help='Include Chipotle')
    parser.add_argument('-w', action='store_true', help='Include Willys')
    parser.add_argument('-m', action='store_true', help='Include Moes')
    parser.add_argument('-debug', action='store_true', help='Activate Debug Mode to see relationships between all Nodes and Edges.')

    args = parser.parse_args()    # New list of locations

    edges_to_include = []
    locations_to_include = []

    if args.all:
        # Include all restaurants
        locations_to_include.extend(Locations.all_locations)
        edges_to_include.extend(Locations.all_edges)

    else:
        # Include selected restaurants based on arguments
        # CHIPOTLE
        if args.c:
            locations_to_include.extend(Locations.chipotle_locations)
            edges_to_include.extend(Locations.chipotle_edges)

        # WILLYS
        if args.w:
            locations_to_include.extend(Locations.moes_locations)
            edges_to_include.extend(Locations.moes_edges)
        
        #MOES
        if args.m:
            locations_to_include.extend(Locations.willys_locations)
            edges_to_include.extend(Locations.willys_edges)

    # New list of locations
    locations = locations_to_include + ['GSU-DOWNTOWN']

    graph = nx.Graph()
    graph.add_nodes_from(locations)
    graph.add_edges_from(edges_to_include)

    start_location = 'GSU-DOWNTOWN'

    # Visualize the new graph
    visualize_graph(graph)

    distances = dijkstra(graph, start_location)

    # Find the nearest location
    nearest_location = min(distances, key=distances.get)
    distance_to_nearest_location = distances[nearest_location]

    print(f"The nearest location {nearest_location} is located at the following address: {Locations.locations_with_addresses[nearest_location]}.")
    print(f"The distance from {start_location} to the nearest location is {distance_to_nearest_location} units.")

    # Debugging only, prints all distances to see if the algorithm is correct
    if args.debug:
        for location, distance in distances.items():
            print(f"[DEBUG MODE] The distance from {start_location} to {location} is {distance} units.")


if __name__ == "__main__":
    main()
