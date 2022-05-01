# Gridded Data

Lessons on working with data on a grid.

We are going to call data in this section "gridded". Very raw low-level remote sensing data may not be truly gridded, because sensor points may overlap. However, we are still going to use this word to broadely emcompass, "data that is representing an x and y plane in space".

We may also call this group "raster data". Raster data is usually considered to be equidistant grids, so that you don't have to store information about every single latitude and longitude. The data in this module is not going to assume that the points on the grid are equidistant. More rastser-specific resources can be found in the Additional Lectures section.

I have used the definintion that rasters have equally spaced grid points, so the spatial locations of each value don't need to be stored.

I installed dask to use the `open_mfdataset()` function -- add it to the `environment.yml`.
