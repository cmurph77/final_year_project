import csv
import matplotlib.pyplot as plt

def calculate_column_averages(csv_file):
    # Initialize lists to store column data
    columns = []

    # Read the CSV file and extract column data
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if not columns:
                columns = [[] for _ in range(len(row))]
            for i, value in enumerate(row):
                columns[i].append(float(value))

    # Calculate column averages
    column_averages = [sum(column) / len(column) for column in columns]

    return column_averages

def plot_column_averages(column_averages, column_labels):
    # Plot the column averages
    plt.figure(figsize=(8, 6))
    plt.bar(range(len(column_averages)), column_averages, color='skyblue')
    plt.xlabel('Columns')
    plt.ylabel('Average')
    plt.title('Average of Each Column')
    plt.xticks(range(len(column_averages)), column_labels)
    plt.grid(axis='y')
    plt.show()

def main():
    # Replace 'sample_data.csv' with the path to your CSV file
    csv_file = 'no_rerouting_50tr_cm.csv'
    column_averages = calculate_column_averages(csv_file)
    
    # Extract column labels from the header row
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        column_labels = next(reader)

    # Plot column averages with column labels
    plot_column_averages(column_averages, column_labels)

if __name__ == "__main__":
    main()

