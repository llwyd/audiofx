import numpy as np 
import matplotlib.pyplot as plt 
import scipy.io.wavfile as wav 

#import wav file
[fs,x]=wav.read('input.wav')
length = len(x)

#20 ms delay
delay = 20
delay_samples = int((delay / 1000) * fs)
delay_gain = 0.5

#pre allocate output array
y=np.zeros(length)

#pre delay stage (can't use feedback on data that doesn't exist!)
for i in range(delay_samples):
    y[i]=x[i]

#actual delay routine
for i in range(delay_samples,length):
    y[i]=x[i]+(delay_gain*y[i-delay_samples]);

# normalise
y=y/np.max(np.abs(y));

# scale
y*=32767;

y=np.asarray(y,dtype=np.int16);

#write output
wav.write('output.wav',fs,y)
