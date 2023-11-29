# Nearest Burrito Restaurant Locator

## Overview

This Python script utilizes Dijkstra's Algorithm to help you find the shortest path from your location to the nearest Chipotle, Willy's, or Moe's in the Atlanta Metropolitan Area. The script includes options to customize your search based on restaurant preferences and additional filtering criteria.

## Installation

1. Ensure you have Python installed on your system.
2. Clone the repository using the following command:

    ```bash session
    git clone https://github.com/sebastian9654/algoproject.git
    ```
3. Install the required libraries/dependencies using the following command(s):

    ```bash
    pip install -r requirements.txt   

    OR

    pip3 install -r requirements.txt    
    ```

## Usage
Run the script in your terminal or command prompt:

```bash
python dijkstras.py [options]
```

Options:

- **REQUIRED ARGUMENTS** 
    - --choose [restaurant] [other args] OR --nearest [other args]
        - Note: You must select ***one or the other*** arguments here. A list of all available restaurants along with their 'codes' is provided in this documentation.

- **OPTIONAL ARGUMENTS**
    - -c: Include Chipotle in the search.
    - -w: Include Willy's in the search.
    - -m: Include Moe's in the search.
        - Note: If none of the 3 above arguments are provided, the program will automatically include all 3 restaurants: Chipotle, Moe's and Willy's in the algorithm.

    - -debug: Activate '*Debug Mode*' to inspect shortest path from starting point to **all nodes**.

## List of Locations

When referencing the chip
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
[13:27] seb ~/Developer/proj % python3 dijkstras.py --nearest -debug
The nearest location C-3 is located at the following address: Buford Highway.
The distance from GSU-DOWNTOWN to the nearest location is 1 'miles'.

[DEBUG MODE] The shortest path from GSU-DOWNTOWN to C-1 is 5 'miles'.
[DEBUG MODE] The shortest path from GSU-DOWNTOWN to C-2 is 27 'miles'.
[DEBUG MODE] The shortest path from GSU-DOWNTOWN to C-3 is 1 'miles'.
[DEBUG MODE] The shortest path from GSU-DOWNTOWN to C-4 is 22 'miles'.
[DEBUG MODE] The shortest path from GSU-DOWNTOWN to W-1 is 10 'miles'.
[DEBUG MODE] The shortest path from GSU-DOWNTOWN to W-2 is 10 'miles'.
[DEBUG MODE] The shortest path from GSU-DOWNTOWN to W-3 is 24 'miles'.
[DEBUG MODE] The shortest path from GSU-DOWNTOWN to M-1 is 10 'miles'.
[DEBUG MODE] The shortest path from GSU-DOWNTOWN to M-2 is 24 'miles'.
[13:30] seb ~/Developer/proj % 
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

- The same command with additional argument -debug: `python3 dijkstras.py --choose C-1` will find the shortest path to get to location C-1 (Chipotle 1) from starting point GSU-DOWNTOWN. -debug will produce the same output as shown above in Example 1b.

```bash session
[13:37] seb ~/Developer/proj % python3 dijkstras.py --choose C-1 -debug
The shortest path to get to C-1 is 5 'miles'.

[DEBUG MODE] The shortest path from GSU-DOWNTOWN to C-1 is 5 'miles'.
[DEBUG MODE] The shortest path from GSU-DOWNTOWN to C-2 is 27 'miles'.
[DEBUG MODE] The shortest path from GSU-DOWNTOWN to C-3 is 1 'miles'.
[DEBUG MODE] The shortest path from GSU-DOWNTOWN to C-4 is 22 'miles'.
[DEBUG MODE] The shortest path from GSU-DOWNTOWN to W-1 is 10 'miles'.
[DEBUG MODE] The shortest path from GSU-DOWNTOWN to W-2 is 10 'miles'.
[DEBUG MODE] The shortest path from GSU-DOWNTOWN to W-3 is 24 'miles'.
[DEBUG MODE] The shortest path from GSU-DOWNTOWN to M-1 is 10 'miles'.
[DEBUG MODE] The shortest path from GSU-DOWNTOWN to M-2 is 24 'miles'.
[13:41] seb ~/Developer/proj % 
```
## Libraries Used

- NetworkX: (Version: 3.2.1) Used to represent and manipulate the graph.
- Matplotlib: (Version: 3.8.2) Used for graph visualization.

## Structure
The project utilizes a data class, Locations, to store information about restaurant edges, locations, and addresses. This allows for easy access to important data and quick modifications.