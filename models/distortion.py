import numpy as np 
import matplotlib.pyplot as plt 
import scipy.io.wavfile as wav 

#import wav file
[fs,x]=wav.read('input.wav')
length = len(x)

# distortion polynomial
p=np.poly1d([0.1,0.5,0.6])

#pre allocate output array
y=np.zeros(length)

# run input through polynomial
for i in range(length):
    y[i]=(p(np.abs(x[i])))
    if(x[i]<0):
        y[i]=y[i]*-1

# normalise
y=y/np.max(np.abs(y))

# scale
y*=32767;

#convert output
y=np.asarray(y,dtype=np.int16);

#write output
wav.write('dist_output.wav',fs,y)
