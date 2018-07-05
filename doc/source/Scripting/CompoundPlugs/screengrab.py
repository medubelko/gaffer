# BuildTarget: images/nodeEditorWindowCompoundPlugs.png

import IECore
import imath

import Gaffer
import GafferUI

import GafferScene

mainWindow = GafferUI.ScriptWindow.acquire( script )

# Transform tab in Node Editor window
sphereNode = GafferScene.Sphere()
script.addChild( sphereNode )
nodeEditorWindow = GafferUI.NodeEditor.acquire( sphereNode, floating=True )
nodeEditorWindow.nodeUI().plugValueWidget( sphereNode["transform"] ).reveal()
nodeEditorWindow._qtWidget().setFocus()
GafferUI.WidgetAlgo.grab( widget = nodeEditorWindow, imagePath = "images/nodeEditorWindowCompoundPlugs.png" )
