# imports getting tested
import geopandas as gpd
import xarray as xr
import rasterio
import h5py
import netCDF4 as nc
# not tested: openpyxl
import seaborn as sns
from bokeh.plotting import figure
import cartopy.crs as ccrs

# additional imports that were needed
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import time
import os


# Geopandas
df = pd.DataFrame(
    {'City': ['Buenos Aires', 'Brasilia', 'Santiago', 'Bogota', 'Caracas'],
     'Country': ['Argentina', 'Brazil', 'Chile', 'Colombia', 'Venezuela'],
     'Latitude': [-34.58, -15.78, -33.45, 4.60, 10.48],
     'Longitude': [-58.66, -47.91, -70.66, -74.08, -66.86]})

gdf = gpd.GeoDataFrame(
    df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))

# xarray
ds = xr.Dataset(
    {"foo": (("x", "y"), np.random.rand(4, 5))},
    coords={
        "x": [10, 20, 30, 40],
        "y": [-80, -79, -78, -77, -76],
    }
)

ds.to_netcdf("testfile.nc")

# netcdf
with nc.Dataset("testfile.nc") as src:
    time.sleep(0.5)

# h5py
with h5py.File("testfile.hdf5", "w") as f:
    f.create_dataset("mydataset", (100,), dtype='i')

# rasterio
Z = np.random.rand(4, 5)
transform = (45, 10, 0, 1, 1, 0)
with rasterio.open('testfile.tif', 'w', driver='GTiff', height=Z.shape[0],
                   width=Z.shape[1], count=1, dtype=Z.dtype, crs='+proj=latlong',
                   transform=transform) as dst:
    dst.write(Z, 1)

# seaborn
sns.set_theme()
may_flights = sns.load_dataset("flights")
sns.lineplot(data=may_flights, x="year", y="passengers")

# bokeh
p = figure()
p.line([1, 2, 3], [4, 5, 6])

# cartopy
ax = plt.axes(projection=ccrs.PlateCarree())
ax.coastlines()

# remove test files
os.remove('testfile.nc')
os.remove('testfile.hdf5')
os.remove('testfile.tif')

print('Tests ran successfully! Here are a bunch of plots oddly stacked on top of each other:')
