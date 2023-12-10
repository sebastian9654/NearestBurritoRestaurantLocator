# Nearest Burrito Restaurant Locator

## Overview
This project was for CSC 4520 - Design and Analysis of Algorithms. Fall 2023 Final Project.

This Python script utilizes Dijkstra's Algorithm to help you find the shortest path from your location to the nearest Chipotle, Willy's, or Moe's in the Atlanta Metropolitan Area. The script includes options to customize your search based on restaurant preferences and additional filtering criteria. When running the script, the user will be provided with 
a visual representation of the graph, thanks to the MatPlotLib python library. 

## Installation

1. Ensure you have Python installed on your system.
2. Clone the repository using the following command:

    ```bash session
    git clone https://github.com/sebastian9654/algoproject.git
    ```
3. Install the required libraries/dependencies using the following command(s):

    ```bash
    pip install networkx
    pip install matplotlib   

    OR

    ensure you are in `/NearestBurritoRestaurantLocator directory`
    pip install -r requirements.txt
    ```
    and ensure you are using the correct interpreter for these dependencies, if in VScode, select python interpreter in the botton right toolbar
    
## Usage
Run the script in your terminal or command prompt:

```bash
python dijkstras.py [options]

OR

python3 dijkstras.py [options]
```

Options:

- **REQUIRED ARGUMENTS** 
    - --choose [restaurant] [other args] OR --nearest [other args]
        - Note: You must select ***one or the other*** arguments here. A list of all available locations to choose from along with their 'codes' is provided in the next section.
        - Ensure you use the 'code' when providing a specific location (ex. W-1, M-2, C-4, etc...)
- **OPTIONAL ARGUMENTS**
    - -c: Include Chipotle in the search.
    - -w: Include Willy's in the search.
    - -m: Include Moe's in the search.
        - Note: If none of the 3 above arguments are provided, the program will automatically include all 3 restaurants: Chipotle, Moe's and Willy's in the algorithm.

    - -debug: Activate '*Debug Mode*' to inspect shortest path from starting point to **all nodes**.

## List of Locations

### Chipotle Locations
- **C-1**: Ashford Dunwoody Road
- **C-2**: Chamblee Dunwoody Road
- **C-3**: Buford Highway
- **C-4**: Perimeter Mall

### Willy's Locations
- **W-1**: Roswell Road
- **W-2**: Hammond Drive
- **W-3**: Chamblee Tucker Blvd

### Moe's Locations
- **M-1**: Northridge Road
- **M-2**: Dunwoody Village

## Examples
#### Finding the nearest *overall location* from Georgia State

**1a:** 
- The command `python3 dijkstras.py --nearest` will locate the nearest overall restaurant from our starting point: GSU-DOWNTOWN.

```bash title="python3"
[13:27] seb ~/Developer/proj % python3 dijkstras.py --nearest    
The nearest location C-3 is located at the following address: Buford Highway.
The distance from GSU-DOWNTOWN to the nearest location is 1 'miles'.
[13:27] seb ~/Developer/proj % 
```
**1b:** 
- The same command with additional argument -debug: `python3 dijkstras.py --nearest -debug` will locate the nearest overall restaurant from our starting point: GSU-DOWNTOWN. Along with a debug output of all locations and the shortest path to them.

```bash
PS C:\Users\Sebastian\Documents\Schoolwork\proj\NearestBurritoRestaurantLocator> python .\dijkstras.py --nearest -debug
The nearest location C-3 is located at the following address: Buford Highway.
The distance from GSU-DOWNTOWN to the nearest location is 5 'miles'.
The shortest path from GSU-DOWNTOWN to each of the following nodes: 
        C-1: 6 'miles'.
        C-2: 15 'miles'.
        C-3: 5 'miles'.
        C-4: 8 'miles'.
        W-1: 18 'miles'.
        W-2: 13 'miles'.
        W-3: 9 'miles'.
        M-1: 16 'miles'.
        M-2: 20 'miles'.
```
#### Finding the nearest *given location* from Georgia State.

**2a.**

- The command: `python3 dijkstras.py --choose C-1` will find the shortest path to get to location C-1 (Chipotle 1) from starting point GSU-DOWNTOWN.

```bash session
[13:30] seb ~/Developer/proj % python3 dijkstras.py --choose C-1    
The shortest path to get to C-1 is 5 'miles'.
[13:37] seb ~/Developer/proj % 
```

**2b.**

- The same command with additional argument -debug: `python3 dijkstras.py --choose C-1 -debug` will find the shortest path to get to location C-1 (Chipotle 1) from starting point GSU-DOWNTOWN. -debug will produce the same output as shown above in Example 1b.

```shell
PS C:\Users\Sebastian\Documents\Schoolwork\proj\NearestBurritoRestaurantLocator> python3 dijkstras.py --choose C-1 -debug
The shortest path to get to C-1 is 6 'miles'.
The shortest path from GSU-DOWNTOWN to each of the following nodes:
        C-1: 6 'miles'.
        C-2: 15 'miles'.
        C-3: 5 'miles'.
        C-4: 8 'miles'.
        W-1: 18 'miles'.
        W-2: 13 'miles'.
        W-3: 9 'miles'.
        M-1: 16 'miles'.
        M-2: 20 'miles'.
PS C:\Users\Sebastian\Documents\Schoolwork\proj\NearestBurritoRestaurantLocator> 
```
## Libraries Used

- NetworkX: (Version: 3.2.1) Used to represent and manipulate the graph.
- Matplotlib: (Version: 3.8.2) Used for graph visualization.

## Algorithm Details:
Time Complexity: O(V+E)
Space Complexity: O(V)

## Structure
The project utilizes a data class, Locations, to store information about restaurant edges, locations, and addresses. This allows for easy access to important data and quick modifications.

## TLDR

After cloning repo and installing required libraries for the project to function:

1. Run the script: `python3 dijkstras.py --nearest -debug` to see the nearest location from GSU 
and also see the shortest distance to all locations

2. Inspect the graph to see the edge weights and vertices.

or

1. Run the script: `python3 dijkstras.py --choose [location] to choose any location on in the list (located in list_of_restaurants.md)`

2. inspect the graph.
