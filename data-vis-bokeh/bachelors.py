# Plots data from the bachelors.csv file showing the percentage of bachelor's degree awardees who are female

import pandas
from bokeh.plotting import figure
from bokeh.io import output_file, show

field = "Computer Science"

# Read data using pandas and get information from dictionary
df = pandas.read_csv("bachelors.csv")
# df = pandas.read_csv("http://pythonhow.com/data/bachelors.csv")
y_data = df[field]
x_data = df["Year"]

# Generate the html file
output_file("bachelors.html")

# Create a blank figure for the file
f1 = figure(plot_width=500, plot_height=400, tools="pan,reset")

f1.title.text = "Percentage of " + field + " Degrees Earned by Women vs. Time"
f1.title.text_color = "Gray"
f1.title.text_font = "times"
f1.title.text_font_style = "bold"

f1.xaxis.minor_tick_line_color = None
f1.yaxis.minor_tick_line_color = None

f1.xaxis.axis_label = "Year"
f1.yaxis.axis_label = "Percentage of Degrees Obtained by Women"

# Add a line plot to the figure
f1.line(x_data, y_data)

# Show the html page
show(f1)
