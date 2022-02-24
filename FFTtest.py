#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import numpy as np
import pandas as pd
from scipy.fftpack import fft
import math
import matplotlib.pyplot as plt
def myfft(TIME,DATA,Fs):
    #DATA = DATA.replace([np.inf, -np.inf], 0)
    len = TIME.size
    Y1 = fft(DATA)
    P2 = abs(Y1 / len);
    P1 = P2[range(0, int(len / 2))];
    P1[0] = P1[0] * 0.5
    P1 = P1 * 2
    f1 = Fs * np.linspace(0, (len / 2), int(len / 2)) / len
    ################################################################
    temp_rms2 = 0;
    for Ptemp in P1:
        # if i == 0:
        #     temp_rms2 = temp_rms2 + P1(0) * P1(0) * 2
        # else:
        #     temp_rms2 = temp_rms2 + P1(i) * P1(i)
        temp_rms2 = temp_rms2 + Ptemp * Ptemp
    temp_rms2 = temp_rms2 + P1[0] * P1[0]

    temp_rms2 = np.sqrt(temp_rms2) / 1.414
    return (f1,P1,Fs/len,temp_rms2)

# t1 = []
# t1 = np.arange(0,0.1,0.0001)
# f_sample1= 1/0.0001
# data1 = 3* np.sin(2*math.pi*50*t1)
# plt.plot(t1, data1, color="red", linewidth=1.5, linestyle="-")
# plt.show()
#
# [Freq, P1] = myfft(t1,data1,f_sample1)
#
# plt.plot(Freq,P1,color="red", linewidth=1.5, linestyle="-")
# plt.show()