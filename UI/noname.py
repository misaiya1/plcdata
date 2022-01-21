# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Jul 11 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class plc
###########################################################################

class plc ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"B&R buffer plot", pos = wx.DefaultPosition, size = wx.Size( 800,600 ), style = wx.CAPTION|wx.CLOSE_BOX|wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		
		gSizer3 = wx.GridSizer( 1, 1, 0, 0 )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer5.SetMinSize( wx.Size( 800,200 ) ) 
		self.m_staticText15 = wx.StaticText( self, wx.ID_ANY, u".csv/mat文件路径", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText15.Wrap( -1 )
		
		self.m_staticText15.SetFont( wx.Font( 18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "宋体" ) )
		
		bSizer5.Add( self.m_staticText15, 0, wx.ALL|wx.EXPAND, 5 )
		
		self.m_filePicker1 = wx.FilePickerCtrl( self, wx.ID_ANY, wx.EmptyString, u"Select a file", u"*.*", wx.DefaultPosition, wx.DefaultSize, wx.FLP_DEFAULT_STYLE )
		bSizer5.Add( self.m_filePicker1, 0, wx.ALL|wx.EXPAND, 5 )
		
		wSizer1 = wx.WrapSizer( wx.HORIZONTAL, wx.WRAPSIZER_DEFAULT_FLAGS )
		
		self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"过滤", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText3.Wrap( -1 )
		
		wSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )
		
		self.m_textCtrl4 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		wSizer1.Add( self.m_textCtrl4, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		bSizer5.Add( wSizer1, 0, wx.EXPAND, 5 )
		
		self.m_scrolledWindow2 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
		self.m_scrolledWindow2.SetScrollRate( 5, 5 )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )
		
		m_checkList3Choices = []
		self.m_checkList3 = wx.CheckListBox( self.m_scrolledWindow2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_checkList3Choices, 0 )
		bSizer3.Add( self.m_checkList3, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.m_scrolledWindow2.SetSizer( bSizer3 )
		self.m_scrolledWindow2.Layout()
		bSizer3.Fit( self.m_scrolledWindow2 )
		bSizer5.Add( self.m_scrolledWindow2, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		gSizer3.Add( bSizer5, 0, wx.EXPAND, 5 )
		
		
		self.SetSizer( gSizer3 )
		self.Layout()
		self.m_menubar1 = wx.MenuBar( 0 )
		self.m_menu5 = wx.Menu()
		self.m_menuItem2 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"说明信息", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.Append( self.m_menuItem2 )
		
		self.m_menuItem3 = wx.MenuItem( self.m_menu5, wx.ID_ANY, u"版本信息", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu5.Append( self.m_menuItem3 )
		
		self.m_menubar1.Append( self.m_menu5, u"说明" ) 
		
		self.SetMenuBar( self.m_menubar1 )
		
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_filePicker1.Bind( wx.EVT_FILEPICKER_CHANGED, self.OnFileChanged )
		self.m_filePicker1.Bind( wx.EVT_SET_FOCUS, self.SetFocus )
		self.m_textCtrl4.Bind( wx.EVT_TEXT, self.OnTextFilter )
		self.m_checkList3.Bind( wx.EVT_LISTBOX, self.Box )
		self.m_checkList3.Bind( wx.EVT_LISTBOX_DCLICK, self.BoxDClick )
		self.m_checkList3.Bind( wx.EVT_CHECKLISTBOX, self.BoxToggled )
		self.Bind( wx.EVT_MENU, self.mOnMenuSelection2, id = self.m_menuItem2.GetId() )
		self.Bind( wx.EVT_MENU, self.mOnMenuSelection1, id = self.m_menuItem3.GetId() )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def OnFileChanged( self, event ):
		event.Skip()
	
	def SetFocus( self, event ):
		event.Skip()
	
	def OnTextFilter( self, event ):
		event.Skip()
	
	def Box( self, event ):
		event.Skip()
	
	def BoxDClick( self, event ):
		event.Skip()
	
	def BoxToggled( self, event ):
		event.Skip()
	
	def mOnMenuSelection2( self, event ):
		event.Skip()
	
	def mOnMenuSelection1( self, event ):
		event.Skip()
	

