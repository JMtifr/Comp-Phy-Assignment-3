# Assignment 3
# Problem 10

import numpy as np
import pandas as pd
import matplotlib.pyplot as pt

noice=pd.read_table('/media/jibak/Data/JIBAK/GS/Computational physics/Asignment 3/noice.txt',sep='\n',names=["x"])
n=len(noice.x) # number of measurements
sq=np.linspace(0,n-1,n)
#---------------------------------------   Plotting measurements  ---------------------------------------------
pt.subplot(2,2,1)
pt.plot(sq,noice.x,'k1')
pt.title("Measurements")
pt.xlabel("secquences");pt.ylabel("value")
#------------------------------------------------------------------------------------------------------------
#-----------    DFT of measurements  ---------------------------------------------------------
k=np.fft.fft(noice.x,norm="ortho")
pt.subplot(2,2,2)
pt.plot(sq,np.real(k),'b.',label="Real part")
pt.plot(sq,np.imag(k),'r.',label="Imaginary part")
pt.title("DFT")
pt.xlabel("secquences");pt.ylabel("value")
pt.legend(loc=0)
#---------------------------------------------------------------------------------------------
#------------------- Power spectrum ---------------------------------------------------------------
freq=np.fft.fftfreq(n,1)*np.pi*2
PS=np.real(k)**2+np.imag(k)**2
pt.subplot(2,2,3)
pt.plot(freq,PS,'m|')
pt.xlabel("discrete frequency");pt.ylabel("value")
pt.title("Power spectrum")
#--------------------------------------------------------------------------------------------------
#---------------- Binned power spectrum ------------------------------------
bin=10
data=noice.x
while (n%10)!=0: # zero padding to make number of data points multiple of 10
 n=n+1
 data=np.hstack((data,[0]))
nb=int(n/10) # numer of points in each segment
kb=np.fft.fftfreq(nb,1)*np.pi*2.0
bin_spectrum=np.zeros(nb)
for i in range(10):
 b_data=data[i*nb:(i+1)*nb]
 b_sptr=np.fft.fft(b_data,norm="ortho")
 bin_spectrum=bin_spectrum+np.real(b_sptr)**2+np.imag(b_sptr)**2
bin_spectrum=bin_spectrum/n
pt.subplot(2,2,4)
pt.plot(kb,bin_spectrum,'g|')
pt.xlabel("discrete frequency");pt.ylabel("value")
pt.title("binned power spectrum")
pt.tight_layout()
pt.show()
