import csv
import os


def read_data(filename):
    test_data_directory = "../test_data/"
    relative_file_path = test_data_directory + filename
    current_directory = os.path.dirname(__file__)
    destination_file = os.path.join(current_directory, relative_file_path)

    # Create an empty list to store rows
    rows = []
    # Open the CSV file
    data_file = open(destination_file, 'r')
    # Create a CSV reader
    reader = csv.reader(data_file)
    # Skip the header
    next(reader)
    # Add rows from the reader to the list
    for row in reader:
        rows.append(row)
    return rows
