#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from UI.noname import plc

import matplotlib as mpl
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
from mpl_toolkits.axisartist.parasite_axes import HostAxes, ParasiteAxes
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA
from matplotlib.backend_tools import ToolBase, ToolToggleBase

import numpy as np
import pandas as pd
import scipy.io as scio

import wx
import wx.xrc
import locale

import operator

''' 函数：返回变量是否被定义过 '''

# def resource_path(relative_path):
#     if getattr(sys, 'frozen', False):  # 是否Bundle Resource
#         base_path = sys._MEIPASS
#     else:
#         base_path = os.path.abspath(".")
#     return os.path.join(base_path, relative_path)

global checkedNum, checkedNumSave
global checkedItems, showItems
global xmin, xmax

checkedItems = ()
showItems = set (checkedItems)

xmin = -50000
xmax = 50000
font = {'family': 'SimHei',
        'weight': 'bold',
        'size': '16'}


def isset(v):
    try:
        type (eval (v))
    except:
        return 0
    else:
        return 1


def csv_to_dataframe(name):
    return


def func_cycle(x, e, x_o, y_o):
    return np.sqrt ((e ** 2 - (x - x_o) ** 2)) + y_o


def plt_font_set():
    plt.rc ('font', **font)  # 步骤一（设置字体的更多属性）
    plt.rc ('axes', unicode_minus=False)  # 步骤二（解决坐标轴负数的负号显示问题）


