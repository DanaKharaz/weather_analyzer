# -*- coding: utf-8 -*-
"""
Reads weather records from 1948 until 2018.
Then plots the veriation of average temperature from 1949 until 2018 for each month and overall as well.
The graphs are very basic, not labeled in any way.
"""

import matplotlib as matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
fig=plt.figure(figsize=(70, 70))
ax=fig.add_subplot(111)

file=open('weather.txt', 'r')

end=[]

pro=0
i=0
y='1949'

for line in file:
  t=line.find(' ')+1
  o=line.find(' ')+5
  year=str(line[t:o])
  if year=='1948':
    continue
  if line[28]!=' ':
     temp=float(line[28:31])
  if line[27]!=' ':
     temp=float(line[27:31])
  if line[26]!=' ':
     temp=float(line[26:31])
  if year==y:
     pro+=temp
     i+=1
  else:
     n=round(pro/i, 3)
     end.append(n)
     pro=temp
     y=year
     i=1

ax.plot(end)
fig.savefig('graph.png')

file.close()

file2=open('weather.txt', 'r')

fig1=plt.figure(figsize=(71, 71))
January=fig1.add_subplot(111)

fig2=plt.figure(figsize=(71, 71))
February=fig2.add_subplot(111)

fig3=plt.figure(figsize=(71, 71))
March=fig3.add_subplot(111)

fig4=plt.figure(figsize=(71, 71))
April=fig4.add_subplot(111)

fig5=plt.figure(figsize=(71, 71))
May=fig5.add_subplot(111)

fig6=plt.figure(figsize=(71, 71))
June=fig6.add_subplot(111)

fig7=plt.figure(figsize=(71, 71))
July=fig7.add_subplot(111)

fig8=plt.figure(figsize=(71, 71))
August=fig8.add_subplot(111)

fig9=plt.figure(figsize=(71, 71))
September=fig9.add_subplot(111)

fig10=plt.figure(figsize=(71, 71))
October=fig10.add_subplot(111)

fig11=plt.figure(figsize=(71, 71))
November=fig11.add_subplot(111)

fig12=plt.figure(figsize=(71, 71))
December=fig12.add_subplot(111)

months=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

january=[]
february=[]
march=[]
april=[]
may=[]
june=[]
july=[]
august=[]
september=[]
october=[]
november=[]
december=[]

y=1948
i=0

for line in file2:
  line=line.split()
  year=int(line[1])
  month=int(line[2])
  temp=float(line[6])
     
  if year==y:
    months[(month-1)]+=temp
  else:
    january.append(months[0]/31)
    march.append(months[2]/31)
    april.append(months[3]/30)
    may.append(months[4]/31)
    june.append(months[5]/30)
    july.append(months[6]/31)
    august.append(months[7]/31)
    september.append(months[8]/30)
    october.append(months[9]/31)
    november.append(months[10]/30)
    december.append(months[11]/31)
    if int(year)%4==0:
      february.append(months[1]/29)
    else:
      february.append(months[1]/28)
    y=year
    months=[temp, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

january=january[2:]
february=february[2:]
march=march[2:]
april=april[2:]
may=may[2:]
june=june[2:]
july=july[2:]
august=august[2:]
september=september[2:]
october=october[2:]
november=november[2:]
december=december[2:]

January.plot(january)
fig1.savefig('january.png')

February.plot(february)
fig2.savefig('february.png')

March.plot(march)
fig3.savefig('march.png')

April.plot(april)
fig4.savefig('april.png')

May.plot(may)
fig5.savefig('may.png')

June.plot(june)
fig6.savefig('june.png')

July.plot(july)
fig7.savefig('july.png')

August.plot(august)
fig8.savefig('august.png')

September.plot(september)
fig9.savefig('september.png')

October.plot(october)
fig10.savefig('october.png')

November.plot(november)
fig11.savefig('november.png')

December.plot(december)
fig12.savefig('december.png')