# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Sep  8 2010)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx

###########################################################################
## Class FirstRun
###########################################################################

class FirstRun ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 373,213 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"欢迎使用MoneySaver365！这是您初次使用，请选择存钱计划：", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )
		bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		sbSizer1 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"计划" ), wx.VERTICAL )
		
		self.plan365 = wx.RadioButton( self, wx.ID_ANY, u"365天，存1-365元，共66795元", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.plan365, 0, wx.ALL, 5 )
		
		self.plan182 = wx.RadioButton( self, wx.ID_ANY, u"365天，存1-182.5元，共33397.5元", wx.DefaultPosition, wx.DefaultSize, 0 )
		sbSizer1.Add( self.plan182, 0, wx.ALL, 5 )
		
		bSizer1.Add( sbSizer1, 1, wx.EXPAND, 5 )
		
		gSizer4 = wx.GridSizer( 2, 2, 0, 0 )
		
		self.fst_ok = wx.Button( self, wx.ID_ANY, u"确定", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.fst_ok, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.fst_exit = wx.Button( self, wx.ID_ANY, u"退出", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer4.Add( self.fst_exit, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer1.Add( gSizer4, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.plan365.Bind( wx.EVT_RADIOBUTTON, self.plan365choose )
		self.plan182.Bind( wx.EVT_RADIOBUTTON, self.plan182choose )
		self.fst_ok.Bind( wx.EVT_BUTTON, self.fst_ok_click )
		self.fst_exit.Bind( wx.EVT_BUTTON, self.fst_exit_click )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def plan365choose( self, event ):
		event.Skip()
	
	def plan182choose( self, event ):
		event.Skip()
	
	def fst_ok_click( self, event ):
		event.Skip()
	
	def fst_exit_click( self, event ):
		event.Skip()
	

###########################################################################
## Class MainSaver
###########################################################################

class MainSaver ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 179,98 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer4 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"欢迎使用MoneySaver！", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer4.Add( self.m_staticText2, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer5 = wx.GridSizer( 2, 2, 0, 0 )
		
		self.start_random = wx.Button( self, wx.ID_ANY, u"开始随机", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.start_random, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.see_saved = wx.Button( self, wx.ID_ANY, u"查看已存", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer5.Add( self.see_saved, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer4.Add( gSizer5, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer4 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.start_random.Bind( wx.EVT_BUTTON, self.start_random_click )
		self.see_saved.Bind( wx.EVT_BUTTON, self.see_saved_click )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def start_random_click( self, event ):
		event.Skip()
	
	def see_saved_click( self, event ):
		event.Skip()
	

###########################################################################
## Class SaveEnd
###########################################################################

class SaveEnd ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 306,133 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer5 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText4 = wx.StaticText( self, wx.ID_ANY, u"欢迎使用MoneySaver！存款计划已结束。", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText4.Wrap( -1 )
		bSizer5.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer7 = wx.GridSizer( 2, 2, 0, 0 )
		
		self.restart = wx.Button( self, wx.ID_ANY, u"重开计划", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.restart, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.end_exit = wx.Button( self, wx.ID_ANY, u"退出程序", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer7.Add( self.end_exit, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer5.Add( gSizer7, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer5 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.restart.Bind( wx.EVT_BUTTON, self.restart_click )
		self.end_exit.Bind( wx.EVT_BUTTON, self.end_exit_click )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def restart_click( self, event ):
		event.Skip()
	
	def end_exit_click( self, event ):
		event.Skip()
	

###########################################################################
## Class Accept
###########################################################################

class Accept ( wx.Dialog ):
	
	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 281,91 ), style = wx.DEFAULT_DIALOG_STYLE )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer7 = wx.BoxSizer( wx.VERTICAL )
		
		self.random_text = wx.StaticText( self, wx.ID_ANY, u"今天随机产生的存款金额为￥0元，能否接受？", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.random_text.Wrap( -1 )
		bSizer7.Add( self.random_text, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )
		
		gSizer9 = wx.GridSizer( 2, 2, 0, 0 )
		
		self.accept_ok = wx.Button( self, wx.ID_ANY, u"可以", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.accept_ok, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.accept_no = wx.Button( self, wx.ID_ANY, u"不能", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer9.Add( self.accept_no, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		bSizer7.Add( gSizer9, 1, wx.EXPAND, 5 )
		
		self.SetSizer( bSizer7 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.Bind( wx.EVT_INIT_DIALOG, self.accept_show )
		self.accept_ok.Bind( wx.EVT_BUTTON, self.accept_ok_click )
		self.accept_no.Bind( wx.EVT_BUTTON, self.accept_no_click )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def accept_show( self, event ):
		event.Skip()
	
	def accept_ok_click( self, event ):
		event.Skip()
	
	def accept_no_click( self, event ):
		event.Skip()
	

