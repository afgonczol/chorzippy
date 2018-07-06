# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 2018

@author: Allen Gonczol
"""

import geopandas as gp
import pandas as pd
import matplotlib.pyplot as plt
from gooey import Gooey, GooeyParser


@Gooey
def main():
    
    #https://matplotlib.org/examples/color/colormaps_reference.html
    cmap_options = [
            'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
            'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
            'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn',
            'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
            'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
            'hot', 'afmhot', 'gist_heat', 'copper',
            'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
            'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic',
            'viridis', 'plasma', 'inferno', 'magma',
            'Pastel1', 'Pastel2', 'Paired', 'Accent',
            'Dark2', 'Set1', 'Set2', 'Set3',
            'tab10', 'tab20', 'tab20b', 'tab20c',
            'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
            'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg', 'hsv',
            'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar',
        ]
    
    #Get kwargs from GUI
    parser = GooeyParser(description="chorzippy")
    parser.add_argument('Filename', widget='FileChooser', help="Name of the file you want to process")
    parser.add_argument('Map File', widget='FileChooser', help="Name of the map file")
    
    parser.add_argument('Zip Column Name', help="Name of column in Filename with zip codes")
    parser.add_argument('Data Column Name', help="Name of column in Filename with data you want to plot")
    parser.add_argument('Figure Size', help="Figure Size", type=float, default=10)
    parser.add_argument('Legend', help='Include Legend', choices=['Yes', 'No'], default='Yes')
    parser.add_argument('Color Map', help='matplotlib.org/examples/color/colormaps_reference.html', choices=cmap_options, default='RdYlGn')
    parser.add_argument('Reverse Color Map', help='Reverse Color Map', choices=['Yes', 'No'], default='No')
    
    args = vars(parser.parse_args())
    print(args)
    

    #Read map file
    dfzip = gp.read_file(args['Map File'])
    
    #Read data file
    df_path = args['Filename']
    if df_path[-3:] == 'csv':
        df = pd.read_csv(df_path)
    elif df_path[-4:] == 'xlsx':
        df = pd.read_excel(df_path)
    else:
        raise Exception('Must choose either a .csv or a .xlsx file.')
    
    #Make sure zip is string so that it can be merged with json file
    zip_column = args['Zip Column Name']
    df[zip_column] = df[zip_column].map(str)
        
    #Inner join files on zip codes
    mzip = pd.merge(dfzip, df, left_on='ZCTA5CE10', right_on=zip_column)
    
    #Set size of choropleth
    figsize = plt.rcParams["figure.figsize"]
    figsize[0] = args['Figure Size']
    figsize[1] = args['Figure Size']
    
    #Get color map and potentially reverse
    cmap = args['Color Map']
    if args['Reverse Color Map'] == 'Yes':
        cmap += '_r'
    
    include_legend = True if args['Legend'] == 'Yes' else False
    
    #Plot the data onto the map
    try:
        mzip.plot(column=args['Data Column Name'], cmap=cmap, legend=include_legend)
        print("\n\n\nProgram will continue running until image is closed.\n\nDon't forget to save image if you like the results.")
        plt.show()
        
    except Exception as e:
        print(e)
        
        
if __name__ == '__main__':
    main()
    













