///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Jul 11 2018)
// http://www.wxformbuilder.org/
//
// PLEASE DO *NOT* EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#ifndef __NONAME_H__
#define __NONAME_H__

#include <wx/artprov.h>
#include <wx/xrc/xmlres.h>
#include <wx/string.h>
#include <wx/stattext.h>
#include <wx/gdicmn.h>
#include <wx/font.h>
#include <wx/colour.h>
#include <wx/settings.h>
#include <wx/filepicker.h>
#include <wx/textctrl.h>
#include <wx/bitmap.h>
#include <wx/image.h>
#include <wx/icon.h>
#include <wx/button.h>
#include <wx/wrapsizer.h>
#include <wx/checklst.h>
#include <wx/sizer.h>
#include <wx/scrolwin.h>
#include <wx/menu.h>
#include <wx/frame.h>

///////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////
/// Class plc
///////////////////////////////////////////////////////////////////////////////
class plc : public wxFrame 
{
	private:
	
	protected:
		wxStaticText* m_staticText15;
		wxFilePickerCtrl* m_filePicker1;
		wxStaticText* m_staticText151;
		wxStaticText* m_staticText3;
		wxTextCtrl* m_textCtrl4;
		wxStaticText* m_staticText32;
		wxStaticText* m_staticText31;
		wxTextCtrl* m_textCtrl_xmin;
		wxStaticText* m_staticText311;
		wxTextCtrl* m_textCtrl_xmax;
		wxButton* m_button1;
		wxButton* m_button_FFT;
		wxScrolledWindow* m_scrolledWindow2;
		wxCheckListBox* m_checkList3;
		wxMenuBar* m_menubar1;
		wxMenu* m_menu5;
		
		// Virtual event handlers, overide them in your derived class
		virtual void OnFileChanged( wxFileDirPickerEvent& event ) { event.Skip(); }
		virtual void SetFocus( wxFocusEvent& event ) { event.Skip(); }
		virtual void OnTextFilter( wxCommandEvent& event ) { event.Skip(); }
		virtual void OnButtonClick( wxCommandEvent& event ) { event.Skip(); }
		virtual void OnButtonClick_FFT( wxCommandEvent& event ) { event.Skip(); }
		virtual void Box( wxCommandEvent& event ) { event.Skip(); }
		virtual void BoxDClick( wxCommandEvent& event ) { event.Skip(); }
		virtual void BoxToggled( wxCommandEvent& event ) { event.Skip(); }
		virtual void mOnMenuSelection2( wxCommandEvent& event ) { event.Skip(); }
		virtual void mOnMenuSelection1( wxCommandEvent& event ) { event.Skip(); }
		
	
	public:
		
		plc( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxT("B&R buffer plot"), const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 800,600 ), long style = wxCAPTION|wxCLOSE_BOX|wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );
		
		~plc();
	
};

#endif //__NONAME_H__
