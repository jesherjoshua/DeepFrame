import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

# Read data from the text file
data = np.loadtxt("./logs/intensity/logs.txt", delimiter=",")

# Extract latitude, longitude, and intensity
latitude = data[:, 0]
longitude = data[:, 1]
intensity = data[:, 2]

# Create a figure and axis
fig = plt.figure(figsize=(10, 6))
ax = plt.axes(projection=ccrs.PlateCarree())

# Plot the heatmap
heatmap = ax.scatter(
    longitude, latitude, c=intensity, cmap="YlOrRd", s=30, transform=ccrs.PlateCarree()
)

# Add colorbar
cbar = plt.colorbar(heatmap, orientation="vertical")
cbar.set_label("Intensity")

# Add map features
ax.coastlines()
ax.set_global()

# Set plot title
plt.title("Heatmap of Intensity Data")

# Show the plot
plt.savefig("./plots/intensityplot.png")
plt.show()
