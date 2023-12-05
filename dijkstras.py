import networkx as nx
import matplotlib.pyplot as plt
import heapq
import argparse

from networkx import Graph
from locations import Locations

def dijkstras(graph: Graph, start: str) -> list[str]:
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
        graph (Graph): Input graph from NetworkX library that contains edges and vertices, mimicking the actual graph data structure. Implemented using an
        adjacency list.
    Returns:
        None
    """
    pos = nx.spring_layout(graph)
    nx.draw(graph, pos, with_labels=True, font_weight='bold')
    labels = nx.get_edge_attributes(graph, 'weight')
    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)
    plt.show()

def init_parser() -> argparse.ArgumentParser:
    """Initializes an argument parser so that the user can provide Command Line arguments to configure the program how they choose.

    Args:
        None
    Returns:
        ArgumentParser: parser object to be used for taking in CLI args.
    """
    parser = argparse.ArgumentParser(description="Options for choosing which restaurants to add")
    parser.add_argument('-debug', action='store_true', help='Activate Debug Mode to see relationships between all Nodes and Edges.')

    mutually_exclusive_group = parser.add_mutually_exclusive_group(required=True)
    mutually_exclusive_group.add_argument('--nearest', action='store_true', help='Set mode to find overall nearest restaurant out of all available on the map.')
    mutually_exclusive_group.add_argument('--choose', type=str, help='Set mode to find shortest path to a specific given restaurant by the user.')

    parser.add_argument('-c', action='store_true', help='Include Chipotle')
    parser.add_argument('-w', action='store_true', help='Include Willys')
    parser.add_argument('-m', action='store_true', help='Include Moes')

    return parser

def handle_locations(args, edges: list[dict], locations:list[str]) -> tuple:
    """Handles all processing of which locations to add to the list based on what the user provides in the CLI. 

    Args:
        args: argument list to process.
        edges (list[dict]): empty list
        locations (list[str]): empty list

    Returns:
        tuple: Returns a tuple of (edges, locations) to be unpacked by the caller, where both elements are lists.
    """
    #Chipotle
    if args.c:
        locations.extend(Locations.chipotle_locations)
        edges.extend(Locations.chipotle_edges)

    # WILLYS
    if args.w:
        locations.extend(Locations.moes_locations)
        edges.extend(Locations.moes_edges)
        
     #MOES
    if args.m:
        locations.extend(Locations.willys_locations)
        edges.extend(Locations.willys_edges)
    
    # All locations;
    if not args.m and not args.c and not args.w:   
        locations.extend(Locations.all_locations)
        edges.extend(Locations.all_edges)

    return (edges, locations)


def main():
    parser = init_parser()
    args = parser.parse_args()    # New list of locations

    edges_to_include = []
    locations_to_include = []

    handle_locations(args, edges_to_include, locations_to_include)

    locations_to_include.append(Locations.gsu)

    graph = Graph()
    graph.add_nodes_from(locations_to_include)
    graph.add_edges_from(edges_to_include)

    # Visualize the new graph
    visualize_graph(graph)
    start_location = Locations.gsu

    distances = dijkstras(graph, start_location)

    if args.nearest:
        # Find the nearest overall location on the graph.
        nearest_location = min(distances, key=distances.get)
        distance_to_nearest_location = distances[nearest_location]

        print(f"The nearest location {nearest_location} is located at the following address: {Locations.locations_with_addresses[nearest_location]}.")
        print(f"The distance from {start_location} to the nearest location is {distance_to_nearest_location} 'miles'.")

    elif args.choose:
        # Find shortest path to any given restaurant.
        print(f"The shortest path to get to {args.choose} is {distances[args.choose]} 'miles'.")

    # Debugging only, prints all shortest paths to see if the algorithm is correct
    if args.debug:
        print(f"The shortest path from GSU-DOWNTOWN to each of the following nodes:")
        for location, distance in distances.items():
            print(f"\t{location}: {distance} 'miles'.")

if __name__ == "__main__":
    main()