class MyFrame (plc):
    locale.getlocale ()
    ''' 创建输出路径  '''
    plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
    plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

    def __init__(self, parent):
        plc.__init__ (self, parent)

        wx.Frame.SetBackgroundColour (self, 'Write')  # ???
        font1 = wx.Font (22, wx.MODERN, wx.NORMAL, wx.NORMAL)


    def OnFileChanged(self, event):
        global data1, ItemInFile
        global fig1, ax1, fig2, ax2
        global checkedItems, showItems
        global data2
        checkedItems = ()
        showItems = set (checkedItems)

        self.m_checkList3.Clear ()
        locale.setlocale (locale.LC_ALL, 'English_United States')
        print ("OnFileChanged")
        CSV_Path = self.m_filePicker1.GetPath ()
        print (type (CSV_Path))
        print ((CSV_Path))

        if CSV_Path[-3:] == 'csv':
            try:
                data1 = pd.read_csv (CSV_Path, skiprows=1)
            # except:
            #     data1 = pd.read_csv(CSV_Path, skiprows=1, encoding = 'gb2312')
            except:
                data1 = pd.read_csv (CSV_Path, skiprows=1, encoding="ISO-8859-1")

            # 将Timestamp 改成 TimeStamp
            try:
                data1['TimeStamp'] = data1['Timestamp']
            except:
                pass

            print (data1['gGridP'].head (10))

            try:
                data1['TestTorque'] = data1['gGridP'] / data1['gCovGenSpd'] * 30 / 3.1415926
                print ('ooooooooooooooooooooooooooooooooooooooooooooooooo')
            except:
                pass

            # 填充空白
            data1 = data1.fillna (-1)
            data2 = data1

            n = len (data1['TimeStamp'])
            print (n)
            # ==========ErrorPoint========== 去除
            print ('finding')
            for i in range (n):
                temp = data1['TimeStamp'][i]
                # print(temp)
                if "ErrorPoint" in temp:
                    print ('find error time')
                    data1 = data1.drop (i)
                    errorPoint = i
                    print (errorPoint)


            # 获取时间序列
            print (data1['TimeStamp'][0])
            print (type (data1['TimeStamp'][0]))
            t0 = pd.to_datetime (data1['TimeStamp'][0], format='%Y-%m-%d/%H:%M:%S.%f')
            t1 = pd.to_datetime (data1['TimeStamp'][1], format='%Y-%m-%d/%H:%M:%S.%f')

            print (t0)
            print (type (t0))


            data1['temp1'] = pd.to_datetime (data1['TimeStamp'], format='%Y-%m-%d/%H:%M:%S.%f', errors='coerce')
            data1 = data1.dropna ()

            data1['temp2'] = pd.to_timedelta (data1['temp1'] - t0)
            print (data1['temp2'].head ())
            data1['time_d_float'] = data1['temp2'].dt.total_seconds ()



            ################### 更新勾选项 ####################

            # 获取所有项
            ItemInFile = data1.columns.values

            #  mat  ################################################################ mat
        elif CSV_Path[-3:] == 'mat':
            train_data = scio.loadmat (CSV_Path)
            try:
                del train_data['__header__']
            except:
                pass

            try:
                del train_data['__version__']
            except:
                pass

            try:
                del train_data['__globals__']
            except:
                pass

            data_len = train_data['Turbine_Controller_Time'].size
            print (data_len)
            train_data2 = train_data.copy ()
            for key in train_data.keys ():
                try:
                    if train_data[key].size == data_len:
                        # train_data2[key].reshape(data_len,1)
                        train_data2[key] = train_data2[key].tolist ()[0]
                    else:
                        print (key)
                        del train_data2[key]
                except:
                    print ("=====")
                    print (key)
                    del train_data2[key]
            data1 = pd.DataFrame.from_dict (train_data2)
            data1.head (10)
            print (data1['Turbine_Controller_Time'].head (10))
            data1['time_d_float'] = data1['Turbine_Controller_Time']  # .dt.total_seconds().round(3)

            ItemInFile = data1.columns.values

        else:  # 不是mat也不是csv
            pass

        temp = np.array ([i.find ('Word') for i in ItemInFile])
        ItemInFileFilter = ItemInFile[temp > 0]
        for item in ItemInFileFilter:
            data1[item + r'.bit0'] = np.bitwise_and (data1[item].astype (np.uint16), 1)/1+0.008
            data1[item + r'.bit1'] = np.bitwise_and (data1[item].astype (np.uint16), 2)/2+0.007
            data1[item + r'.bit2'] = np.bitwise_and (data1[item].astype (np.uint16), 4)/4+0.006
            data1[item + r'.bit3'] = np.bitwise_and (data1[item].astype (np.uint16), 8)/8+0.005
            data1[item + r'.bit4'] = np.bitwise_and (data1[item].astype (np.uint16), 16)/16+0.004
            data1[item + r'.bit5'] = np.bitwise_and (data1[item].astype (np.uint16), 32)/32+0.003
            data1[item + r'.bit6'] = np.bitwise_and (data1[item].astype (np.uint16), 64)/64+0.002
            data1[item + r'.bit7'] = np.bitwise_and (data1[item].astype (np.uint16), 128)/128+0.001

            data1[item + r'.bit8'] = np.bitwise_and (data1[item].astype (np.uint16), 256)/256-0.008
            data1[item + r'.bit9'] = np.bitwise_and (data1[item].astype (np.uint16), 512)/512-0.007
            data1[item + r'.bit10'] = np.bitwise_and (data1[item].astype (np.uint16), 1024)/1024-0.006
            data1[item + r'.bit11'] = np.bitwise_and (data1[item].astype (np.uint16), 2048)/2048-0.005
            data1[item + r'.bit12'] = np.bitwise_and (data1[item].astype (np.uint16), 4096)/4096-0.004
            data1[item + r'.bit13'] = np.bitwise_and (data1[item].astype (np.uint16), 8192)/8192-0.003
            data1[item + r'.bit14'] = np.bitwise_and (data1[item].astype (np.uint16), 16384)/16384-0.002
            data1[item + r'.bit15'] = np.bitwise_and (data1[item].astype (np.uint16), 32768)/32768-0.001

        ################### 更新勾选项 ####################

        # 获取所有项
        ItemInFile = data1.columns.values
        print (type (ItemInFile))
        # 删除


        try:
            ind = np.where (ItemInFile == 'TimeStamp')
            ItemInFile = np.delete (ItemInFile, ind)
        except:
            pass
        try:
            ind = np.where (ItemInFile == 'Timestamp')
            ItemInFile = np.delete (ItemInFile, ind)
        except:
            pass
        try:
            ind = np.where (ItemInFile == 'time_d_float')
            ItemInFile = np.delete (ItemInFile, ind)
        except:
            pass
        try:
            ind = np.where (ItemInFile == 'temp1')
            ItemInFile = np.delete (ItemInFile, ind)
        except:
            pass

        try:
            ind = np.where (ItemInFile == 'temp2')
            ItemInFile = np.delete (ItemInFile, ind)
        except:
            pass
        ItemInFile = np.delete (ItemInFile, ind)
        self.m_checkList3.AppendItems (ItemInFile)
        self.m_checkList3.Update ()



    def OnTextFilter(self, event):
        print ('OnTextFilter')
        fWord = self.m_textCtrl4.GetValue ()
        print ('fWord')
        print (fWord)

        ItemInFile2 = [x for x in ItemInFile if
                       (str.lower(fWord) in str.lower(x))]
        print ('ItemInFile2')
        print (ItemInFile2)

        # 隐藏所有Item
        self.m_checkList3.Clear ()
        # 显示过滤后的Item
        self.m_checkList3.AppendItems (ItemInFile2)
        try:
            self.m_checkList3.SetCheckedStrings (showItems & set (ItemInFile2))
        except:
            pass

        self.m_checkList3.Update ()

    def Box(self, event):
        print ("Box")

    def BoxDClick(self, event):
        print ("BoxDClick")

    def BoxToggled(self, event):
        global checkedNum, checkedNumSave
        global checkedItems, showItems
        offset = 30
        print ("BoxToggled")

        ##### 重写 #####
        # 打勾了哪些
        checkedItems = self.m_checkList3.GetCheckedStrings ()
        print ('checkedItems')
        print (checkedItems, type (checkedItems))
        # 打勾有什么变化
        # 如果打勾的项不属于输出项
        if set (checkedItems) - showItems != set ():
            difItems = set (checkedItems) - showItems
            addOne = 1
            showItems = showItems | (set (checkedItems) - showItems)
        else:  # 取消了勾选
            addOne = -1
            difItems = (showItems & set (self.m_checkList3.GetItems ())) - set (checkedItems)  # 输出里有，列表里有，却没打勾
            showItems = showItems - difItems

        # 变化项
        print ('difItems')
        print (difItems, type (difItems))
        print ("addOne ")
        print (int (addOne))
        print (showItems, type (showItems))

        # fig1, ax1 = plt.subplots(figsize=(10, 5))
        fig1 = plt.figure (1, figsize=(10, 5))
        plt.clf ()
        ax1 = fig1.add_subplot (111)
        plt.cla ()
        for item in showItems:
            ax1.plot (data1['time_d_float'], data1[item], label=item)

        ax1.grid (linestyle='-.', which='major', linewidth=0.5, alpha=1)
        ax1.grid (linestyle='-.', which='minor', linewidth=0.3, alpha=0.8)
        ax1.set_xlabel ('Time')
        ax1.set_title ('CSV File Record Data')
        plt.grid (True)
        plt.style.use ('seaborn-paper')
        # plt_font_set ()
        plt.legend (loc='upper right')
        plt.tight_layout ()
        plt.draw ()
        plt.show ()

        ##绘图
        # plt.rcParams['toolbar'] = 'toolmanager'
        # fig1 = plt.figure (1, figsize=(10, 5))
        #
        # # mpl.backend_tools.add_tools_to_container (fig1.canvas.manager.toolbar, tools=[['foo', ['fullscreen']]])
        # # mpl.backend_tools.add_tools_to_container (fig1.canvas.manager.toolbar, tools=[['foo2', ['grid']]])
        # fig1.canvas.manager.toolbar.add_tool ('quit', 'foo')
        # fig1.canvas.manager.toolbar.add_toolitem ('fullscreen', 'foo', -1, 'fullscreen', 'fullscreen', False)
        #
        # font = {'family': 'SimHei',
        #         'weight': 'bold',
        #         'size': '12'}
        # plt.rc ('font', **font)  # 步骤一（设置字体的更多属性）
        # plt.rc ('axes', unicode_minus=False)  # 步骤二（解决坐标轴负数的负号显示问题）
        # fig1.canvas.manager.toolmanager.add_tool('最大化', showMax)
        # fig1.canvas.manager.toolbar.add_tool('最大化', 'window_state')
        # fig.canvas.manager.window.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint |QtCore.Qt.WindowCloseButtonHint)
        # fig1.canvas.manager.window.setWindowFlags(
        #     QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint )
        # plt.subplots()  #
        # Tu.grid(linestyle='-.', which='major')
        # Tu.grid(linestyle='-.', which='minor', linewidth=0.3, alpha=0.9)
        # liney = np.linspace(0, 200, 200)
        # linex0 = np.ones(200) * 0
        # linex1 = np.ones(200) * 1
        # plt.plot(linex0, liney, color="green", linewidth=1.5, linestyle="-.", label="T0")
        # plt.plot(linex1, liney, color="green", linewidth=1.5, linestyle="-.", label="T1")
        # ax = plt.gca()
        # cursor = Cursor(ax, horizOn=False, vertOn=True, useblit=False, color='grey')
        # plt.ylabel()

    def PlotBottonClick(self, event):
        print ("PlotBottonClick")

    def mOnMenuSelection2(self, event):
        dlg = wx.MessageDialog (None,
                                "1.支持csv或mat文件格式\n2.csv文件格式，第二行为表头，第三行开始为数据。\n3.绘图数据可多选。",
                                u"确认", wx.YES_DEFAULT | wx.ICON_QUESTION)
        if dlg.ShowModal () == wx.ID_YES:
            self.Close (True)
        dlg.Destroy ()

    def mOnMenuSelection1(self, event):
        dlg = wx.MessageDialog (None, u"上海电气风电集团 电气COE\n版本:V1.1", u"确认", wx.YES_DEFAULT | wx.ICON_QUESTION)
        if dlg.ShowModal () == wx.ID_YES:
            self.Close (True)
        dlg.Destroy ()

    def OnButtonClick(self, event):
        try:
            xmin = float (self.m_textCtrl_xmin.GetValue ())
        except:
            xmin = -50000

        try:
            xmax = float (self.m_textCtrl_xmax.GetValue ())
        except:
            xmax = 50000
        print ([xmin, xmax])

        fig1 = plt.figure (1, figsize=(10, 5))
        plt.clf ()
        ax1 = fig1.add_subplot (111)
        plt.cla ()
        global data2
        data2 = data1
        data2 = data2[data1['time_d_float'] <= xmax]
        data2 = data2[data2['time_d_float'] >= xmin]
        for item in showItems:
            ax1.plot (data2['time_d_float'], data2[item], label=item)

        ax1.grid (linestyle='-.', linewidth=0.5, alpha=1)
        ax1.set_xlabel ('Time')
        ax1.set_title ('CSV File Record Data')
        plt.grid (True)
        plt.style.use ('seaborn-paper')
        # plt_font_set ()
        plt.legend (loc='upper right')
        plt.tight_layout ()
        plt.draw ()
        plt.show ()

    def OnButtonClick_FFT(self, event):
        print ("FFT")
        from FFTtest import myfft
        try:
            data3 = data2
        except:
            data3 = data1
        # data3 = data3.fillna (-1)
        data3 = data3.dropna ()
        data3['t_diff'] = data3['time_d_float'].diff ()
        min_diff = data3['t_diff'].min ()
        if (min_diff < 0.022) and (min_diff > 0.018):
            min_diff = 0.02
        if (min_diff < 0.012) and (min_diff > 0.008):
            min_diff = 0.01
        print ("min_diff = ", min_diff)

        temp_end_time = data3['time_d_float'].iloc[-1]
        temp_start_time = data3['time_d_float'].iloc[0]
        print ("temp_start_time = ", temp_start_time)
        print ("temp_end_time = ", temp_end_time)

        time_sec = np.linspace (temp_start_time, temp_end_time,
                                round ((temp_end_time - temp_start_time) / min_diff) + 1)
        df_fft_50Hz = pd.DataFrame ({"time_d_float": time_sec}).round (3)
        # df_fft_50Hz['my_data'] = 'Nan'
        df_fft_50Hz.head (56)
        # 将50Hz的表与原来的表合并
        df_fft_merge = pd.merge (data3, df_fft_50Hz, on='time_d_float', how='outer')
        df_fft3 = df_fft_merge.sort_values (by='time_d_float')
        df_fft3.index = range (len (df_fft3))
        df_fft3.set_index ('time_d_float', inplace=True)
        for item in showItems:
            df_fft3[item].interpolate (method='linear', limit_direction='forward', axis=0, limit=None,
                                       limit_area=None, downcast=None, inplace=True)
        df_fft_merge2 = pd.merge (df_fft_50Hz, df_fft3, on='time_d_float', how='inner')
        f_sample = round (1 / min_diff)

        fig2 = plt.figure (2, figsize=(10, 5))
        plt.clf ()
        ax2 = fig2.add_subplot (111)
        plt.cla ()

        for item in showItems:
            # ax1.plot (data2['time_d_float'], data2[item], label=item)
            [F1, P1, Fs__len, rms_value] = myfft (data3['time_d_float'].values, data3[item].values, f_sample)
            print ('Fs__len = %s' % Fs__len)
            len_y = len (P1)
            x = F1
            print ('F1')
            print (F1)
            _y = [P1[-1]] * len_y
            ax2.plot (x, P1, label=item)

        ax2.set_title ('Data - Frequency Domain ')
        ax2.set_xlabel ('Frequency')
        ax2.set_ylabel ('Mag(相峰值)(指数)')
        ax2.set_yscale ("log")
        ax2.grid (linestyle='-.', linewidth=0.5, alpha=1)

        plt.grid (True)
        plt.style.use ('seaborn-paper')
        # plt_font_set ()
        plt.legend (loc='upper right')
        plt.tight_layout ()
        plt.draw ()
        plt.show ()



'''end of file'''
