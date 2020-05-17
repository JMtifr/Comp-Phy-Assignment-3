# Assignment 3
# Problem 5
import numpy as np
import time 
import math as m
import matplotlib.pyplot as pt

# defining function for DFT
def DFT(x):
 n=len(x)
 Y=[]
 for q in range(n):
  y=0.0
  for p  in range(n):
   y=y+x[p]*(m.cos(2.0*m.pi*p*q/n)-m.sin(2.0*m.pi*p*q/n)*1.0j)
  Y+=[y/m.sqrt(n)]
 return(Y)

# time comparison loop
N=[2,4,8,16,19,32,47,64,97,128,197,256,371,512] # number of points array
x_a=0.0;x_b=100.0;t_dft=[];t_fft=[]
for i in N:
 X=np.linspace(x_a,x_b,i) # array for DFT
 t1_dft=time.perf_counter()
 Y1=DFT(X)
 t2_dft=time.perf_counter()
 t_dft+=[t2_dft-t1_dft] # time taken for dft
 t1_fft=time.perf_counter()
 Y2=np.fft.fft(X,norm='ortho')
 t2_fft=time.perf_counter()
 t_fft+=[t2_fft-t1_fft] # time taken for numpy.fft
 Y1=[];Y2=[] 

# plotting time data
pt.loglog(N,t_dft,'g+',label="ordinary DFT",basex=2,basey=10)
pt.loglog(N,t_fft,'bx',label="numpy.fft.fft",basex=2,basey=10)
pt.xlabel("N");pt.ylabel("t in sec")
pt.title("Time comparison between DFT & numpy FFT") 
pt.legend()
pt.show()

