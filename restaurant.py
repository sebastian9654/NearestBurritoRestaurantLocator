import networkx as nx
import matplotlib.pyplot as plt
import heapq
import argparse

from dataclasses import dataclass

def dijkstra(graph, start) -> list[str]:
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


@dataclass
class Locations:
    chipotle_edges = [
        ('GSU-DOWNTOWN', 'C-1', {'weight': 6}),
        ('GSU-DOWNTOWN', 'C-3', {'weight': 10}),
        ('C-1', 'C-2', {'weight': 22}),
        ('C-1', 'C-3', {'weight': 4}),
        ('C-2', 'C-4', {'weight': 52}),
        ('C-3', 'C-4', {'weight': 21}),
        ('C-1', 'C-4', {'weight': 50}),
    ]

    willys_edges = [
        ('W-1', 'GSU-DOWNTOWN', {'weight': 10}),
        ('W-1', 'W-2', {'weight': 10}),
        ('W-2', 'GSU-DOWNTOWN', {'weight': 10}),
        ('W-3', 'W-2', {'weight': 14}),
    ]

    moes_edges = [
        ('M-1','GSU-DOWNTOWN', {'weight': 10}),
        ('M-2', 'M-1', {'weight': 24}),
        ('M-2', 'GSU-DOWNTOWN', {'weight': 24}),
    ]

    all_edges = chipotle_edges + willys_edges + moes_edges

    chipotle_locations = ['C-1', 'C-2', 'C-3', 'C-4',] 
    willys_locations = ['W-1', 'W-2', 'W-3']
    moes_locations = ['M-1', 'M-2']

    all_locations = chipotle_locations + willys_locations + moes_locations

    # New dictionary mapping locations to addresses
    locations_with_addresses = {
        'C-1': 'Ashford Dunwoody Road',
        'C-2': 'Chamblee Dunwoody Road',
        'C-3': 'Buford Highway',
        'C-4': 'Perimeter Mall',

        'W-1' : 'Roswell Road',
        'W-2' : 'Hammond Drive',
        'W-3' : 'Chamblee Tucker Blvd',

        'M-1' : 'Northridge Road',
        'M-2' : 'Dunwoody Village',
    }


def visualize_graph(graph):
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
