# Assignment 3
# Problem 8
# 2 d ft
import numpy as np
import matplotlib.pyplot as pt
from matplotlib import cm
from mpl_toolkits.mplot3d.axes3d import get_test_data
from mpl_toolkits.mplot3d import Axes3D  
#from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

# defining 2d functions
def f(x,y): # f(x,y)
 return(np.exp(-x*x-y*y))
def w(x,y): # analytic FT of f(x,y)
 return(np.exp(-(x*x+y*y)/4.0)/2.0)

# creating arrays
n_x=256;n_y=256
x_min=-40.0;x_max=40.0
y_min=-40.0;y_max=40.0
dx=(x_max-x_min)/(n_x-1)
dy=(y_max-y_min)/(n_y-1)
X=np.linspace(x_min,x_max,n_x)
Y=np.linspace(y_min,y_max,n_y)
f_xy=np.zeros((n_x,n_y))
for i in range(n_x):
 f_xy[i]=np.array(f(X[i],Y))

# calculating fft
f_kx_ky=np.fft.fft2(f_xy,norm="ortho")

#calculating FT from FFT
kx=np.fft.fftfreq(n_x,dx)*np.pi*2.0
ky=np.fft.fftfreq(n_y,dy)*np.pi*2.0
for i in range(n_x):
 for j in range(n_y):
  f_kx_ky[i][j]=dx*dy*np.sqrt(n_x*n_y)/2.0/np.pi*np.exp(-1.0j*(x_min*kx[i]+y_min*ky[j]))*f_kx_ky[i][j]

#plotting data
# rearranging data by increasing order in K-----------
f_kx_ky=np.vstack((f_kx_ky[int(n_x/2):],f_kx_ky[:int(n_x/2)]))
ky=np.hstack((ky[int(n_y/2):],ky[:int(n_y/2)]))
kx=np.hstack((kx[int(n_x/2):],kx[:int(n_x/2)]))
for i in range(n_x):
 f_kx_ky[i]=np.hstack((f_kx_ky[i][int(n_y/2):],f_kx_ky[i][:int(n_y/2)]))
#-----------------------------------------------------
X, Y = np.meshgrid(kx,ky)
an=w(X,Y)
fig = pt.figure()
ax = fig.add_subplot(1, 2, 1, projection='3d')
surf = ax.plot_surface(X, Y, np.real(f_kx_ky), cmap=cm.coolwarm,linewidth=0, antialiased=False)
ax.set_xlabel('K_x');ax.set_ylabel('K_y');ax.set_zlabel('FT');pt.title("Numerical")
fig.colorbar(surf,shrink=0.5, aspect=10)
ax=fig.add_subplot(1,2,2,projection='3d')
surf2=ax.plot_surface(X,Y,an,cmap=cm.coolwarm,linewidth=0, antialiased=False)
ax.set_xlabel('K_x');ax.set_ylabel('K_y');ax.set_zlabel('FT');pt.title("Analytic")
fig.colorbar(surf2,shrink=0.5, aspect=10)
pt.tight_layout()
pt.show()

