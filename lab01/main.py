import librosa
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

chunk = 8192
y, sr = librosa.load(librosa.example('brahms'))

fig = plt.figure()
ax = plt.subplot(111,projection='polar')
ax.axis('off')
ln, = ax.plot(np.linspace(0,2*np.pi,chunk),np.zeros(chunk))

def update(frame):
    y_clip = y[frame:frame+chunk]
    y_fft = np.abs(np.fft.fft(y_clip))
    y_fft = 0.02 * y_fft / np.max(y_fft)
    y_fft = np.roll(y_fft,100*frame//chunk)
    ln.set_ydata(y_fft)
    return ln,

ani = FuncAnimation(fig, update, frames = np.arange(0,len(y),chunk))

plt.show()