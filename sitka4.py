import matplotlib.pyplot as plt
import csv
from datetime import datetime

open_file = open("death_valley_2018_simple.csv", "r")

csv_file = csv.reader(open_file, delimiter=",")

header_row = next(csv_file)

print(type(header_row))

for index, column_header in enumerate(header_row):
    print(index, column_header)


# testing to convert date from string
# mydate = datetime.strptime('2018-07-01', '%Y-%m-%d')
# print(type(mydate))


highs = []
dates = []
lows = []

for row in csv_file:
    try:
        the_date = datetime.strptime(row[2], '%Y-%m-%d')
        high = int(row[4])
        low = int(row[5])
    except ValueError:
        print(f"Missing data for {the_date}")
    else:
        highs.append(int(row[4]))
        lows.append(int(row[5]))
        dates.append(the_date)
# missing data use except method.


# print(highs)
# print(dates)
# commen that can show like list

'''
fig = plt.figure()


#for row in csv_file:
    #highs.append(int(row[5]))

#print(highs)


plt.title("Daliy high temperatures, July 2018", fontsize=16)
plt.xlabel("", fontsize=12)
plt.ylabel("Temperature (F)", fontsize=12)
plt.tick_params(axis="both", which="major", labelsize=12)

plt.plot(dates, highs, c="red", alpha=0.5)
plt.plot(dates, lows, c="blue", alpha=0.5)

plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

fig.autofmt_xdate()

plt.show()


plt.subplot(2, 1, 1)
plt.plot(dates, highs, c="red")
plt.title("Highs")

plt.subplot(2, 1, 2)
plt.plot(dates, lows, c="blue")
plt.title("Lows")

plt.suptitle("Highs and Lows of Sitka, Alaska")
plt.show()
'''
