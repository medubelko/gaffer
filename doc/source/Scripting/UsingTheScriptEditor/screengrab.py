# BuildTarget: images/scriptEditor.png images/scriptEditorError.png

import Gaffer
import GafferUI

scriptWindow = GafferUI.ScriptWindow.acquire( script )
scriptEditor = scriptWindow.getLayout().editors( GafferUI.ScriptEditor )[0]
scriptEditor.reveal()
GafferUI.WidgetAlgo.grab( widget = scriptEditor.parent(), imagePath = "images/scriptEditor.png" )

scriptEditor.inputWidget().setText( 'undefinedVariable' )
scriptEditor.execute()
GafferUI.WidgetAlgo.grab( widget = scriptEditor.outputWidget(), imagePath = "images/scriptEditorError.png" )
