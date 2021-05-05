% Geographic Information Systems for Public Policy - Lecture VIII
% Creating Maps
%[Sergio Rey](http://sergrey.org)


## Last Time
![100-globe](./images/06/100-globe.jpg)


- Midterm Exam

## Today
![100-globe](./images/06/100-globe.jpg)


<ul>
<li class="fragment"> Working with Vector Data </li>
<li class="fragment"> Symbology</li>
<li class="fragment"> Classifying Vector Data</li>
<li class="fragment"> Color</li>
</ul>


#
## Working with Vector Data



## Shapefile
![800_rivers](./images/08/800_rivers.png)

## Geopackage

<ul>
<li class="fragment"> open format </li>
<li class="fragment"> multiple layers </li>
<li class="fragment"> different geometries </li>
<li class="fragment"> can contain vector and raster layers </li>
<li class="fragment"> different coordinate systems </li>
</ul>



## Geopackage
![810_geopackage](./images/08/810_geopackage.png)

## Geopackage: Roads
![815_geopackage_roads](./images/08/815_geopackage_roads.png)

## SQLite

## SQLite
![830_sqlite](./images/08/830_sqlite.png)

## SQLite Connection
![831_sqlite](./images/08/831_sqlite.png)

## SQLite Land Use
![832_sqlite](./images/08/832_sqlite.png)

#
## Symbology

## Color

![832101_color](./images/08/832101_color.png)


## Fill color
![842102_color](./images/08/842102_color.png)


## Symbol Structure

## Stroke
![832300_stroke](./images/08/832300_stroke.png)


## No pen
![832301_nonpen](./images/08/832301_nonpen.png)


## Scale-based visibility

## Buildings
![83251_scale](./images/08/83251_scale.png)


## Scale-based visibility
![83252_scale](./images/08/83252_scale.png)


## Scale-based visibility
![83253_scale](./images/08/83253_scale.png)



## Adding Symbol Layers and Ordering Symbol Levels

## Roads
![83280_roads_0](./images/08/83280_roads_0.png)


## Add Symbol Layer

![83281_roads](./images/08/83281_roads.png)

## Order Symbol Levels

##
![83282_roads](./images/08/83282_roads.png)



## Ordered Symbol Levels


![83283_roads](./images/08/83283_roads.png)




## Geometry generator symbology

## Water: Single Symbol
![83212_generator](./images/08/83212_generator.png)

## Water: To Centroid
![83212_generator_0](./images/08/83212_generator_0.png)


## Water: To Centroid
![83212_generator_1](./images/08/83212_generator_1.png)


## Water: 2 symbol layers
![83213_generator_2](./images/08/83213_generator_2.png)





#
## Classifying Vector Data

## Why Classification?

<ul>
<li class="fragment"> Summarizing the attribute value distribution </li>
<li class="fragment"> Representing the spatial distribution of attribute values </li>
</ul>


## Measurement Scales

<ul>
<li class="fragment"> Nominal: name-based, no order </li>
<li class="fragment"> Ordinal: arranged in order (ranks) </li>
<li class="fragment"> Interval: pos, neg, zero values (height above/below sea level)</li>
<li class="fragment"> Ratio: positive, zero values (distances, degrees Kelvin) </li>
</ul>



## Classifying Nominal Data

## SCAG Data: COUNTY

##
![8_000_nominal](./images/08/8_000_nominal.png)

##
![8_001_nominal](./images/08/8_001_nominal.png)




## Ratio/Interval Classification

## TOTPOP


##
![8_010_graduated](./images/08/8_010_graduated.png)

##
![8_011_graduated](./images/08/8_011_graduated.png)

## ACRES

##
![8_020_ei](./images/08/8_020_ei.png)

##
![8_021_ei](./images/08/8_021_ei.png)



## Extensive and Intensive Variables
<ul>
<li class="fragment"> AREA and TOTPOP are counts </li>
<li class="fragment"> Extensive variables </li>
<li class="fragment"> Geometry size correlated with values </li>
<li class="fragment"> Choropleths generally not appropriate for extensive variables </li>

</ul>

## Intensive Variables
<ul>
<li class="fragment"> Percentages, ratios, densities </li>
<li class="fragment"> Standardized by area (in some sense)</li>
<li class="fragment"> Geometry size not correlated with values </li>
<li class="fragment"> Choropleths appropriate for intensive variables </li>
</ul>


## pctHISP (Equal Interval)

##
![8_030_pcthispei](./images/08/8_030_pcthispei.png)

##
![8_031_pcthispei](./images/08/8_031_pcthispei.png)



## pctHISP (LA Equal Interval)

##
![8_032_pcthisei_zoom](./images/08/8_032_pcthisei_zoom.png)



## pctHISP (LA Quantiles: 5)

##
![8_040_pcthispq5la](./images/08/8_040_pcthispq5la.png)

##
![8_041_pcthispq5la](./images/08/8_041_pcthispq5la.png)


## pctHISP (LA Jenks: 5)

##
![8_050_j](./images/08/8_050_j.png)

##
![8_051_j](./images/08/8_051_j.png)



## pctHISP (LA Standard Deviation)

##
![8_060_std](./images/08/8_060_std.png)

##
![8_061_std](./images/08/8_061_std.png)


## pctHISP (LA Pretty Breaks)

##
![8_070_pb](./images/08/8_070_pb.png)

##
![8_071_pb](./images/08/8_071_pb.png)


## [mapclassify](https://github.com/pysal/mapclassify)  
![08_080_mapclassify](./images/08/08_080_mapclassify.png)







#
## Color 

## ColorBrewer
![08_090_cb](./images/08/08_090_cb.png)


## ColorBrewer in QGIS
![8700_cb_ramp](./images/08/8700_cb_ramp.png)



## Next Up
- Creating Vector Data




#
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">GIS for Public Policy'20</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="http://sergerey.org" property="cc:attributionName" rel="cc:attributionURL">Sergio Rey</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.


