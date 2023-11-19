"""
Author: Jesher Joshua M
Email: jesherjoshua.m2021@vitstudent.ac.in

Description:
This script generates a heatmap plot based on geographical data, specifically latitude, longitude, intensity, and depth.
It uses Cartopy for map projections and visualization, and Matplotlib for plotting.

Libraries Used:
- NumPy
- Matplotlib
- Cartopy

Note: Ensure the required libraries are installed using pip install [library_name].
"""

import argparse
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

def generate_heatmap(mode='intensity'):
    """
    Generate a heatmap plot based on geographical data and save it as an image.

    Args:
        mode (str): Mode of plotting, e.g., 'intensity'.

    Returns:
        None
    """
    # Read data from the text file
    data = np.loadtxt(f"./logs/{mode}/logs.txt", delimiter=",")

    # Extract latitude, longitude, intensity, and depth
    latitude = data[:, 0]
    longitude = data[:, 1]
    intensity = data[:, 2]
    depth = data[:, 3]  # Add this line to extract depth data

    # Create a figure and axis
    fig = plt.figure(figsize=(10, 6))
    ax = plt.axes(projection=ccrs.PlateCarree())

    # Scale the size of circles based on intensity and depth
    size = 50 * intensity  # Adjust this scaling factor as needed
    depth_gradient = 1 - (depth / np.max(depth))  # Normalize depth for gradient

    print(f'size: {size}')
    print(f'depth_gradient: {depth_gradient}')

    # Plot the heatmap
    heatmap = ax.scatter(
        latitude, longitude, c=depth_gradient, cmap="Blues", s=size, alpha=0.7,
        transform=ccrs.PlateCarree(), edgecolors='k'
    )

    # Add colorbar
    cbar = plt.colorbar(heatmap, orientation="vertical")
    cbar.set_label(f"Depth Gradient")

    # Add land polygons and set their face color to black
    ax.add_feature(cfeature.LAND, facecolor='#c1272d')

    # Add map features
    ax.coastlines()
    ax.set_global()

    # Set plot title
    plt.title(f"Heatmap of {mode} Data")

    # Save the plot as an image
    plt.savefig(f"./plots/{mode}plot.png")

    # Show the plot
    plt.show()

# Example usage with 'intensity' mode
if __name__ == "__main__":
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="Generate a heatmap plot based on geographical data.")

    # Add an argument for the mode parameter
    parser.add_argument('--mode', type=str, default='intensity', help="Mode of plotting, e.g., 'intensity'.")

    # Parse the command line arguments
    args = parser.parse_args()

    # Call the generate_heatmap function with the specified mode
    generate_heatmap(mode=args.mode)