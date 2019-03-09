from bokeh.plotting import figure
from bokeh.io import output_file, show
import random

# Make a plot with randomly-generated data
x_vals = range(100)
y_vals = []

# I'm genuinely surprised there's not a more pythonic way to do this
for i in range(100):
    y_vals.append(random.randint(1, 50))

# Create the html
output_file("random_circles.html")

# Create the blank figure
fig = figure()

# Add the circles
fig.circle(x_vals, y_vals)

# Show the graph
show(fig)
