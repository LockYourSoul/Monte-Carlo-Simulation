%matplotlib inline
from numpy import random
import numpy as np
import math
import matplotlib.pyplot as plt

#we'll be generating triplets let's say x,y,z and measuring distance from origin to check if it lies in the sphere
def func(N,a):
    #limits for the numbers
    b=-1*a

    x=random.uniform(a,b,N)
    y=random.uniform(a,b,N)
    z=random.uniform(a,b,N)

    inside=0

    for i in range(N):
        dist=(x[i]**2+y[i]**2+z[i]**2)**0.5
        if(dist<=abs(a)):
            inside+=1

    return(inside/N)
def plot(N,a):
    ratios=[ ]
    for i in range(N):
        ratios.append(func(N,a))

    plt.title("Ratio Distribution")
    plt.hist(ratios,bins=25,ec='black')
    plt.xlabel("ratios")

plot(1000,10)