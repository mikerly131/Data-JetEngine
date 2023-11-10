import csv
from datetime import datetime
import matplotlib.pyplot as plt

# Use for simple, on emonth weather data
# filename = 'data/sitka_weather_07-2018_simple.csv'

filename = 'data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # print(header_row)

    # Use to see headers and find column to work with
    # for index, column_header in enumerate(header_row):
    #    print(index, column_header)

    # Get dates and high temperatures from csv file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

    # Plot the high temperatures
    plt.style.use('bmh')
    fig, ax = plt.subplots()
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='black', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # Format plot
    plt.title("Daily high and low temperatures - 2018", fontsize=16)
    plt.xlabel('', fontsize=14)
    fig.autofmt_xdate()
    plt.ylabel('Temperatures (F)',  fontsize=14)
    plt.tick_params(axis='both', which='major', labelsize=14)

    plt.show()

