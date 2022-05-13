#!/usr/bin/env python
# _*_ coding:utf-8 _*_



# 说明  pyinstaller -F -w -i test.ico main.spec



import time
import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import scipy.signal as sig
from math import pi
import control as ctl
import math

plt.rcParams['font.sans-serif'] = ['SimHei']  # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

# 读取文件 显示前5行
data1 = pd.read_csv('b2_2021_08_02_09_15.csv', skiprows=1)
#print(data1.head(5))

# 填充空白
data1 = data1.fillna(-1)
#data1['TimeStamp'].head(5)
n = len(data1['TimeStamp'])
print(n)

# 获取时间序列
t0 = pd.to_datetime(data1['TimeStamp'][0],format='%Y-%m-%d/%H:%M:%S.%f')
t1 = pd.to_datetime(data1['TimeStamp'][1],format='%Y-%m-%d/%H:%M:%S.%f')
print(t0)
print(type(t0))
dt = pd.to_timedelta(t1 - t0)
dtt = dt.total_seconds()
print(dt)
print(dtt)

tt1 = [0 for i in range(n)]
ttt1 = [0 for i in range(n)]
print(len(tt1))
for i in range(n):
    print(i)
    temp1 = pd.to_datetime(data1['TimeStamp'][i], format='%Y-%m-%d/%H:%M:%S.%f', errors='ignore')

    try:
        temp2 = pd.to_timedelta(temp1 - t0)
        time_d_float = temp2.total_seconds()

        tt1[i] = temp2;
        ttt1[i] = time_d_float;
    except:
        tt1[i] = tt1[i - 1] + dt;
        ttt1[i] = ttt1[i - 1] + dtt;
        print(i)
        print('error')

# 读取时间以外的数据

gCovGenSpd = pd.DataFrame(data1['gCovGenSpd'])   #gActualGenSpd
gCovGenSpd = gCovGenSpd.values

gConvActPower = pd.DataFrame(data1['gConvActPower'])
gConvActPower = gConvActPower.values

gGenActPower = pd.DataFrame(data1['gGenActPower'])
gGenActPower = gGenActPower.values

print(len(ttt1))
print(len(gCovGenSpd))

# 绘图部分
plt.figure()
plt.grid()
#plt.title(pd.Series(data1['TimeStamp']).value_counts())

# miloc = plt.MultipleLocator(50)
# maloc = plt.MultipleLocator(100)
# plt.xaxis.set_minor_locator(miloc)
# plt.yaxis.set_minor_locator(maloc)
plt.grid(linestyle='-.', which='minor', linewidth=0.3, alpha=0.9)

plt.plot(ttt1,gGenActPower, label=u'gGenActPower')
plt.plot(ttt1,gConvActPower, label=u'gConvActPower')
plt.legend()
plt.show()