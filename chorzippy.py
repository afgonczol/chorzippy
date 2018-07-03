# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 2018

@author: Allen Gonczol
"""

import geopandas as gp
import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import filedialog, Tk, messagebox, simpledialog, Button, Label, OptionMenu, StringVar, Message


def main(zip_column, data_column, leg_var, plot_size, cmap):
    print(zip_column, data_column, leg_var, plot_size, cmap)
    leg_var = leg_var == 'True' #Convert text to boolean. Used text originally so that button would appear normal (as opposed to 0 or 1)
    #limit to csv and excel files
    ftypes = [("CSV file", "*.csv"), ("Excel File", "*.xlsx")]
    zip_path = filedialog.askopenfilename(title='Open geographic zip code file')
    
    df_path = filedialog.askopenfilename(filetypes=ftypes, title='Open file with data that you want to plot.')

    #Read in file
    dfzip = gp.read_file(zip_path)
    if df_path[-3:] == 'csv':
        df = pd.read_csv(df_path)
    elif df_path[-4:] == 'xlsx':
        df = pd.read_excel(df_path)
    else:
        raise Exception('Must choose either a .csv or a .xlsx file.')
    
    #Make sure zip is string so that it can be merged with json file
    df[zip_column] = df[zip_column].map(str)
        
#    zip_column = simpledialog.askstring("Zip Column", "Enter the name of the column with the zip codes")
#    data_column = simpledialog.askstring("Zip Column", "Enter the name of the column with the data you want plotted")
    print(df.dtypes)
    print(dfzip.dtypes)
    
    mzip = pd.merge(dfzip, df, left_on='ZCTA5CE10', right_on=zip_column)
    print(mzip.shape)
    print(mzip.columns)
    
    figsize = plt.rcParams["figure.figsize"]
    figsize[0] = plot_size
    figsize[1] = plot_size
    
    try:
        mzip.plot(column=data_column, cmap=cmap, legend=bool(leg_var))
#        plot.show()
    except Exception as e:
        print(e)
        root.destroy()
    
    root.destroy()



def my_function():
    zip_column = zc_entry.get()
    data_column = dc_entry.get()
    leg_var = legend_var.get()
    plot_size = int(ps_entry.get())
    cmap = cmap_var.get()
    print(zip_column, data_column, leg_var)
    main(zip_column, data_column, leg_var, plot_size, cmap)
    #do stuff with url_member

def help_func():
    helproot = Tk()
    sb = tk.Scrollbar(helproot)
    sb.pack(side=tk.RIGHT, fill=tk.Y)
    
    help_text =  """First create an Excel or csv file that has a columnfor 5 digit zip 
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

For additional information and latest updates, visit my github page 
for this program at:
https://github.com/afgonczol/chorzippy
"""

    help_message = tk.Text(helproot, height=20, width=70)
    help_message.insert(tk.END, help_text)
    help_message.pack()
    sb.config(command=help_message.yview)
    help_message.config(yscrollcommand=sb.set)
    helproot.mainloop()


root = Tk()
root.title('chorzippy Parameters')
#root.withdraw()


zip_column_label = tk.Label(root, text = "Column Name for zip code ")
zip_column_label.grid(row = 0, column = 0)
zc_entry = tk.Entry(root)
zc_entry.insert(0, 'ZIP code column')
zc_entry.grid(row = 0, column = 1)

data_column_label = tk.Label(root, text = "Column Name for data to be plotted")
data_column_label.grid(row = 1, column = 0)
dc_entry = tk.Entry(root)
dc_entry.insert(0, 'Data column')
dc_entry.grid(row = 1, column = 1)

plot_size_label = tk.Label(root, text = "Size of plot")
plot_size_label.grid(row = 2, column = 0)
ps_entry = tk.Entry(root)
ps_entry.insert(0, 16)
ps_entry.grid(row = 2, column = 1)

legend_label = tk.Label(root, text = "Include legend")
legend_label.grid(row = 3, column = 0)
legend_var = StringVar(root)
legend_var.set('False')
legend_option = OptionMenu(root, legend_var, 'False', 'True')
legend_option.grid(row = 3, column = 1)

cmap_label = tk.Label(root, text = "Color map")
cmap_label.grid(row = 4, column = 0)
cmap_var = StringVar(root)
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
cmap_var.set('RdYlGn')
cmap_option = OptionMenu(root, cmap_var, *cmap_options)
cmap_option.grid(row = 4, column = 1)



my_button = tk.Button(root, text = "Submit", command = my_function)
my_button.grid(row = 10, column = 0)

help_button = tk.Button(root, text = "Help", command = help_func)
help_button.grid(row = 10, column = 1)


root.mainloop()





