///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Jul 11 2018)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#include "noname.h"

///////////////////////////////////////////////////////////////////////////

plc::plc( wxWindow* parent, wxWindowID id, const wxString& title, const wxPoint& pos, const wxSize& size, long style ) : wxFrame( parent, id, title, pos, size, style )
{
	this->SetSizeHints( wxDefaultSize, wxDefaultSize );
	
	wxGridSizer* gSizer3;
	gSizer3 = new wxGridSizer( 1, 1, 0, 0 );
	
	wxBoxSizer* bSizer5;
	bSizer5 = new wxBoxSizer( wxVERTICAL );
	
	bSizer5->SetMinSize( wxSize( 800,200 ) ); 
	m_staticText15 = new wxStaticText( this, wxID_ANY, wxT("1.浏览csv/mat文件路径"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_HORIZONTAL );
	m_staticText15->Wrap( -1 );
	m_staticText15->SetFont( wxFont( 18, wxFONTFAMILY_DEFAULT, wxFONTSTYLE_NORMAL, wxFONTWEIGHT_NORMAL, false, wxT("宋体") ) );
	
	bSizer5->Add( m_staticText15, 0, wxALL|wxEXPAND, 5 );
	
	m_filePicker1 = new wxFilePickerCtrl( this, wxID_ANY, wxEmptyString, wxT("1.浏览文件"), wxT("*.*"), wxDefaultPosition, wxDefaultSize, wxFLP_DEFAULT_STYLE );
	bSizer5->Add( m_filePicker1, 0, wxALL|wxEXPAND, 5 );
	
	m_staticText151 = new wxStaticText( this, wxID_ANY, wxT("2.勾选信号"), wxDefaultPosition, wxDefaultSize, wxALIGN_CENTER_HORIZONTAL );
	m_staticText151->Wrap( -1 );
	m_staticText151->SetFont( wxFont( 18, wxFONTFAMILY_DEFAULT, wxFONTSTYLE_NORMAL, wxFONTWEIGHT_NORMAL, false, wxT("宋体") ) );
	
	bSizer5->Add( m_staticText151, 0, wxALL|wxEXPAND, 5 );
	
	wxWrapSizer* wSizer1;
	wSizer1 = new wxWrapSizer( wxHORIZONTAL, wxWRAPSIZER_DEFAULT_FLAGS );
	
	m_staticText3 = new wxStaticText( this, wxID_ANY, wxT("过滤"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText3->Wrap( -1 );
	wSizer1->Add( m_staticText3, 0, wxALL, 5 );
	
	m_textCtrl4 = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	wSizer1->Add( m_textCtrl4, 1, wxALL|wxEXPAND, 5 );
	
	m_staticText32 = new wxStaticText( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText32->Wrap( -1 );
	wSizer1->Add( m_staticText32, 0, wxALL, 5 );
	
	m_staticText31 = new wxStaticText( this, wxID_ANY, wxT("x_min"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText31->Wrap( -1 );
	wSizer1->Add( m_staticText31, 0, wxALL, 5 );
	
	m_textCtrl_xmin = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	wSizer1->Add( m_textCtrl_xmin, 0, wxALL, 5 );
	
	m_staticText311 = new wxStaticText( this, wxID_ANY, wxT("x_max"), wxDefaultPosition, wxDefaultSize, 0 );
	m_staticText311->Wrap( -1 );
	wSizer1->Add( m_staticText311, 0, wxALL, 5 );
	
	m_textCtrl_xmax = new wxTextCtrl( this, wxID_ANY, wxEmptyString, wxDefaultPosition, wxDefaultSize, 0 );
	wSizer1->Add( m_textCtrl_xmax, 0, wxALL, 5 );
	
	m_button1 = new wxButton( this, wxID_ANY, wxT("3.过滤x轴范围"), wxDefaultPosition, wxDefaultSize, 0 );
	wSizer1->Add( m_button1, 0, wxALL, 5 );
	
	m_button_FFT = new wxButton( this, wxID_ANY, wxT("4.对该时段FFT"), wxDefaultPosition, wxDefaultSize, 0 );
	wSizer1->Add( m_button_FFT, 0, wxALL, 5 );
	
	
	bSizer5->Add( wSizer1, 0, wxEXPAND, 5 );
	
	m_scrolledWindow2 = new wxScrolledWindow( this, wxID_ANY, wxDefaultPosition, wxDefaultSize, wxHSCROLL|wxVSCROLL );
	m_scrolledWindow2->SetScrollRate( 5, 5 );
	wxBoxSizer* bSizer3;
	bSizer3 = new wxBoxSizer( wxVERTICAL );
	
	wxArrayString m_checkList3Choices;
	m_checkList3 = new wxCheckListBox( m_scrolledWindow2, wxID_ANY, wxDefaultPosition, wxDefaultSize, m_checkList3Choices, 0 );
	bSizer3->Add( m_checkList3, 1, wxALL|wxEXPAND, 5 );
	
	
	m_scrolledWindow2->SetSizer( bSizer3 );
	m_scrolledWindow2->Layout();
	bSizer3->Fit( m_scrolledWindow2 );
	bSizer5->Add( m_scrolledWindow2, 1, wxALL|wxEXPAND, 5 );
	
	
	gSizer3->Add( bSizer5, 0, wxEXPAND, 5 );
	
	
	this->SetSizer( gSizer3 );
	this->Layout();
	m_menubar1 = new wxMenuBar( 0 );
	m_menu5 = new wxMenu();
	wxMenuItem* m_menuItem2;
	m_menuItem2 = new wxMenuItem( m_menu5, wxID_ANY, wxString( wxT("说明信息") ) , wxEmptyString, wxITEM_NORMAL );
	m_menu5->Append( m_menuItem2 );
	
	wxMenuItem* m_menuItem3;
	m_menuItem3 = new wxMenuItem( m_menu5, wxID_ANY, wxString( wxT("版本信息") ) , wxEmptyString, wxITEM_NORMAL );
	m_menu5->Append( m_menuItem3 );
	
	m_menubar1->Append( m_menu5, wxT("说明") ); 
	
	this->SetMenuBar( m_menubar1 );
	
	
	this->Centre( wxBOTH );
	
	// Connect Events
	m_filePicker1->Connect( wxEVT_COMMAND_FILEPICKER_CHANGED, wxFileDirPickerEventHandler( plc::OnFileChanged ), NULL, this );
	m_filePicker1->Connect( wxEVT_SET_FOCUS, wxFocusEventHandler( plc::SetFocus ), NULL, this );
	m_textCtrl4->Connect( wxEVT_COMMAND_TEXT_UPDATED, wxCommandEventHandler( plc::OnTextFilter ), NULL, this );
	m_button1->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( plc::OnButtonClick ), NULL, this );
	m_button_FFT->Connect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( plc::OnButtonClick_FFT ), NULL, this );
	m_checkList3->Connect( wxEVT_COMMAND_LISTBOX_SELECTED, wxCommandEventHandler( plc::Box ), NULL, this );
	m_checkList3->Connect( wxEVT_COMMAND_LISTBOX_DOUBLECLICKED, wxCommandEventHandler( plc::BoxDClick ), NULL, this );
	m_checkList3->Connect( wxEVT_COMMAND_CHECKLISTBOX_TOGGLED, wxCommandEventHandler( plc::BoxToggled ), NULL, this );
	m_menu5->Bind(wxEVT_COMMAND_MENU_SELECTED, wxCommandEventHandler( plc::mOnMenuSelection2 ), this, m_menuItem2->GetId());
	m_menu5->Bind(wxEVT_COMMAND_MENU_SELECTED, wxCommandEventHandler( plc::mOnMenuSelection1 ), this, m_menuItem3->GetId());
}

plc::~plc()
{
	// Disconnect Events
	m_filePicker1->Disconnect( wxEVT_COMMAND_FILEPICKER_CHANGED, wxFileDirPickerEventHandler( plc::OnFileChanged ), NULL, this );
	m_filePicker1->Disconnect( wxEVT_SET_FOCUS, wxFocusEventHandler( plc::SetFocus ), NULL, this );
	m_textCtrl4->Disconnect( wxEVT_COMMAND_TEXT_UPDATED, wxCommandEventHandler( plc::OnTextFilter ), NULL, this );
	m_button1->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( plc::OnButtonClick ), NULL, this );
	m_button_FFT->Disconnect( wxEVT_COMMAND_BUTTON_CLICKED, wxCommandEventHandler( plc::OnButtonClick_FFT ), NULL, this );
	m_checkList3->Disconnect( wxEVT_COMMAND_LISTBOX_SELECTED, wxCommandEventHandler( plc::Box ), NULL, this );
	m_checkList3->Disconnect( wxEVT_COMMAND_LISTBOX_DOUBLECLICKED, wxCommandEventHandler( plc::BoxDClick ), NULL, this );
	m_checkList3->Disconnect( wxEVT_COMMAND_CHECKLISTBOX_TOGGLED, wxCommandEventHandler( plc::BoxToggled ), NULL, this );
	
}
