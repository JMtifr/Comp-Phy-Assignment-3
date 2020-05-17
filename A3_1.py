# Assignment 3
# problem 1
# FT of sinx/x

import numpy as np
import matplotlib.pyplot as pt

def f(x): # defining f(x)
 y=np.zeros(len(x))
 for i in range(len(x)):
  if x[i]==0.0:
   y[i]=1.0
  else:
   y[i]=np.sin(x[i])/x[i]
 return(y)
def fe(k): # analytical F(k)
 y=np.zeros(len(k))
 for i in range(len(k)):
  if abs(k[i])<=1.0:
   y[i]=np.sqrt(np.pi/2.0)
  else:
   y[i]=0.0
 return(y)

x_min=-np.pi*30.0
x_max=np.pi*30.0
n=2**10 # number of points
dx=(x_max-x_min)/(n-1.0) # dx
x=np.linspace(x_min,x_max,n) #creating x array
k=2.0*np.pi*np.fft.fftfreq(n,d=dx) # creating k array
y_k=np.fft.fft(f(x),norm="ortho") # FFT  using numpy
y_k=dx*np.sqrt(n/2.0/np.pi)*np.exp(-1.0j*x_min*k)*y_k # Fourier transform 


k=np.hstack((k[int(n/2):n],k[:int(n/2)])) # rearranging k array in monotonic increase order
y_k=np.hstack((y_k[int(n/2):n],y_k[:int(n/2)]))
np.savetxt("A3_1.csv",np.column_stack((k,np.real(y_k))),delimiter=',') # saving result in datafile

pt.plot(k,np.real(y_k),'m4-',label='DFT')
pt.plot(k,fe(k),'c-',label='Analytic FT')
pt.xlabel("k");pt.ylabel("F(k)")
pt.title("Fourier transform")
pt.legend()
pt.show()
