from dataclasses import dataclass

@dataclass
class Locations:
    """Data Class used to store all variables pertaining to this project such as the list of restaurants (edges and locations) each in their own list, list of 
    all of the locations and the address associated with them. Allows for quick and easy access to all important info.

    Attributes: 
        chipotle_edges: (list)

        willys_edges (list)

        moes_edges (list)

        all_edges (list)

        chipotle_locations (list)

        willys_locations (list)

        moes_locations (list)

        all_locations (list)

        locations_with_addresses (dictionary)
    """

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