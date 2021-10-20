#!/usr/bin/env python
# _*_ coding:utf-8 _*_
from UI.noname import plc
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

import wx
import wx.xrc
import locale



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


def func_cycle(x, e, x_o, y_o):
    return np.sqrt((e ** 2 - (x - x_o) ** 2)) + y_o


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
        global data1
        locale.setlocale(locale.LC_ALL, 'English_United States')
        print("OnFileChanged")
        CSV_Path = self.m_filePicker1.GetPath()
        print(type(CSV_Path))
        print((CSV_Path))

        # f = open(CSV_Path)
        # data1 = pd.read_csv(f, error_bad_lines=False, engine='python', skiprows=1)


        try:
            data1 = pd.read_csv(CSV_Path, skiprows=1)
        # except:
        #     data1 = pd.read_csv(CSV_Path, skiprows=1, encoding = 'gb2312')
        except:
            data1 = pd.read_csv(CSV_Path, skiprows=1, encoding = "ISO-8859-1")

        # 将Timestamp 改成 TimeStamp
        try:
            data1['TimeStamp'] = data1['Timestamp']
        except:
            pass

        # 填充空白
        data1 = data1.fillna(-1)
        # data1['TimeStamp'].head(5)

        n = len(data1['TimeStamp'])
        print(n)
        #==========ErrorPoint========== 去除
        print('finding')
        for i in range(n):
            temp = data1['TimeStamp'][i]
            print(temp)
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
        dt = pd.to_timedelta(t1 - t0)
        dtt = dt.total_seconds()
        print(dt)
        print(dtt)




        data1['temp1'] = pd.to_datetime(data1['TimeStamp'], format='%Y-%m-%d/%H:%M:%S.%f', errors='coerce')
        data1 = data1.dropna()

        data1['temp2'] = pd.to_timedelta(data1['temp1'] - t0)
        print(data1['temp2'].head())
        data1['time_d_float'] = data1['temp2'].dt.total_seconds()

        tt1 = data1['temp2']
        ttt1 = data1['time_d_float']
        # except:
        #     pass


        ################### 更新勾选项 ####################
        #print(data1.columns.values)

        # 获取所有项
        temp = data1.columns.values
        print(type(temp))
        # 删除

        ind = np.where('TimeStamp')
        temp = np.delete(temp,ind)

        try:
            ind = np.where('Timestamp')
            temp = np.delete(temp, ind)
        except:
            pass

        self.m_checkList3.AppendItems(temp)
        self.m_checkList3.Update()

        # 绘图部分
        global Tu
        plt.figure()
        Tu = plt.subplot(1, 1, 1)  # 功率图


    def BoxToggled(self, event):
        print("BoxToggled")
        inx = self.m_checkList3.GetCheckedItems()
        print(inx)
        print(type(inx))

        checkedItems = self.m_checkList3.GetCheckedStrings()
        plt.clf()
        Tu.grid(linestyle='-.', which='major')
        #Tu.set_title('Scope - Power')

        # miloc = plt.MultipleLocator(50)
        # maloc = plt.MultipleLocator(100)
        # Tu.xaxis.set_minor_locator(miloc)
        # Tu.yaxis.set_minor_locator(maloc)
        Tu.grid(linestyle='-.', which='minor', linewidth=0.3, alpha=0.9)
        for item in checkedItems:
            plt.plot(data1['time_d_float'], data1[item], label=item)

        Tu.set_xlabel('time[sec]')
        Tu.legend()
        Tu.grid()
        plt.grid()
        plt.legend()
        plt.show()




    def PlotBottonClick(self, event):
        print("PlotBottonClick")

    # def SetFocus(self, event):
    #     print("SetFocus")
    #
    def mOnMenuSelection2(self, event):
        dlg = wx.MessageDialog(None,
                               "1.csv文件格式，第二行为表头，第三行开始为数据。\n2.绘图数据可多选。",
                               u"确认", wx.YES_DEFAULT | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            self.Close(True)
        dlg.Destroy()

    def mOnMenuSelection1(self, event):
        dlg = wx.MessageDialog(None, u"上海电气风电集团 电气COE\n版本:V1.0", u"确认", wx.YES_DEFAULT | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            self.Close(True)
        dlg.Destroy()

def save_all():
    pass


'''end of file'''
