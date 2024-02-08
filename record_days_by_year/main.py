# -*- coding: utf-8 -*-
"""
Reads weather records from 1948 until 2018.
Then counts how many 'record' cold or hot days each year had.
A 'record' in a year means that this year has the highest/lowest recorded
temperature for this specific day.
Example: the hottest November 13th (1948-2018) in this city was in 1977.
"""

file=open('weather.txt')
days=dict([('2 29', '-6.5+1952')])
days2=dict([('2 29', '-6.5+1952')])
i=0
for line in file:
  line=line.split()
  year=line[1]
  month=line[2]
  day=line[3]
  temp=float(line[6])
  date=month+' '+day
  x=str(temp)+'+'+year
  if i<365:
    days[date]=x
    days2[date]=x
    i+=1
  else:
    a=days[date]
    b=days2[date]
    a1=a.find('+')
    b1=b.find('+')
    if float(a[:a1])<temp:
      days[date]=x
    if float(b[:b1])>temp:
      days2[date]=x
years={}
years2={}
d=days.values()
d2=days2.values()
for elem in d:
  q=elem.find('+')+1
  elem=elem[q:]
  years[elem]=0
for elem in d2:
  q=elem.find('+')+1
  elem=elem[q:]
  years2[elem]=0
for elem in d:
  q=elem.find('+')+1
  elem=elem[q:]
  years[elem]+=1
for elem in d2:
  q=elem.find('+')+1
  elem=elem[q:]
  years2[elem]+=1
print('hottest days:')
a=years.keys()
for elem in a:
  b=years[elem]
  print(elem, '-', b)
print('\ncoldest days:')
a=years2.keys()
for elem in a:
  b=years2[elem]
  print(elem, '-', b)