# weather_analyzer
This is an old project about analyzing large sets of weather-related data. Time of development: 11/2019 - 03/2020

There are 3 different analyzers


1 - average_temp_variation

This was the first one, its purpose was to get acquainted with reading large datasets as well as plotting data with matplotlib.

What it does:

Reads weather records for one city from 1948 until 2018. Then plots the variation of average temperature from 1949 until 2018 for each month and overall as well. The graphs are very basic, not labeled in any way.


2 - record_days_by_year

This was the second one. It uses the same data as before, but this time it analyzes the data looking or 'record' days.

What it does:

Reads weather records for one city from 1948 until 2018. Then counts how many 'record' cold or hot days each year had. A 'record' in a year means that this year has the highest/lowest recorded temperature for this specific day. Example: the hottest November 13th (1948-2018) in this city was in 1977.


3 - daily_temp_animated

This was the last one, this time combining data for multiple cities together. Additionally, it served as a stepping stone or learning tkinter, as the data was presented visually through a changing map.

What it does:

Reads weather records for multiple cities from 1948 until 2018. Then asks the user for a start date. Afterward, shows on a map the average day temperature for each city starting from that date (changing to the next day each second.
