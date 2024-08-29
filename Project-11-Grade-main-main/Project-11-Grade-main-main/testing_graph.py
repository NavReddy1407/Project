x=[]
y=[]
name=str(input("Please enter a title for this graph:"))
xname=str(input("Please enter the name of the x axis:"))
yname=str(input("Please enter the name of the y axis:"))
n=int(input("Please enter how many points you'd like to plot:"))
for i in range(0,n):
    xu=int(input("Please Enter the x value:"))
    yu=int(input("Please Enter the y value:"))
    x.append(xu)
    y.append(yu)
yname=yname+"-->"
xname=xname+"-->"
print("Data entry done!")

import matplotlib.pyplot as plt
import numpy as np 
plt.xlabel(xname,fontweight="bold")
plt.ylabel(yname,fontweight="bold")
plt.title(name,fontweight="bold")
plt.plot(x,y,linestyle='dotted',color="red",marker='o',markersize=8)
plt.grid()
plt.show()