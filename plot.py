import matplotlib.pyplot as pt
import matplotlib.cbook as cbook
import matplotlib as mpl
import numpy as np
import pandas as pd
#----------------------------------------------------------------------------------------------------------------------------
msft = pd.read_csv('/media/jibak/Data/JIBAK/GS/Computational physics/Asignment 3/A3_2.csv',names=['k','FFTW','Analytic'])
cccc=pd.read_csv('/media/jibak/Data/JIBAK/GS/Computational physics/Asignment 3/A3_1.csv',names=['kk','numpy.fft'])
aa = pd.concat([msft,cccc], axis=1)
print(aa.shape)
aa.plot(0,[2,1,4],legend=True,style=['y','m--','c:'])
pt.title("Fourier transform using FFTW")
pt.savefig("/media/jibak/Data/JIBAK/GS/Computational physics/Asignment 3/A3_2.svg")
pt.tight_layout()
pt.clf()
#----------------------------------------------------------------------------------------------------------------------------
msft = pd.read_csv('/media/jibak/Data/JIBAK/GS/Computational physics/Asignment 3/A3_2.csv',names=['k','FFTW','Analytic'])
cccc=pd.read_csv('/media/jibak/Data/JIBAK/GS/Computational physics/Asignment 3/A3_3.csv',names=['kk','GSL','an'])
aa = pd.concat([msft,cccc], axis=1)
aa.plot(0,[2,1,4],legend=True,style=['y','c--','m:'])
pt.title("Fourier transform using GSL")
pt.savefig("/media/jibak/Data/JIBAK/GS/Computational physics/Asignment 3/A3_3.svg")
pt.clf()
#----------------------------------------------------------------------------------------------------------------------------
msft = pd.read_csv('/media/jibak/Data/JIBAK/GS/Computational physics/Asignment 3/A3_4.csv',names=['k','FFTW','Analytic'])
msft.plot(0,[2,1],legend=True,style=['y-','g--'])
pt.title("Fourier transform of Gaussian using FFTW")
pt.savefig("/media/jibak/Data/JIBAK/GS/Computational physics/Asignment 3/A3_4.svg")
pt.clf()
