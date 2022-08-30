import pandas as pd
import numpy as np
import time

#start the counter
inicial_time = time.time()

data = None
#teste
with open(file='traffic.csv', mode='r', encoding='utf8') as fp:
    #skip the header
    fp.readline()

    #put the lines in a string
    data = fp.read()

#analytics - test
day = 14
incidents = 0
incident_by_day = dict()
half_hour = 1

for timebox in data.split(sep='\n'):
    timebox_data_str = timebox.split(sep=';')
    timebox_data = list(map(int, timebox_data_str[1: len(timebox_data_str) - 1]))

    timebox_array = np.array(timebox_data)
    #sum the elements of the array - problem vectorization
    sum_array = sum(timebox_array)

    #increases in accidents of the day
    incidents = incidents + sum_array

    #27 is the last half-hour of the day
    if half_hour == 27:
        incident_by_day[day] = incidents
        day = day + 1
        incidents = 0
        half_hour = 1
    else:
        half_hour += 1

#print the results
for day in incident_by_day:
    print(f'{day}: {incident_by_day[day]}')

#shows how much time was spent processing
final_time = time.time()
print(final_time - inicial_time)