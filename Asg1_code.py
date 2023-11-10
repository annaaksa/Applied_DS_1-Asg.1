# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 21:13:02 2023

@author: DELL
"""
#import the libraires matplotlib and pandas
import pandas as pd
import matplotlib.pyplot as plt

# Function to read the CSV file into a DataFrame
def read_data(file_path):
    data = pd.read_csv(file_path)
    return data

# Function to create a line graph

#define a functin for the line graph
def create_line_graph(data, x_col, y_cols, labels, title, x_label, y_label):
    plt.figure(figsize=(10, 6))

    for i, y_col in enumerate(y_cols):
    # Iterate over each y-axis column and plot the data
        plt.plot(data[x_col], data[y_col], label=labels[i], marker='o')
        
    #Labeling the graph
    
    plt.title(title) #set the title for graph
    plt.xlabel(x_label) #label the X axis
    plt.ylabel(y_label) #label the Y axis
    plt.legend() #show the legend for the labelling
    plt.grid(True) # Display in grid
    plt.show() #show the graph

# Function to create a bar chart

#define a functin for the bar graph
def create_bar_graph(data, x_col, y_col, title, x_label, y_label):
    plt.figure(figsize=(10, 6))
    plt.bar(data[x_col], data[y_col])
    
    #Labeling the graph
    plt.title(title) #set the title for graph
    plt.xlabel(x_label) #label the X axis
    plt.ylabel(y_label) #label the Y axis
    plt.show()#show the graph

# Function to create a scatter plot
def create_scatter_plot(data, x_col, y_cols, labels, title, x_label, y_label):
    plt.figure(figsize=(12, 8))

    for i, y_col in enumerate(y_cols):
        plt.scatter(data[x_col], data[y_col], label=labels[i], marker='o', s=50)
    #Labelling the graph
    plt.title(title) #set the title for graph
    plt.xlabel(x_label) #label the X axis
    plt.ylabel(y_label) #label the Y axis
    plt.legend() #show the legend for the labelling
    plt.grid(True) # Display in grid
    plt.show() #show the graph

if __name__ == "__main__":
    file_path = 'C:\\Users\\DELL\\Downloads\\health_insurance_coverage.csv'
    data = read_data(file_path)

    # Create a line graph for health insurance coverage
    create_line_graph(data, 'year', ['white', 'black', 'hispanic'], 
                     ['Whites in America', 'Blacks in America', 'Hispanics in America'],
                     'Health Insurance Coverage between Whites, Blacks, and Hispanics Over Time',
                     'Year', 'Health Coverage(ESI)')

    # Create a bar chart for health insurance coverage of white women
    create_bar_graph(data, 'year', 'white_women', 
                    'Bar graph of Public Health Insurance Coverage of White Women',
                    'Year', 'Health Insurance Coverage Percentage')

    # Create a scatter plot to show the impact of education on health insurance coverage
    create_scatter_plot(data, 'year', 
                       ['high_school', 'bachelors_degree', 
                        'recent_high-school_graduate', 'recent_college_graduate'],
                       ['High School', 'Bachelors Degree',
                        'Recent High School Graduate', 'Recent College Graduate'],
                       'Impact of Education in Employer-sponsored Health Insurance',
                       'Year', 'Health Insurance Coverage')
