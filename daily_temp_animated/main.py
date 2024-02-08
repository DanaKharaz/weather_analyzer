"""
Reads weather records for multiple cities from 1948 until 2018.
Asks the user for a start date.
On a map shows the average day temperature for each city starting from that date.
"""

import time
from tkinter import *
canvas_width=450
canvas_height=526
master=Tk()
c=Canvas(master, width=canvas_width, height=canvas_height)
c.pack()
img=PhotoImage(file='Map.png')
c.create_image(0, 0, anchor=NW, image=img)
print("format: [year] [month] [day]")
f=str(input('Date: '))
NN=open("Nizhny Novgorod.txt", "r")
def nn(x):
  for line in NN:
    date=line[6:16]
    if line[19]!=' ':
      t=float(line[19:22])
    if line[18]!=' ':
      t=float(line[18:22])
    if line[17]!=' ':
      t=float(line[17:22])
    if date==x:
      break
  return t
t=nn(f)
i=t
xnn=c.create_text(245, 267, text=t, fill="navy", font=('Arial', 6))
M=open("Moscow.txt", "r")
def m(x):
  for line in M:
    date=line[6:16]
    if line[29]!=' ':
      t=float(line[29:32])
    if line[28]!=' ':
      t=float(line[28:32])
    if line[27]!=' ':
      t=float(line[27:32])
    if date==x:
      break
  return t
t=m(f)
xm=c.create_text(170, 267, text=t, fill="navy", font=('Arial', 6))
A=open("Archangel.txt", "r")
def a(x):
  for line in A:
    date=line[6:16]
    if line[25]!=' ':
      t=float(line[25:28])
    if line[24]!=' ':
      t=float(line[24:28])
    if line[23]!=' ':
      t=float(line[23:28])
    if date==x:
      break
  return t
t=a(f)
xa=c.create_text(200, 120, text=t, fill="navy", font=('Arial', 6))
Mu=open("Murmansk.txt", "r")
def mu(x):
  for line in Mu:
    date=line[6:16]
    if line[25]!=' ':
      t=float(line[25:28])
    if line[24]!=' ':
      t=float(line[24:28])
    if line[23]!=' ':
      t=float(line[23:28])
    if date == x:
      break
  return t
t=mu(f)
xmu=c.create_text(160, 43, text=t, fill="navy", font=('Arial', 6))
St=open("St. Petersburg.txt", "r")
def st(x):
  for line in St:
    date=line[6:16]
    if line[29]!=' ':
      t=float(line[29:32])
    if line[28]!=' ':
      t=float(line[28:32])
    if line[27]!=' ':
      t=float(line[27:32])
    if date==x:
      break
  return t
t=st(f)
xst=c.create_text(122, 189, text=t, fill="navy", font=('Arial', 6))
K=open("Kazan.txt", "r")
def k(x):
  for line in K:
    date=line[6:16]
    if line[29]!=' ':
      t=float(line[29:32])
    if line[28]!=' ':
      t=float(line[28:32])
    if line[27]!=' ':
      t=float(line[27:32])
    if date==x:
      break
  return t
t=k(f)
xk=c.create_text(285, 275, text=t, fill="navy", font=('Arial', 6))
S=open("Samara.txt", "r")
def s(x):
  for line in S:
    date=line[6:16]
    if line[29]!=' ':
      t=float(line[29:32])
    if line[28]!=' ':
      t=float(line[28:32])
    if line[27]!=' ':
      t=float(line[27:32])
    if date==x:
      break
  return t
t=s(f)
xs=c.create_text(300, 300, text=t, fill="navy", font=('Arial', 6))
U=open("Ufa.txt", "r")
def u(x):
  for line in U:
    date=line[6:16]
    if line[19]!=' ':
      t=float(line[19:22])
    if line[18]!=' ':
      t=float(line[18:22])
    if line[17]!=' ':
      t=float(line[17:22])
    if date==x:
      break
  return t
t=u(f)
xu=c.create_text(352, 262, text=t, fill="navy", font=('Arial', 6))
P=open("Perm.txt", "r")
def p(x):
  for line in P:
    date=line[6:16]
    if line[29]!=' ':
      t=float(line[29:32])
    if line[28]!=' ':
      t=float(line[28:32])
    if line[27]!=' ':
      t=float(line[27:32])
    if date==x:
      break
  return t
t=p(f)
xp=c.create_text(340, 212, text=t, fill="navy", font=('Arial', 6))
Y=open("Yekaterinburg.txt", "r")
def y(x):
  for line in Y:
    date=line[6:16]
    if line[29]!=' ':
      t=float(line[29:32])
    if line[28]!=' ':
      t=float(line[28:32])
    if line[27]!=' ':
      t=float(line[27:32])
    if date==x:
      break
  return t
t=y(f)
xy=c.create_text(383, 217, text=t, fill="navy", font=('Arial', 6))
V=open("Volgograd.txt", "r")
def v(x):
  for line in V:
    date=line[6:16]
    if date==x:
      if line[29]!=' ':
        t=float(line[29:32])
      if line[28]!=' ':
        t=float(line[28:32])
      if line[27]!=' ':
        t=float(line[27:32])
      break
  return t
t=v(f)
xv=c.create_text(247, 397, text=t, fill="navy", font=('Arial', 6))
def change(x):
  a=x[-2:]
  if a[0]==' ':
    a=int(a[1])
    a+=1
    a=str(a)
  else:
    a=int(a)
    a+=1
    a=str(a)
  if len(a)==1:
    a=' '+a
  x=x[:-2]+a
  return x
f=change(f)
day=c.create_text(40, 20, text=f, fill="navy", font=('Arial', 6))
def animate():
  global f
  global day
  global xnn
  global xa
  global xk
  global xm
  global xmu
  global xp
  global xs
  global xst
  global xu
  global xv
  global xy
  c.delete(xnn)
  c.delete(xa)
  c.delete(xk)
  c.delete(xm)
  c.delete(xmu)
  c.delete(xp)
  c.delete(xs)
  c.delete(xst)
  c.delete(xu)
  c.delete(xv)
  c.delete(xy)
  c.delete(day)
  f=change(f)
  day=c.create_text(40, 20, text=f, fill="navy", font=('Arial', 6))
  i=a(f)
  xa=c.create_text(200, 120, text=i, fill="navy", font=('Arial',  6))
  i=k(f)
  xk=c.create_text(285, 275, text=i, fill="navy", font=('Arial',  6))
  i=m(f)
  xm=c.create_text(170, 267, text=i, fill="navy", font=('Arial',  6))
  i=mu(f)
  xmu=c.create_text(160, 43, text=i, fill="navy", font=('Arial',  6))
  i=nn(f)
  xnn=c.create_text(245, 267, text=i, fill="navy", font=('Arial',  6))
  i=p(f)
  xp=c.create_text(340, 212, text=i, fill="navy", font=('Arial',  6))
  i=s(f)
  xs=c.create_text(300, 300, text=i, fill="navy", font=('Arial',  6))
  i=st(f)
  xst=c.create_text(122, 189, text=i, fill="navy", font=('Arial',  6))
  i=u(f)
  xu=c.create_text(352, 262, text=i, fill="navy", font=('Arial',  6))
  i=v(f)
  xv=c.create_text(247, 397, text=i, fill="navy", font=('Arial',  6))
  i=y(f)
  xy=c.create_text(383, 217, text=i, fill="navy", font=('Arial',  6))
  c.after(2000, animate)
animate()
mainloop()
