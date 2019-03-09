from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas

# Make a basic Bokeh line graph

# Your lists must have the same length
df = pandas.read_csv("somedata.csv")
x_data = df["x"]
y_data = df["y"]

# Prepare the html file
output_file("basicline.html")

# Create a blank figure for the file
f1 = figure()

# Add a line plot to the figure
f1.line(x_data, y_data)

# Make it show up
show(f1)
