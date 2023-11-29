# Nearest Burrito Restaurant Locator

## Overview

This Python script utilizes Dijkstra's Algorithm to help you find the shortest path from your location to the nearest Chipotle, Willy's, or Moe's in the Atlanta Metropolitan Area. The script includes options to customize your search based on restaurant preferences and additional filtering criteria.

## Installation

1. Ensure you have Python installed on your system.
2. Install the required libraries using the following command:

    ```bash
    pip install networkx matplotlib
    ```

Clone the repository using the following link or download the script (dijkstras.py) and the locations.py file, and ensure you place them in the same directory.:

```bash session
git clone https://github.com/sebastian9654/algoproject.git
```

## Usage
Run the script in your terminal or command prompt:

```bash
python dijkstras.py [options]
```

Options:

- **REQUIRED ARGUMENTS** 
    - --choose [restaurant] [other args] OR --nearest [other args]
        - Note: You must select ***one or the other*** restaurants. A list of all available restaurants along with their 'codes' is provided in this documentation.

- **OPTIONAL ARGUMENTS**
    - -c: Include Chipotle in the search.
    - -w: Include Willy's in the search.
    - -m: Include Moe's in the search.
        - Note: If none of the 3 above arguments are provided, the program will automatically include all 3 restaurants: Chipotle, Moe's and Willy's in the algorithm.

    - -debug: Activate '*Debug Mode*' to inspect shortest path from starting point to **all nodes**.

## Examples

**1.**
```bash session

    [10:23] seb ~/Developer/proj % python3 dijkstras.py -all -debug

    The nearest location C-1 is located at the following address: Ashford       Dunwoody Road.
    The distance from GSU-DOWNTOWN to the nearest location is 6 units.
    [DEBUG MODE] The distance from GSU-DOWNTOWN to C-1 is 6 units.
    [DEBUG MODE] The distance from GSU-DOWNTOWN to C-2 is 28 units.
    [DEBUG MODE] The distance from GSU-DOWNTOWN to C-3 is 10 units.
    [DEBUG MODE] The distance from GSU-DOWNTOWN to C-4 is 31 units.
    [DEBUG MODE] The distance from GSU-DOWNTOWN to W-1 is 10 units.
    [DEBUG MODE] The distance from GSU-DOWNTOWN to W-2 is 10 units.
    [DEBUG MODE] The distance from GSU-DOWNTOWN to W-3 is 24 units.
    [DEBUG MODE] The distance from GSU-DOWNTOWN to M-1 is 10 units.
    [DEBUG MODE] The distance from GSU-DOWNTOWN to M-2 is 24 units.
    [10:24] seb ~/Developer/proj % 
    ```
This command will find the shortest path to the nearest Chipotle, Willy's, or Moe's from the predefined starting point.
```
**2.**
```bash session

    [10:27] seb ~/Developer/proj % python3 dijkstras.py -m -w
    The nearest location M-1 is located at the following address: Northridge Road.
    The distance from GSU-DOWNTOWN to the nearest location is 10 units.
    [10:27] seb ~/Developer/proj % 
```
## Libraries Used

- NetworkX: Used to represent and manipulate the graph.
- Matplotlib: Used for graph visualization.
Data Structure
The project utilizes a data class, Locations, to store information about restaurant edges, locations, and addresses. This allows for easy access to important data and quick modifications.