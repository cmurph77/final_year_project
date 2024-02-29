import matplotlib.pyplot as plt
import numpy as np

def parse_data(data):
    parsed_data = {}
    for entry in data:
        key = list(entry.keys())[0]
        value = list(entry.values())[0]
        parsed_data[key] = value
    return parsed_data

def graph_results(data1, data2,title,ylabel):
    labels = list(data1.keys())
    x = np.arange(len(labels))
    width = 0.35

    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, list(data1.values()), width, label='Data 1')
    rects2 = ax.bar(x + width/2, list(data2.values()), width, label='Data 2')

    ax.set_xlabel('Trips')
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()

    plt.show()


# Example data
data1 = [{'500': 144.248}, {'750': 258.28}, {'1000': 356.76}, {'1250': 503.1816}, {'1500': 742.012}]
data2 = [{'500': 214.178}, {'750': 219.37333333333333}, {'1000': 312.983}, {'1250': 392.3968}, {'1500': 857.4246666666667}]


# Generate paired barchart
graph_results(parse_data(data1), parse_data(data2),"Average Travel Time", "Travel Time (seconds)")

