"""
    classwork for february 22
"""

# import seaborn as sns
# import matplotlib as plt
# import pandas as pd

# funct takes 2 in parameters, and returns int type
# def sum_two_numbers(a: int, b: int) -> int:
# return a + b

# compute rolling average, of df 'mta', column 'entries':
# mta['7DayRolling'] = mta['entries'].rolling(7).mean()

# create a lineplot of entries and rolling averages
# sns.lineplot(x='date', y='entries', data=mta) # line plot, entries
# sns.lineplot(x='date', y='7DayRolling', data=mta) #line plot, rolling

# using folium to create maps
# import folium library


import folium

myMap = folium.Map()

newMark = folium.Marker([lat, lon], popup=name)

newMark.add_to(myMap)

myMap = folium.Map(location=[40.75, -74.125],
                   zoom_start=10, tiles='Stamen Watercolor')

myMap.save(outfile='myMap.html')
