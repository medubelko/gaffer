##########################################################################
#
#  Copyright (c) 2012-2014, John Haddon. All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#
#      * Redistributions of source code must retain the above
#        copyright notice, this list of conditions and the following
#        disclaimer.
#
#      * Redistributions in binary form must reproduce the above
#        copyright notice, this list of conditions and the following
#        disclaimer in the documentation and/or other materials provided with
#        the distribution.
#
#      * Neither the name of John Haddon nor the names of
#        any other contributors to this software may be used to endorse or
#        promote products derived from this software without specific prior
#        written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS
#  IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
#  THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
#  PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
#  CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
#  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
#  PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
#  PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
#  LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
#  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
#  SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
##########################################################################

import Gaffer
import GafferUI
import GafferArnold

Gaffer.Metadata.registerNode(

	GafferArnold.ArnoldRender,

	"description",
	"""
	Performs offline batch rendering using the
	Arnold renderer. This is done in two phases -
	first a .ass file is generated and then Arnold
	is invoked to render it. Note though that the .ass
	file is lightweight, and contains little more than
	a procedural which will use Gaffer to generate the
	scene at render time.
	""",

	plugs = {

		"mode" : [

			"description",
			"""
			When in the standard "Render" mode, an .ass
			file is generated and then renderered in Arnold.
			Alternatively, just the .ass file can be generated
			and then another method can be used to post-process
			it or launch the render - a SystemCommand node may
			be useful for this. Finally, an expanded .ass file
			may be generated - this will contain the entire
			expanded scene rather than just a procedural, and can
			be useful for debugging.
			""",

			"preset:Render", "render",
			"preset:Generate .ass only", "generate",
			"preset:Generate expanded .ass", "expand",

		],

		"fileName" : [

			"description",
			"""
			The name of the .ass file to be generated.
			""",

		],

		"verbosity" : [

			"description",
			"""
			Controls the verbosity of the Arnold renderer output.
			""",

			"preset:0", 0,
			"preset:1", 1,
			"preset:2", 2,
			"preset:3", 3,
			"preset:4", 4,
			"preset:5", 5,
			"preset:6", 6,

		],

}

)

GafferUI.PlugValueWidget.registerCreator(
	GafferArnold.ArnoldRender,
	"mode",
	GafferUI.PresetsPlugValueWidget,
)

GafferUI.PlugValueWidget.registerCreator(
	GafferArnold.ArnoldRender,
	"fileName",
	lambda plug : GafferUI.PathPlugValueWidget( plug,
		path = Gaffer.FileSystemPath( "/", filter = Gaffer.FileSystemPath.createStandardFilter() ),
		pathChooserDialogueKeywords = {
			"bookmarks" : GafferUI.Bookmarks.acquire( plug, category = "ass" ),
			"leaf" : True,
		},
	),
)

GafferUI.PlugValueWidget.registerCreator(
	GafferArnold.ArnoldRender,
	"verbosity",
	GafferUI.PresetsPlugValueWidget,
)

GafferUI.Nodule.registerNodule( GafferArnold.ArnoldRender, "mode", lambda plug : None )
GafferUI.Nodule.registerNodule( GafferArnold.ArnoldRender, "fileName", lambda plug : None )
GafferUI.Nodule.registerNodule( GafferArnold.ArnoldRender, "verbosity", lambda plug : None )
