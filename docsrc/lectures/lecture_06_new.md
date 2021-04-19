% Geographic Information Systems for Public Policy - Lecture VI
% Coordinate Reference Systems
%[Sergio Rey](http://sergrey.org)


## Last Time
![100-globe](./images/06/100-globe.jpg)


- Rasters


## Today
![100-globe](./images/06/100-globe.jpg)


-   Coordinate Reference Systems
-   Map Projections

#
## Coordinate Reference Systems
![100-globe](./images/06/100-globe.jpg)

## Earth
![earth](./images/06/earth.jpg)


- Equatorial circumference: 24,901 miles (40,075 km)
- Meridional circumference: 24,860 miles (40,008 km)

## Earth

- Equatorial circumference: 24,901 miles (40,075 km)
- Meridional circumference: 24,860 miles (40,008 km)


## 
![mapmaker](./images/06/mapmaker.png)


## 
![map_projection](./images/06/map_projection.jpg)



## Coordinate Reference Systems

- Geographic Coordinate Systems
- Projected Coordinate Systems


## Geographic Coordinate System

##
![geographic_crs](./images/06/geographic_crs.png)

## Geographic Coordinate System

- lines of latitude
  - parallel to the equator
  - 180 equally spaced sections from North to South
  - each hemisphere divided into ninety sections (0-90 degrees)
- lines of longitude
  - perpendicular to the equator
  - converge at the poles
  - 0-180 E(+) or W(-) of prime Meridian 

## Why Math in GIS?
![coordinate_precision](https://imgs.xkcd.com/comics/coordinate_precision.png)




## Projected Coordinate Systems

##
![projected_crs](./images/06/projected_crs.png)



## Universal Transverse Mercator (UTM)

- Global _map projection_
- 60 equal zones of 6 degrees of longitude (1-60)


##
![utm_zones](./images/06/utm_zones.png)

##
![eastings](./images/06/eastings.png)

##
![utm_for_sa](./images/06/utm_for_sa.png)



## UTM

- northing (Y) value
  - distance from equator in meters
- easting (X) value
  - distance from zone central meridian
  
  
## Coordinates for Point of interest

- UTM Zone 35S
- 35 415,000 m E/ 6,540,000 m N
- Coordinates from the point of origin of the zone
  - intersection of equator and zone central meridian
- Southern Hemisphere: northings decrease to the south

## UTM: northing (Y)

- Place of interest: 3,550,000 meters south of the equator
- northing (Y): -3,550,00000
- Add false northing of 10,000,000
- 6,450,000m

## UTM: easting (X)
- Central meridian for UTM Zone 35s: 27 degrees easting
- Place of interest is 85,000 meters West of this
- -85,000m
- False easting of 500,000m
- easting (X): 415,000





#
## Map Projections

## 
![map_projection](./images/06/map_projection.jpg)

## Map Projection Characteristics

- Class
- Case
- Aspect

## Class 
![class](./images/06/class.png)

## Case
![projection](./images/06/projection.gif)

## Aspect: Projection's Center

- equatorial: centered somewhere along equator
- polar: centered about one of the poles
- oblique: between poles and equator 


## Accuracy of Map Projections

- Angular distortion
- Distance distortion
- Area distortion

## Angular Conformity: Mercator

- maintain 90 degrees for compaass rose (N,S,E,W)
- difficult for large areas
- only used for small portions of earth surface
- distorts area
- uses: navigation and meterological tasks

##
![mercator_projection](./images/06/mercator_projection.png)


## Equal Distance: Plate Carree Equidistant Cylindrical

- scale of the map is kept constant
- accurate distances from the center of projection to any other place
- accurate along given lines
- uses: radio and seismic mapping

##
![plate_carree_projection](./images/06/plate_carree_projection.png)


## Equal Area: Mollweide Equal Area Cylindrical

- preserves proportional relationships of mapped areas to areas on the Earth
- uses: when area needs to be measured (density, deforestation) 
- distortions of angular conformity

##
![mollweide_equal_area_projection](./images/06/mollweide_equal_area_projection.png)


## Map Projections

- Each map projection has advantages and disadvantages
- The best projection for a map depends on the scale of the map, and on the purposes for which it will be used.
- A projection may have unacceptable distortions if used to map the entire African continent, but may be an excellent choice for a large-scale (detailed) map of your country.



## On-The-Fly Projection

- Project starts with a given CRS
- Subsequently loaded layers get projected to that CRS
- Allows overlays of layers with different CRSs


## Next Up
- Map Production

#
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">GIS for Public Policy'20</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="http://sergerey.org" property="cc:attributionName" rel="cc:attributionURL">Sergio Rey</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.


