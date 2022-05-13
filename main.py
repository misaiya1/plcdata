#!/usr/bin/env python
# _*_ coding:utf-8 _*_


import wx
from ExcelOperator import MyFrame


def main():
    app = wx.App ()
    frame = MyFrame (None)
    frame.Show ()
    # frame.ShowFullScreen(True)
    # wx.CallLater(5000, frame.ShowFullScreen, False)
    app.MainLoop ()
    # del app
    # del frame
    # save_all()


if __name__ == '__main__':
    main ()
