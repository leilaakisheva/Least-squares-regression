import numpy as np
import math
import matplotlib.pyplot as plt

def data(vmin, vmax, N, max_noise, y0, k):
  x=np.random.uniform(vmin, vmax, N) #creating values of x in the given range
  noise=np.random.uniform(-max_noise, max_noise, N) #creating an array of the noise with the given extrema value
  x_new=x+noise #redefining values of x with the noise
  y=y0*np.exp(-k*x_new) #finding values of y using values of x with the noise
  y1=np.log(y) #linearizing for the linear regression
  a0=np.log(y0)
  a1=-k
  return x, x_new, y, y1,a0, a1

def lsr(x1,y1, a0, a1, N):
  e=np.zeros(N)
  s=np.zeros(N)
  for i in range(N):
    e[i]=y1[i]-(a0+a1*x1[i]) #finding errors for the i-th y1, x1
    s[i]=y1[i]-np.mean(y1) #computing deviation
  S_r=np.sum(e**2)
  S_t=np.sum(s**2)
  r_2=(S_t-S_r)/(S_t)
  a1_new=(N*sum(x1*y1)-sum(x1)*sum(y1))/(N*sum(x1**2)-(sum(x1))**2) #computing new value of the slope (fitted)
  a0_new=np.mean(y1)-a1_new*np.mean(x1) #new value of a0
  return r_2, a0_new, a1_new

def order(x): #the point of this function is to sort data in ascending order in order to create a plot
    for i in range(len(x)):
        swap=i+np.argmin(x[i:])
        (x[i], x[swap]) = (x[swap], x[i])
    return x

def plot(vmin, vmax, N, max_noise, y0, k):
  x,x1,y,y1,a0,a1=data(vmin, vmax, N, max_noise, y0, k)
  r,a0_fit,a1_fit=lsr(x,y1,a0,a1, N)
  y_fit=a0_fit + a1_fit*x1 #finding a fitted line
  plt.scatter(x, y1, label='Observation')
  plt.plot(x1,y_fit, color='r', label='Fit')
  plt.legend()
  plt.title("N = %i" %N)
  plt.show()
  plt.scatter(x,y)
  #redifining coefficients in order to make a fitted line for our initial exponential function
  k=a1_fit
  y0_exp=np.exp(a0_fit)
  x1_order=order(x)
  y_exp=y0_exp*np.exp(k*x)
  plt.plot(x1_order, y_exp,color='r')
  plt.title("N = %i" %N)
  plt.show()
  return r, y1, y_fit

"""##**Part I**
Plotting data with different N's

###**Plot 1.1**
"""

N=20
r1, y, y_fit=plot(1, 5, N, 0.5, 7, 2)
error=abs((y-y_fit)/(y_fit))
rel_er1=np.mean(error)
print("R squared:", r1)
print("Relative error:", rel_er1)

"""###**Plot 1.2**"""

N=30
r2, y, y_fit=plot(1, 5, N, 0.5, 7, 2)
error=abs((y-y_fit)/(y_fit))
rel_er2=np.mean(error)
print("R squared:", r2)
print("Relative error:", rel_er2)

"""###**Plot 1.3**"""

N=40
r3, y, y_fit=plot(1, 5, N, 0.5, 7, 2)
error=abs((y-y_fit)/(y_fit))
rel_er3=np.mean(error)
print("R squared:", r3)
print("Relative error:", rel_er3)

"""###**Plot 1.4**"""

N=100
r4, y, y_fit=plot(1, 5, N, 0.5, 7, 2)
error=abs((y-y_fit)/(y_fit))
rel_er4=np.mean(error)
print("R squared:", r4)
print("Relative error:", rel_er4)

"""##**Part II**
Plotting data with different level of noises.

###**Plot 2.1**
"""

N=30
vmin=1
vmax=5
max_noise5=np.random.uniform(0.05*vmin, 0.45*vmax)
print(max_noise5)
r5, y, y_fit=plot(vmin, vmax, N, max_noise5, 7, 2)
error=abs((y-y_fit)/(y_fit))
rel_er5=np.mean(error)
print("R squared:", r5)
print("Relative error:", rel_er5)

"""###**Plot 2.2**"""

N=30
vmin=1
vmax=5
max_noise6=np.random.uniform(0.05*vmin, 0.45*vmax)
print(max_noise6)
r6, y, y_fit=plot(vmin, vmax, N, max_noise6, 7, 2)
error=abs((y-y_fit)/(y_fit))
rel_er6=np.mean(error)
print("R squared:", r6)
print("Relative error:", rel_er6)

"""###**Plot 2.3**"""

N=30
vmin=1
vmax=5
max_noise7=np.random.uniform(0.05*vmin, 0.45*vmax)
print(max_noise7)
r7, y, y_fit=plot(vmin, vmax, N, max_noise7, 7, 2)
error=abs((y-y_fit)/(y_fit))
rel_er7=np.mean(error)
print("R squared:", r7)
print("Relative error:", rel_er7)

"""###**Plot 2.4**"""

N=30
vmin=1
vmax=5
max_noise8=np.random.uniform(0.05*vmin, 0.45*vmax)
print(max_noise8)
r8, y, y_fit=plot(vmin, vmax, N, max_noise8, 7, 2)
error=abs((y-y_fit)/(y_fit))
rel_er8=np.mean(error)
print("R squared:", r8)
print("Relative error:", rel_er8)

"""####Creating tables with the results"""

from tabulate import tabulate
table1 = [['N', 'R squared', 'Rel. error'],
         [20, round(r1, 5), round(rel_er1,5)],
         [30, round(r2, 5), round(rel_er2,5)],
         [40, round(r3, 5), round(rel_er3, 5)],
         [100, round(r4, 5), round(rel_er4,5)]]

table2 = [['N', 'Max. noise','R squared', 'Rel. error'],
         [30, round(max_noise5, 5),round(r5, 5), round(rel_er5,5)],
         [30, round(max_noise6, 5),round(r6, 5), round(rel_er6,5)],
         [30, round(max_noise7, 5),round(r7, 5), round(rel_er7, 5)],
         [30, round(max_noise8, 5),round(r8, 5), round(rel_er8,5)]]

"""###**Results**
As it can be seen in the **plot 1.1-1.4** as the number of elements in the dataset increases, out exponential fit becomes better. Moreover the **Table-1**, values of the R-squared slightly increases with the number of elements, so the correlation becomes better. This can be explained by the fact that as the number of points increases, there is a higher probability that more points will be at the best fit line.

In the **plot 2.1-2.4** it can be seen that for N=30 and decreasing noise levels, R-squared also decreases. However, comparing with the first part, there is a dramatic increase in correlation with the decrease of noise. And in the **Table-2** one can see numerical results of this. Also, relative error drops from **22% to 0.01%**.

###**Table 1**
"""

print(tabulate(table1, headers='firstrow'))

"""###**Table-2**"""

print(tabulate(table2, headers='firstrow'))

"""###**Conclusion**
In this assignment it was asked to complete linear regression on the exponential decay function and compare results as the number of points and noise levels vary. The results are consistent with the hypothesis, so the method is successful.
"""
