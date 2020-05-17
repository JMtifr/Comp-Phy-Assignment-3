#Assignment 3
# Problem 9
# Convolution of Box function with itself.
# We evaluate convolution by FT 
import numpy as np
import matplotlib.pyplot as pt

# defining functions for convolutions
def f1(x):
 if abs(x)<=1.0:
  return(1.0)
 else:
  return(0.0)
def f2(x):
 if abs(x)<=1.0:
  return(1.0)
 else:
  return(0.0)
 
# setting up arrays 
n=int(2**7)
x_min=-1.5;x_max=4.5
dx=(x_max-x_min)/(n-1)
x=np.linspace(x_min,x_max,n) # x array
X1=[];X2=[]
for i in x: # creating samples
 X1+=[f1(i)] 
 X2+=[f2(i)]
Y1=np.hstack((X1,np.zeros(n))) # zero padding
Y2=np.hstack((X2,np.zeros(n)))

# FTT of 2 zero padded samples
K1=np.fft.fft(Y1,norm="ortho")
K2=np.fft.fft(Y2,norm="ortho")

# inverse FFT of products of FFT
K=K1*K2
Y=np.fft.ifft(K,norm="ortho")

Y=Y*dx*np.sqrt(2*n) # This is convolution
xx=np.linspace(2*x_min,x_min+x_max,n) # the X array of convoluted function


pt.plot([-3,-1,-1,1,1,3],[0,0,1,1,0,0],'m--',label="Box functions")
pt.plot(xx,Y[:n],'c:',label="Numerical convolution")
pt.title("Convolution")
pt.xlabel("x");pt.ylabel("y")
pt.legend()
pt.show()
