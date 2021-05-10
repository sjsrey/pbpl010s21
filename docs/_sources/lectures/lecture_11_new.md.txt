% Geographic Information Systems for Public Policy - Lecture XI
% Vector Analysis: Clipping, Dissolve, and Spatial Joins
%[Sergio Rey](http://sergrey.org)


## Last Time
![100-globe](./images/06/100-globe.jpg)

<ul>
<li class="fragment"> Deterministic Spatial Analysis</li>
<li class="fragment"> Buffers and Buffering</li>
<li class="fragment"> Select by Location</li>
<li class="fragment"> Health Deserts</li>
</ul>



## Today
![100-globe](./images/06/100-globe.jpg)


<ul>
<li class="fragment"> Clipping</li>
<li class="fragment"> Dissolve</li>
<li class="fragment"> Spatial Joins</li>
</ul>

#
## Motivation
![000_latimes](./images/11/000_latimes.png)


## Motivation


>More than 1.2 million people already live in high-pollution zones within 500 feet of a Southern California freeway, with more moving in every day. Between 2000 and 2010 — the most recent period available — the population within 500 feet of a Los Angeles freeway grew 3.9%, compared with a rate of 2.6% citywide.

[url](https://www.latimes.com/projects/la-me-freeway-pollution/)



## Replication for Riverside County

- goal is to detect which tracts intersect highway buffer
- estimate populations inside buffer
- (exercise 4)


## Data

- State highway layer
- Riverside County tracts

## Highway Layer [[url]](https://stacks.stanford.edu/file/druid:xc453kn9742/data.zip?download=true 
)
![100_tracts_highway](./images/11/100_tracts_highway.png)

##
![103_tracts_table](./images/11/103_tracts_table.png)


##
![105_tracts_info](./images/11/105_tracts_info.png)


#
## Clipping


## Highway Layer [[url]](https://stacks.stanford.edu/file/druid:xc453kn9742/data.zip?download=true 
)
![100_tracts_highway](./images/11/100_tracts_highway.png)

## Issue
- We don't need the entire state network
- Only segments in Riverside County
- Efficient: replicate for all counties
- Divide and conquer

## Clipping
- Need a layer that has the clipping polygon
- Apply to segment layer

## Clipping polygon
- Dissolve Riverside tracts

## Dissolve: Menu


##
![110_dissolve_menu](./images/11/110_dissolve_menu.png)


##
![120_dissolve_dialog](./images/11/120_dissolve_dialog.png)


##
![130_dissolve_results](./images/11/130_dissolve_results.png)



## Clipping

##
![200_clipping](./images/11/200_clipping.png)


##
![210_clip_menu](./images/11/210_clip_menu.png)


##
![220_clip_dialog](./images/11/220_clip_dialog.png)


##
![230_clip_results](./images/11/230_clip_results.png)

##
![240_clip_info](./images/11/240_clip_info.png)


#
## Spatial Joins

## Spatial Joins

- Add additional attributes to layer based on spatial relations with other layer
- e.g. assign tract poverty rate to houses in each tract (hedonic modeling)
- e.g. dummy variable for tracts intersecting road buffer

##
![300_spatial_joins](./images/11/300_spatial_joins.png)

##
![310_spatial_joins_results](./images/11/310_spatial_joins_results.png)

##
![320_spatial_joins_table](./images/11/320_spatial_joins_table.png)

##
![330_spatial_joins_table_all](./images/11/330_spatial_joins_table_all.png)

##
![340_spatial_joins_duplicates](./images/11/340_spatial_joins_duplicates.png)

## Segments and Tracts

- One tract can intersect more than one segment
- Not what we want

##  Fix: Buffer
- Buffer segments
- Creates polygons


##
![400_buffer_projection](./images/11/400_buffer_projection.png)




## Problem with CRS
##
![401_clipped_crs](./images/11/401_clipped_crs.png)
##
![401_tracts_crs](./images/11/401_tracts_crs.png)
##
![402_clinics_crs](./images/11/402_clinics_crs.png)



## Change CRS
##
![403_tracts_new_crs_dialog](./images/11/403_tracts_new_crs_dialog.png)


## Buffer Again
##
![420_buffer_menu](./images/11/420_buffer_menu.png)
##
![425_buffer_result](./images/11/425_buffer_result.png)
##
![426_buffer_count](./images/11/426_buffer_count.png)

## Remember Dissolve?
##
![450_buffer_dissolve](./images/11/450_buffer_dissolve.png)
##
![451_buffer_dissolve_one](./images/11/451_buffer_dissolve_one.png)
##
![452_table_join](./images/11/452_table_join.png)
##
![460_table_join_expression](./images/11/460_table_join_expression.png)
##
![465_table_join_result](./images/11/465_table_join_result.png)
##
![466_zoom](./images/11/466_zoom.png)




## Next Up
- OpenStreetMap






#
<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">GIS for Public Policy'20</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="http://sergerey.org" property="cc:attributionName" rel="cc:attributionURL">Sergio Rey</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.


