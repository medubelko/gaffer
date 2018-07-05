# BuildTarget: images/scriptOutputCompoundObject.png

import os
import IECore
import imath
import time

import Gaffer
import GafferScene
import GafferUI

# Delay the script for x seconds
def __delay( delay ) :
	endTime = time.time() + delay
	while time.time() < endTime :
		GafferUI.EventLoop.waitForIdle( 1 )

mainWindow = GafferUI.ScriptWindow.acquire( script )
viewer = mainWindow.getLayout().editors( GafferUI.Viewer )[0]
scriptEditor = mainWindow.getLayout().editors( GafferUI.ScriptEditor )[0]
scriptEditor.reveal()

script["fileName"].setValue( os.path.abspath( "scripts/QueryingAScene.gfr" ) )
script.load()

scriptEditor.inputWidget().setText( 'script["StandardOptions"]["out"]["globals"].getValue()' )
scriptEditor.execute()
GafferUI.WidgetAlgo.grab( widget = scriptEditor.outputWidget(), imagePath = "images/scriptOutputCompoundObject.png" )

