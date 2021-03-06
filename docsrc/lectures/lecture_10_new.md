% Geographic Information Systems for Public Policy - Lecture X 
% Vector Analysis: Buffering
%[Sergio Rey](http://sergrey.org)


## Last Time
![100-globe](./images/06/100-globe.jpg)

<ul>
<li class="fragment"> Detecting Geometry Problems </li>
<li class="fragment"> Understanding Geometry Problems</li>
<li class="fragment"> Fixing Geometry Problems</li>
</ul>


## Today
![100-globe](./images/06/100-globe.jpg)


<ul>
<li class="fragment"> Deterministic Spatial Analysis</li>
<li class="fragment"> Buffers and Buffering</li>
<li class="fragment"> Select by Location</li>
<li class="fragment"> Health Deserts</li>
</ul>


#
## Deterministic Spatial Analysis


## Dimensions of vector geometries

<ul>
<li class="fragment"> Point: 0-dimension </li>
<li class="fragment"> Line: 1-dimensional (length) </li>
<li class="fragment"> Polygon: 2-dimensional (area) </li>
</ul>


## Spatial Relations
![TopologicSpatialRelarions2](./images/10/TopologicSpatialRelarions2.png)



## Dimensionally Extended nine-Intersection Mode (DE-9IM)
##
![DE-9IM](./images/10/DE-9IM.png)

[[url]](https://en.wikipedia.org/wiki/DE-9IM)


## Food Deserts [url](https://proceedings.esri.com/library/userconf/healthy-communities10/pdfs/mapping-food-deserts.pdf)
![000_food_desert](./images/10/000_food_desert.png)
[[url]](https://proceedings.esri.com/library/userconf/healthy-communities10/pdfs/mapping-food-deserts.pdf)

## Today: Clinic Deserts

##
![200_scag_riverside_select](./images/10/200_scag_riverside_select.png)


##
![210_riverside_tracts](./images/10/210_riverside_tracts.png)


##
![220_clinics](./images/10/220_clinics.png)


##
![221_clinics_table](./images/10/221_clinics_table.png)



#
## Buffers and Buffering


## Buffers
![300_buffers](./images/10/300_buffers.png)

## Buffers (Variable)
![310_buffers](./images/10/310_buffers.png)


## Buffers (Rings)
![320_buffers_rings](./images/10/320_buffers_rings.png)


## Buffers (Dissolve)
![330_buffers_dissolve](./images/10/330_buffers_dissolve.png)



## Buffering the Clinics
<ul>
<li class="fragment">food deserts: 0.5 mile distance  </li>
<li class="fragment">use for the clinic points </li>
<li class="fragment">will revisit other distances later </li>
</ul>



## .5 mile clinic buffer 
![400_buffer_menu](./images/10/400_buffer_menu.png)

##  buffer menu
![410_half_mile_menu](./images/10/410_half_mile_menu.png)


## buffer result
![411_result](./images/10/411_result.png)


## buffer result: geometry
![411_result_shape](./images/10/411_result_shape.png)


## buffer rename
![412_rename](./images/10/412_rename.png)




#
## Buffering

## Using the Buffers for Locational Analysis

<ul>
<li class="fragment"> Find what tracts intersect with the buffers </li>
<li class="fragment"> Create layer with these tracts </li>
<li class="fragment"> Use: Select by Location </li>
</ul>


## Processing: Select by Location
(Bring up Processing Toolbox with CTRL-ALT-T)
![500_select_by_location](./images/10/500_select_by_location.png)

## Processing: Select by Location Dialog
![510_sbl_dialog](./images/10/510_sbl_dialog.png)


## What tracts intersect with the .5 mile buffers?
![511_sbl_results](./images/10/511_sbl_results.png)


## Save Layer
![512_save_layer](./images/10/512_save_layer.png)


## Saved Layer
![513_layer_saved](./images/10/513_layer_saved.png)


#
## Health Deserts

## Traditional Approach
<ul>
<li class="fragment"> Tracts *not* intersecting buffers </li>
<li class="fragment"> Add up population in **desert polygons** </li>
</ul>

## Identifying Clinic Desert Tracts
![600_sbl_desert](./images/10/600_sbl_desert.png)


## Clinic Desert 
![610_desert_tracts](./images/10/610_desert_tracts.png)


## Clinic Desert  Layer
![611_desert_tracts_saved](./images/10/611_desert_tracts_saved.png)


## What is the population residing in Clinic Desert?

## Desert Tracts Tables
![700_totpop](./images/10/700_totpop.png)

## Basic Statistics for Fields
![705_stats_menu](./images/10/705_stats_menu.png)


## Basic Statistics for Fields: Dialog
![710_stats_menu](./images/10/710_stats_menu.png)


## Basic Statistics for Fields: Results
![711_stats_log](./images/10/711_stats_log.png)


## Basic Statistics for Fields: File
![711_stats_log_0](./images/10/711_stats_log_0.png)


## Basic Statistics for Fields: File
![712_stats_html](./images/10/712_stats_html.png)


## Total County Tract Population

![713_county_tract_population](./images/10/713_county_tract_population.png)

## Population Estimates

- County Total: 2,189,641 
- In Clinic Desert Tracts: 1,881,643 
- In Buffer Tracts: 307,998
- Population with access problems: 1,881,643




## Issues in measuring access to clinics

- all individuals in the tracts intersecting the buffers are in the buffer
- overestimation of people within .5 miles of a clinic
- underestimation of people in the clinic desert

## Why overestimation of buffer population?
![800_overestimation](./images/10/800_overestimation.png)



## We can do better

## Buffer Tracts
![810_buffer_tracts](./images/10/810_buffer_tracts.png)

## Random Points
![811_points_menu](./images/10/811_points_menu.png)


## Random Points Generated
![812_points_output](./images/10/812_points_output.png)


## Random Points Layer
![813_points_layer](./images/10/813_points_layer.png)

## Random Points Layer Symbology
![814_points_size](./images/10/814_points_size.png)


## Random Points Layer 
![815_point_density](./images/10/815_point_density.png)



## Count points in buffers: Layers 
![816_layers_on](./images/10/816_layers_on.png)


## Count points in buffers
![900_points_in_polygon](./images/10/900_points_in_polygon.png)


## Points in polygons
![910_points_output](./images/10/910_points_output.png)


## Count Field
![920_point_fields](./images/10/920_point_fields.png)


## Count Summary
![930_point_sum](./images/10/930_point_sum.png)


## Count Table
![940_counts_table](./images/10/940_counts_table.png)

## Revised Estimates
- County Total: 2,189,641 
- In Clinic Desert Tracts: 1,881,643 
- In Buffer Tracts: 307,998
  -  90,630 in buffer, in tract
  - 217,358 out of buffer, in tract
- Population with access problems: 2,099,011
- Population within .5 miles of clinic: 90,630





## Issue
- double counting
- points contained in more than a single buffer are counted more than once



## Overlapping Buffers
![950_overlapping_buffers](./images/10/950_overlapping_buffers.png)


## Count Table With Overlapping Buffers
![951_overlap_select](./images/10/951_overlap_select.png)



## Fix
- dissolve on buffering

## Buffer and Dissolve
![960_buffer_dissolve](./images/10/960_buffer_dissolve.png)

## Dissolved Buffer
![961_buffer_dissolved](./images/10/961_buffer_dissolved.png)



## New Buffer
![970_new_buffer](./images/10/970_new_buffer.png)


## New Buffer Feature Count
![971_feature_count](./images/10/971_feature_count.png)


## Points in Polygon Count
![972_points_in_polygons](./images/10/972_points_in_polygons.png)


## Population within .5 Miles of a Clinic
![990_final_count](./images/10/990_final_count.png)



## Revised Estimates
- County Total: 2,189,641 
- In Clinic Desert Tracts: 1,881,643 
- In Buffer Tracts: 307,998
  -  50,190 in buffer, in tract (no double counting)
  - 257,808 out of buffer, in tract
  
  
- Population with access problems: 2,139,451
- Population within .5 miles of clinic: 50,190







## Next Up
- Vector Analysis: Clipping and Spatial Joins






#
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">GIS for Public Policy'20</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="http://sergerey.org" property="cc:attributionName" rel="cc:attributionURL">Sergio Rey</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.


