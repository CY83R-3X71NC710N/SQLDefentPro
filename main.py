
#!/usr/bin/env python
# CY83R-3X71NC710N copyright 2023

# SQLDefentPro is a Python program designed to detect and prevent SQL injection attacks
# by checking for suspicious string formatting and content in database queries.
# The program uses SciPy and Matplotlib to generate data visualizations of the suspicious queries
# and protection state of the system.

# Import necessary libraries
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt

# Define function to check for suspicious strings
def check_for_suspicious_strings(query):
    # List of suspicious strings
    suspicious_strings = ["DROP", "DELETE", "ALTER", "INSERT", "UPDATE"]

    # Iterate through suspicious strings
    for string in suspicious_strings:
        # Check if query contains suspicious string
        if string in query:
            # Return True if query contains suspicious string
            return True
    # Return False if query does not contain suspicious string
    return False

# Define function to generate data visualization
def generate_data_visualization(query):
    # Get suspicious string from query
    suspicious_string = query.split(" ")[0]

    # Create array of data points
    data = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])

    # Create plot
    plt.plot(data[:,0], data[:,1], label=suspicious_string)
    plt.xlabel("x axis")
    plt.ylabel("y axis")
    plt.title("Data Visualization")
    plt.legend()
    plt.show()

# Define main function
def main():
    # Prompt user to enter database query
    query = input("Please enter your database query: ")

    # Check if query contains suspicious string
    if check_for_suspicious_strings(query):
        # Generate data visualization
        generate_data_visualization(query)
    else:
        # Print message
        print("No suspicious strings found in query.")

# Call main function
if __name__ == "__main__":
    main()
