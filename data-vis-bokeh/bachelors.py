# Plots data from the bachelors.csv file showing the percentage of bachelor's degree awardees who are female

import pandas
from bokeh.plotting import figure
from bokeh.io import output_file, show

# Read data using pandas and get information from dictionary
df = pandas.read_csv("bachelors.csv")
# df = pandas.read_csv("http://pythonhow.com/data/bachelors.csv")
y_data = df["Computer Science"]
x_data = df["Year"]

# Generate the html file
output_file("bachelors.html")

# Create a blank figure for the file
f1 = figure()

# Add a line plot to the figure
f1.line(x_data, y_data)

# Show the html page
show(f1)
