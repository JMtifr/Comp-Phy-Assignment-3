# Assignment 3
# Problem 6
# Ft of constant
import numpy as np

print("enter the constant  in (a+bj) form")
a,b=float(input("a= ")),float(input("b= "))
print("enter the domain of constant function")
x_min=float(input("x_min= "))
x_max=float(input("x_max= "))
n=int(input(" enter number of points you want in output function = "))
dx=(x_max-x_min)/(n-1)

# calculating FFT followed by FT
FX=np.zeros(n)+a+1j*b
FK=np.fft.fft(FX,norm="ortho")
K=np.fft.fftfreq(n,dx)
FK=FK*dx*np.sqrt(n/2.0/np.pi)*np.exp(-1j*x_min*K)

# printing output
print("output written in file A3_6.csv")
print("FT at k=0 : ",FK[0])
np.savetxt("A3_6.csv",np.column_stack((K,FK)),delimiter=',')
