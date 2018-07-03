# chorzippy
Simple Program for Creating Choropleth Maps

First create an Excel or csv file that has a columnfor 5 digit zip 
codes and a column with the data you want to graph.
The top row should be the column names. If using Excel, the first sheet should have 
the data you want to graph.

It is a good idea to have the zip codes formatted as strings so that 
no leading zeroes fall off.

Make sure you have the zip code geojson file for the state you want 
to plot.
A file for each state can be found at the following link.
https://github.com/OpenDataDE/State-zip-code-GeoJSON

Enter the parameters into the parameters screen.
For a visual example of the color map options, visit the 
following site:
https://matplotlib.org/examples/color/colormaps_reference.html

Click 'Submit'
Navigate to and select the geojson file.
Navigate to and select your file with the zip codes and values you 
want graphed.
Note that it will take a few moments to create the choropleth.
