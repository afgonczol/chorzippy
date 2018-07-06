# chorzippy
Simple Program for Creating Choropleth Maps
Includes GUI for simple parameter setting and loading of files.

Created and runs in Python 3, but can be converted to .EXE by
using pyinstaller.
Dependencies: geopandas, pandas, matplotlib, Gooey

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

Enter the parameters into the program.
For a visual example of the color map options, visit the 
following site:
https://matplotlib.org/examples/color/colormaps_reference.html

Note that it will take a few moments to create the choropleth.



