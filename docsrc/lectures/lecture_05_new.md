% Geographic Information Systems for Public Policy - Lecture V 
% Raster Data Models
%[Sergio Rey](http://sergrey.org)

## Last Time

- Vector Attributes
- Table Joins
- Virtual Layers

## Today

-   Raster Data Model
-   Conversions
-   Rasters in Public Policy/Social Sciences

#
## Raster Data Model

- Rasters composed of a matrix of pixels (cells)
- Each pixel contains a value representing the conditions for the area covered by that pixel

![100_raster](./images/05/100_raster.png)

##
![101_raster_neon](./images/05/101_raster_neon.png)




## Advantages of Rasters
- Representing *continuous* spatial variation
- More efficient than small polygons (in the vector model)
![110_raster_representation](./images/05/110_raster_representation.png)

## Georeferencing Rasters
- Defines the correspondence between each pixel and location on the earth's surface
- Coordinates of top left pixel in the images
- Size of each pixel in X and Y direction
- Rotation angle

## Raster in QGIS
![120_raster_qgis](./images/05/120_raster_qgis.png)

## Raster in QGIS
![121_raster_info](./images/05/121_raster_info.png)



## Sources of raster data

## Remote Sensing Satellites 
![211_rs](./images/05/211_rs.png)

## Remote Sensors
![201_rs_sensors](./images/05/201_rs_sensors.png)



## Planet
![213_planet](./images/05/213_planet.png)


## Earth Engine Timelapse

##
![212_earth_engine](./images/05/212_earth_engine.png)

['url'](https://earthengine.google.com/timelapse/)

## Remote Sensing Imagery Resolution

- Spatial Resolution
- Spectral Resolution
- Temporal Resultion

## Spatial Resolution

How much area is represented in each pixel

<ul>
<li class="fragment">MODIS 500m x 500m  </li>
<li class="fragment">SPOT5 satellites: 10m x 10m </li>
<li class="fragment">Areal Photography, drones: 50cm x 50cm  </li>
</ul>

<div class="fragment">
__Remember__: images with pixel size covering a _small area_ are called _high resolution_ images.
</div>

## Spatial Resolution and Scale

<table>
<col width="50%">
<col width="50%">
<tr>
<td>
<img src="../content/lectures/images/05/220_raster_small_scale.png" style="height:250px">
</td>
<td>
<img src="../content/lectures/images/05/221_raster_large_scale.png" style="height:250px">
</td>
</tr>
</table>



## Spectral Resolution

- The number of spectral bands in which a sensor can collect reflected radiance
- Choice depends upon application of use
- Different types of ground targets have different spectral signatures

![230_spectral_resolution](./images/05/230_spectral_resolution.png)

## Temporal Resolution

Revisit Periods for Satellites

<ul>
<li class="fragment">SPOT5 - 3 days  </li>
<li class="fragment"> Modis - daily </li>
<li class="fragment"> Airborne - as needed </li>
</ul>


#
## Conversions

## Which Model? 

![vector_vs_raster](./images/02/vector_vs_raster.jpg)


## Vector to raster conversion 
![240_vec2ras](./images/05/240_vec2ras.png)


## Raster to vector conversion
![241_ras2vec](./images/05/241_ras2vec.png)


#
## Rasters in GIS for Public Policy

- Measures of environmental variables
- Risk surfaces
- Dasymetric mapping and areal interpolation


## Environmental variables

[Freeman et al. (2017)](https://scholar.harvard.edu/files/freeman/files/willngess_to_pay_for_clean_air_in_china_ms-for-dash_freeman-laing-song-timmins_dec2017.pdf) "Willingness to pay for clean air in China"


![303_willingness](./images/05/303_willingness.png)



## FEMA: Risk Surface
![307_risk_flooding_raster](./images/05/307_risk_flooding_raster.png)



## Dasymetric Mapping
![301_dasymetric](./images/05/301_dasymetric.png)


## NSF-Neighborhoods
![309_nsf_neighborhoods](./images/05/309_nsf_neighborhoods.png)


##
![312_geosnap](./images/05/312_geosnap.png)



## Interpolation and Harmonization

##
![300_toy_census_tracts_example](./images/05/300_toy_census_tracts_example.png)



## Tobler

![304_areal_interpolation](./images/05/304_areal_interpolation.png)

## Tobler: Voting Precincts

![305_voting_precincts](./images/05/305_voting_precincts.png)

## Tobler: Dasymetric

![311_tobler_nlcd](./images/05/311_tobler_nlcd.png)



## National Land Cover Database
![111_nlcd_video](./images/05/111_nlcd_video.png)





## Next Up
- Coordinate Reference Systems

#
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">GIS for Public Policy'20</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="http://sergerey.org" property="cc:attributionName" rel="cc:attributionURL">Sergio Rey</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.

