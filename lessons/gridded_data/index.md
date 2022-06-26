# Gridded Data

Lessons on working with multidimensional array data. A description of the two data tracks used on this website can be found on the [homepage](../../index.md).

## Semantics: Gridded vs. Raster Data
We are going to call data in this section "gridded". This means that the data can be stored in a multidimenaional array, but it makes no assumption about how the array cells are organized in space. Raw low-level remote sensing data may not be truly gridded, because sensor points may overlap. However, we are still going to use this word to broadely emcompass, "data that is representing an x and y plane in space".

In the past I have called this group "raster data", which is often used to refer to higher level satellite data. I think the term "raster" differs from the term "gridded" in that raster data is usually considered to be equidistant grids. This means that you don't have to store information about every single latitude and longitude, but it excludes data in certain projections. 

In the end I don't think there is a clear de facto standard for how to delineate between these overlapping data formats. In this website, general multi-dimensional data processing with `xarray` will be in this section, called Gridded Data. Raster-specific resources can be found in the Additional Lectures section, which uses `rasterio`.
