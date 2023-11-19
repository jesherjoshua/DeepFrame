"""
Author: Jesher Joshua M
Email: jesherjoshua.m2021@vitstudent.ac.in

Description:
This script generates synthetic geographical locations and logs them based on specified criteria.
It utilizes a random location generator to create latitude and longitude pairs, which are then checked
against predefined geographical regions.

Libraries Used:
- Faker (for random data generation)
- NumPy

Note: Ensure the required libraries are installed using pip install [library_name].
"""

from faker import Faker
import numpy as np

def location_within_defined_regions(latitude, longitude):
    """
    Check if the given latitude and longitude coordinates fall within predefined geographical regions.

    Args:
        latitude (float): Latitude coordinate.
        longitude (float): Longitude coordinate.

    Returns:
        bool: True if the coordinates are within predefined regions, False otherwise.
    """
    if (-145 < latitude < -50) and (10 < longitude < 80):  # North America
        return True
    elif (-85 < latitude < -32) and (-58 < longitude < 15):  # South America
        return True
    elif (-18 < latitude < 52) and (-36 < longitude < 39):  # Africa
        return True
    elif (-72 < latitude < -16) and (58 < longitude < 84):  # Greenland
        return True
    elif (-9 < latitude < 145) and (5 < longitude < 77):  # Asia & Europe
        return True
    elif (112 < latitude < 155) and (-41 > longitude > -2):  # Australia
        return True
    elif (-180 < latitude < 180) and (-90 < longitude < -65):  # Antarctica
        return True
    # Misc
    elif (137 < latitude < 180) and (49 < longitude < 71):
        return True
    else:
        return False

def generate_synthetic_location(value=0, mode='intensity'):
    """
    Generate synthetic geographical locations and log them based on specified criteria.

    Args:
        value (int): Value to be logged.
        mode (str): Mode of logging, e.g., 'intensity'.

    Returns:
        None
    """
    faker = Faker()
    longitude, latitude = faker.latlng()
    depth = np.random.randint(0, 100)

    while location_within_defined_regions(latitude, longitude):
        longitude, latitude = faker.latlng()

    print(f'Latitude: {latitude}, Longitude: {longitude}, {mode}: {value}')

    # Log the generated location
    with open(f'./logs/{mode}/logs.txt', 'a') as file_handle:
        file_handle.write(f'{latitude},{longitude},{value},{depth}\n')
