#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from UI.noname import plc

import matplotlib as mpl
import matplotlib.pyplot as plt
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


def isset(v):
    try:
        type(eval(v))
    except:
        return 0
    else:
        return 1


def csv_to_dataframe(name):
    return


def func_cycle(x, e, x_o, y_o):
    return np.sqrt((e ** 2 - (x - x_o) ** 2)) + y_o


# class showMax(ToolToggleBase):
#     description = '最大化切换'
#
#     def enable(self, *args, **kwargs):
#         fig.canvas.manager.window.showMaximized()
#
#     def disable(self, *args, **kwargs):
#         fig.canvas.manager.window.showNormal()


class MyFrame(plc):
    locale.getlocale()
    ''' 创建输出路径  '''

    # global cwd
    # cwd = os.getcwd()
    # print(cwd)
    # global outputFolderName
    #
    # outputFolderName = cwd + r'\fig_save'  # + datetime.datetime.now().strftime('%Y.%m.%d.%H.%M')
    # outPathExists = os.path.exists(outputFolderName)
    # if not outPathExists:
    #     os.makedirs(outputFolderName)
    #     print(outputFolderName + ' 路径创建成功')
    # else:
    #     print(outputFolderName + ' 路径已存在')

    def __init__(self, parent):
        plc.__init__(self, parent)

        wx.Frame.SetBackgroundColour(self, 'Write')  # ???
        font1 = wx.Font(22, wx.MODERN, wx.NORMAL, wx.NORMAL)
        # self.m_staticText15.SetFont(font1)
        # self.m_button.SetFont(font1)
        # self.m_button2.SetFont(font1)
        # self.m_staticText16.SetFont(font1)

    # def m_buttonOnButtonClick(self, event):
    #     print("m_buttonOnButtonClick")
    def OnFileChanged(self, event):
        global data1, ItemInFile
        self.m_checkList3.Clear()
        locale.setlocale(locale.LC_ALL, 'English_United States')
        print("OnFileChanged")
        CSV_Path = self.m_filePicker1.GetPath()
        print(type(CSV_Path))
        print((CSV_Path))

        if CSV_Path[-3:] == 'csv':
            try:
                data1 = pd.read_csv(CSV_Path, skiprows=1)
            # except:
            #     data1 = pd.read_csv(CSV_Path, skiprows=1, encoding = 'gb2312')
            except:
                data1 = pd.read_csv(CSV_Path, skiprows=1, encoding="ISO-8859-1")

            # 将Timestamp 改成 TimeStamp
            try:
                data1['TimeStamp'] = data1['Timestamp']
            except:
                pass

            print(data1['gGridP'].head(10))

            try:
                data1['TestTorque'] = data1['gGridP'] / data1['gCovGenSpd'] * 30 / 3.1415926
                print('ooooooooooooooooooooooooooooooooooooooooooooooooo')
            except:
                pass

            # 填充空白
            data1 = data1.fillna(-1)
            # data1['TimeStamp'].head(5)

            n = len(data1['TimeStamp'])
            print(n)
            # ==========ErrorPoint========== 去除
            print('finding')
            for i in range(n):
                temp = data1['TimeStamp'][i]
                # print(temp)
                if "ErrorPoint" in temp:
                    print('find error time')
                    data1 = data1.drop(i)
                    errorPoint = i
                    print(errorPoint)
                    print('=======================')
                    # print(data1['TimeStamp'][1540])
                    # print(data1['TimeStamp'][1541])
                    # print(data1['TimeStamp'][1542])
                    # print(data1['TimeStamp'][1543])
                    # print(data1['TimeStamp'][1544])
                    print('=======================')

            # 获取时间序列
            print(data1['TimeStamp'][0])
            print(type(data1['TimeStamp'][0]))
            t0 = pd.to_datetime(data1['TimeStamp'][0], format='%Y-%m-%d/%H:%M:%S.%f')
            t1 = pd.to_datetime(data1['TimeStamp'][1], format='%Y-%m-%d/%H:%M:%S.%f')

            print(t0)
            print(type(t0))
            # dt = pd.to_timedelta(t1 - t0)
            # dtt = dt.total_seconds()
            # print(dt)
            # print(dtt)

            data1['temp1'] = pd.to_datetime(data1['TimeStamp'], format='%Y-%m-%d/%H:%M:%S.%f', errors='coerce')
            data1 = data1.dropna()

            data1['temp2'] = pd.to_timedelta(data1['temp1'] - t0)
            print(data1['temp2'].head())
            data1['time_d_float'] = data1['temp2'].dt.total_seconds()

            # tt1 = data1['temp2']
            # ttt1 = data1['time_d_float']
            # except:
            #     pass

            ################### 更新勾选项 ####################
            # print(data1.columns.values)

            # 获取所有项
            ItemInFile = data1.columns.values
            print(type(ItemInFile))
            # 删除

            ind = np.where('TimeStamp')
            ItemInFile = np.delete(ItemInFile, ind)

            try:
                ind = np.where('Timestamp')
                ItemInFile = np.delete(ItemInFile, ind)
            except:
                pass

            try:
                ind = np.where('temp1')
                ItemInFile = np.delete(ItemInFile, ind)
            except:
                pass

            try:
                ind = np.where('temp2')
                ItemInFile = np.delete(ItemInFile, ind)
            except:
                pass
            #  mat  ################################################################ mat
        elif CSV_Path[-3:] == 'mat':
            train_data = scio.loadmat(CSV_Path)
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
            print(data_len)
            train_data2 = train_data.copy()
            for key in train_data.keys():
                try:
                    if train_data[key].size == data_len:
                        # train_data2[key].reshape(data_len,1)
                        train_data2[key] = train_data2[key].tolist()[0]
                    else:
                        print(key)
                        del train_data2[key]
                except:
                    print("=====")
                    print(key)
                    del train_data2[key]
            data1 = pd.DataFrame.from_dict(train_data2)
            data1.head(10)
            print(data1['Turbine_Controller_Time'].head(10))
            data1['time_d_float'] = data1['Turbine_Controller_Time']  # .dt.total_seconds().round(3)

            ItemInFile = data1.columns.values

        else:  # 不是mat也不是csv
            pass

        self.m_checkList3.AppendItems(ItemInFile)
        self.m_checkList3.Update()

        # 绘图部分

    def OnTextFilter(self, event):
        print('OnTextFilter')
        fWord = self.m_textCtrl4.GetValue()
        print(fWord)
        ItemInFile2 = ItemInFile
        print(type(ItemInFile2))
        ItemInFile2 = [x for x in ItemInFile if
                       ( fWord in x)]

        # 隐藏所有Item

        # 显示过滤后的Item
        self.m_checkList3.AppendItems(ItemInFile2)
        self.m_checkList3.Update()
    def Box(self, event):
        print("Box")

    def BoxDClick(self, event):
        print("BoxDClick")

    def BoxToggled2(self, event):
        global fig1
        global checkedItems, checkedItemSave
        checkedItemSave = ()
        global checkedNum, checkedNumSave
        offset = 30
        print("BoxToggled")

        plt.rcParams['toolbar'] = 'toolmanager'
        fig1 = plt.figure(1, figsize=(10, 5))
        mpl.backend_tools.add_tools_to_container(fig1.canvas.manager.toolbar, tools=[['foo', ['fullscreen']]])
        # fig1.canvas.manager.toolmanager.add_tool('最大化', showMax)
        # fig1.canvas.manager.toolbar.add_tool('最大化', 'window_state')
        # fig.canvas.manager.window.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint |QtCore.Qt.WindowCloseButtonHint)
        # fig1.canvas.manager.window.setWindowFlags(
        #     QtCore.Qt.CustomizeWindowHint | QtCore.Qt.WindowTitleHint )

        # 打勾了哪些
        checkedItems = self.m_checkList3.GetCheckedStrings()
        print(checkedItems, type(checkedItems))
        # print(checkedItems[0])
        checkedItemsidx = self.m_checkList3.GetCheckedItems()
        print(checkedItemsidx, type(checkedItemsidx))
        # 打勾了几个
        checkedNum = len(checkedItemsidx)

        # 打勾有什么变化
        difTup = set(checkedItemSave) ^ set(checkedItems)
        print(difTup)
        addOne = 0
        if set(difTup).issubset(set(checkedItems)):
            addOne = 1
        if set(difTup).issubset(set(checkedItemSave)):
            addOne = 0
        print("addOne ")
        print(int(addOne))

        if checkedNum == 1:
            print('item1')
            host = host_subplot(111, axes_class=AA.Axes)
            plt.subplots_adjust(right=0.75)

            item = checkedItems[0]
            host.set_xlabel('time[sec]')
            host.set_ylabel(item)
            p1, = host.plot(data1['time_d_float'], data1[item], label=item)

            host.axis["left"].label.set_color(p1.get_color())
            host.legend()

            plt.grid()
            plt.draw()
            plt.show()

        elif checkedNum == 0:
            print('item0')

            plt.close()

        elif checkedNum == 2:
            print('item2')
            # 如果 增加到2 ，则右侧加个轴加个图
            # 如果 减小到2 ，则删除一个图和轴

        else:
            pass

    def BoxToggled(self, event):
        # plt.close('all')
        plt.clf()
        font = {'family': 'SimHei',
                'weight': 'bold',
                'size': '12'}
        plt.rc('font', **font)  # 步骤一（设置字体的更多属性）
        plt.rc('axes', unicode_minus=False)  # 步骤二（解决坐标轴负数的负号显示问题）
        # plt.subplots()  #

        print("BoxToggled")
        inx = self.m_checkList3.GetCheckedItems()
        print(inx)
        print(type(inx))

        global checkedItems
        checkedItems = self.m_checkList3.GetCheckedStrings()
        print(checkedItems)

        # Tu.grid(linestyle='-.', which='major')
        # Tu.grid(linestyle='-.', which='minor', linewidth=0.3, alpha=0.9)
        for item in checkedItems:
            plt.plot(data1['time_d_float'], data1[item], label=item)

        # liney = np.linspace(0, 200, 200)
        # linex0 = np.ones(200) * 0
        # linex1 = np.ones(200) * 1
        # plt.plot(linex0, liney, color="green", linewidth=1.5, linestyle="-.", label="T0")
        # plt.plot(linex1, liney, color="green", linewidth=1.5, linestyle="-.", label="T1")

        plt.legend(loc='upper right')
        plt.xlabel('Time')

        # ax = plt.gca()
        # cursor = Cursor(ax, horizOn=False, vertOn=True, useblit=False, color='grey')
        # plt.ylabel()
        plt.title('CSV File Record Data')
        plt.style.use('seaborn-paper')
        plt.grid(True)
        plt.tight_layout()
        plt.show()

        checkedItemSave = checkedItems
        checkedNumSave = checkedNum

        # plt.clf()
        # Tu.grid(linestyle='-.', which='major')
        # #Tu.set_title('Scope - Power')
        #
        # # miloc = plt.MultipleLocator(50)
        # # maloc = plt.MultipleLocator(100)
        # # Tu.xaxis.set_minor_locator(miloc)
        # # Tu.yaxis.set_minor_locator(maloc)
        # Tu.grid(linestyle='-.', which='minor', linewidth=0.3, alpha=0.9)
        # for item in checkedItems:
        #     plt.plot(data1['time_d_float'], data1[item], label=item)
        #
        # Tu.set_xlabel('time[sec]')
        # Tu.legend()
        # Tu.grid()
        # plt.grid()
        # plt.legend()
        # plt.show()

    def PlotBottonClick(self, event):
        print("PlotBottonClick")

    # def SetFocus(self, event):
    #     print("SetFocus")
    #
    def mOnMenuSelection2(self, event):
        dlg = wx.MessageDialog(None,
                               "1.支持csv或mat文件格式\n2.csv文件格式，第二行为表头，第三行开始为数据。\n3.绘图数据可多选。",
                               u"确认", wx.YES_DEFAULT | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            self.Close(True)
        dlg.Destroy()

    def mOnMenuSelection1(self, event):
        dlg = wx.MessageDialog(None, u"上海电气风电集团 电气COE\n版本:V1.1", u"确认", wx.YES_DEFAULT | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            self.Close(True)
        dlg.Destroy()


def save_all():
    pass


'''end of file'''
