from bokeh.plotting import figure
from bokeh.io import output_file, show

# Make a basic Bokeh line graph

# Your lists must have the same length
x_data = [1, 2, 3, 4, 5]
y_data = [3, 5, 6, 8, 9]

# Prepare the html file
output_file("basicline.html")

# Create a blank figure for the file
f1 = figure()

# Add a line plot to the figure
f1.line(x_data, y_data)

# Make it show up
show(f1)
