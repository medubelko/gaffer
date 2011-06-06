##########################################################################
#  
#  Copyright (c) 2011, John Haddon. All rights reserved.
#  Copyright (c) 2011, Image Engine Design Inc. All rights reserved.
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

import weakref
import string
import os
import math

import IECore

import Gaffer
import GafferUI

QtCore = GafferUI._qtImport( "QtCore" )
QtGui = GafferUI._qtImport( "QtGui" )

## The Widget class provides a base class for all widgets in GafferUI.
#
# When building UIs, you will typically derive from an existing Widget subclass such as Window,
# Dialogue or Editor and then populate it with other Widgets. You define behaviours by connecting
# methods of your class to event signals on your base class and child Widgets. It is
# important to avoid circular references when doing this - naively connecting a signal of your
# base class to a method on your class creates a reference cycle - although this will eventually
# be broken by the garbage collector, it may extend the lifetime of the UI beyond the appropriate
# point. To avoid this problem a simple rule of thumb is to always connect signals to Gaffer.WeakMethod
# instances referring to your methods.
#
# GafferUI.Widget subclasses are implemented using Qt widgets (using PySide or PyQt), but the public API
# exposed by the GafferUI classes never includes Qt functions or classes directly - this
# allows the implementation to be changed in the future. Furthermore it allows the use
# of the GafferUI module without learning all the Qt API. To enforce this separation,
# GafferUI classes must not derive from Qt classes.
#
# \todo Consider how this relates to the Gadget class. Currently I'm aiming to have the two classes
# have identical signatures in as many places as possible, with the possibility of perhaps having
# a common base class in the future. Right now the signatures are the same for the event signals and
# for the tool tips.
class Widget( object ) :

	## All GafferUI.Widget instances must hold a corresponding QtGui.QWidget instance
	# which provides the top level implementation for the widget, and to which other
	# widgets may be parented. This QWidget is created during __init__, and cannot be
	# replaced later. Derived classes may pass either a QtGui.QWidget directly, or if
	# they prefer may pass a GafferUI.Widget, in which case a top level QWidget will be
	# created automatically, with the GafferUI.Widget being parented to it. The top level
	# QWidget can be accessed at any time using the _qtWidget() method. Note that this is
	# protected to encourage non-reliance on knowledge of the Qt backend.
	def __init__( self, topLevelWidget, toolTip="" ) :
	
		assert( isinstance( topLevelWidget, ( QtGui.QWidget, Widget ) ) )
		
		if isinstance( topLevelWidget, QtGui.QWidget ) :
			assert( Widget.__qtWidgetOwners.get( topLevelWidget ) is None )
			self.__qtWidget = topLevelWidget
		else :
			self.__gafferWidget = topLevelWidget
			self.__qtWidget = QtGui.QWidget()
			self.__qtWidget.setLayout( QtGui.QGridLayout() )
			self.__qtWidget.layout().setContentsMargins( 0, 0, 0, 0 )
			self.__qtWidget.layout().addWidget( self.__gafferWidget._qtWidget(), 0, 0 )
			
		Widget.__qtWidgetOwners[self.__qtWidget] = weakref.ref( self )
		
		self.__qtWidget.setStyleSheet( self.__styleSheet )
		
		self.__qtWidget.installEventFilter( _eventFilter )
		
		self.__keyPressSignal = GafferUI.WidgetEventSignal()
		self.__buttonPressSignal = GafferUI.WidgetEventSignal()
		self.__buttonReleaseSignal = GafferUI.WidgetEventSignal()
		self.__mouseMoveSignal = GafferUI.WidgetEventSignal()
		
		self.setToolTip( toolTip )
		
	def setVisible( self, visible ) :
	
		self.__qtWidget.setVisible( visible )
		
	def getVisible( self ) :
	
		return self.__qtWidget.isVisible()

	## Returns the GafferUI.Widget which is the parent for this
	# Widget, or None if it has no parent.
	def parent( self ) :
	
		q = self._qtWidget()
				
		while q is not None :
					
			q = q.parentWidget()
			if q in Widget.__qtWidgetOwners :
				return Widget.__qtWidgetOwners[q]()
				
		return None
	
	## Returns the first Widget in the hierarchy above this one
	# to match the desired type.
	def ancestor( self, type ) :
	
		w = self
		while w is not None :
			w = w.parent()
			if isinstance( w, type ) :
				return w
				
		return None
		
	def size( self ) :
	
		return IECore.V2i( self.__qtWidget.width(), self.__qtWidget.height() )

	def keyPressSignal( self ) :
	
		return self.__keyPressSignal
	
	## \todo Should these be renamed to mousePressSignal and mouseReleaseSignal?	
	def buttonPressSignal( self ) :
	
		return self.__buttonPressSignal
	
	def buttonReleaseSignal( self ) :
	
		return self.__buttonReleaseSignal
	
	def mouseMoveSignal( self ) :
	
		return self.__mouseMoveSignal
	
	## Returns the tooltip to be displayed. This may be overriden
	# by derived classes to provide sensible default behaviour, but
	# allow custom behaviour when setToolTip( nonEmptyString ) has
	# been called.
	def getToolTip( self ) :
	
		return self.__toolTip
	
	## Sets the tooltip to be displayed for this Widget. This
	# will override any default behaviour until setToolTip( "" )
	# is called.
	def setToolTip( self, toolTip ) :
	
		assert( isinstance( toolTip, basestring ) )
		
		self.__toolTip = toolTip
		
	## Returns the top level QWidget instance used to implement
	# the GafferUI.Widget functionality.
	def _qtWidget( self ) :
	
		return self.__qtWidget
		
	## Returns the GafferUI.Widget that owns the specified QtGui.QWidget
	@classmethod
	def _owner( cls, qtWidget ) :
		
		while qtWidget :
	
			if qtWidget in cls.__qtWidgetOwners :
				return cls.__qtWidgetOwners[qtWidget]()
		
			qtWidget = qtWidget.parentWidget()
			
		return None
	
	__qtWidgetOwners = weakref.WeakKeyDictionary()
	
	## Converts a Qt key code into a string
	@classmethod
	def _key( cls, qtKey ) :
	
		if not cls.__keyMapping :
			for k in dir( QtCore.Qt ) :
				if k.startswith( "Key_" ) :
					keyValue = getattr( QtCore.Qt, k )
					keyString = k[4:]
					cls.__keyMapping[keyValue] = keyString
	
		return cls.__keyMapping[qtKey]
	
	__keyMapping = {}
	
	## Converts a Qt buttons enum value into Gaffer ButtonEvent enum
	@staticmethod
	def _buttons( qtButtons ) :
	
		result = GafferUI.ButtonEvent.Buttons.None
		if qtButtons & QtCore.Qt.LeftButton :
			result |= GafferUI.ButtonEvent.Buttons.Left
		if qtButtons & QtCore.Qt.MiddleButton :
			result |= GafferUI.ButtonEvent.Buttons.Middle
		if qtButtons & QtCore.Qt.RightButton :
			result |= GafferUI.ButtonEvent.Buttons.Right
			
		return GafferUI.ButtonEvent.Buttons( result )
			
	## Converts Qt modifiers to Gaffer modifiers
	@staticmethod
	def _modifiers( qtModifiers ) :
	
		modifiers = GafferUI.ModifiableEvent.Modifiers.None
		if qtModifiers & QtCore.Qt.ShiftModifier :
			modifiers = modifiers | GafferUI.ModifiableEvent.Modifiers.Shift
		if qtModifiers & QtCore.Qt.ControlModifier :
			modifiers = modifiers | GafferUI.ModifiableEvent.Modifiers.Control
		if qtModifiers & QtCore.Qt.AltModifier :
			modifiers = modifiers | GafferUI.ModifiableEvent.Modifiers.Alt		
			
		return GafferUI.ModifiableEvent.Modifiers( modifiers )
	
	## Converts an IECore.Color[34]f to a QtColor
	@staticmethod
	def _qtColor( color ) :
	
		color = color * 255
		return QtGui.QColor(
			min( 255, max( 0, color.r ) ),
			min( 255, max( 0, color.g ) ),
			min( 255, max( 0, color.b ) ),
		)
	
	## \todo Unify with GafferUI.Style for colours at least. Also set once at application level
	# rather than on each Widget.
	__styleSheet = string.Template( 

		"""
		QWidget {

			color: $foreground;
			background-color: $backgroundMid;
			alternate-background-color: $backgroundLighter;
			selection-background-color: $brightColor
		}

		QMenuBar {

			background-color: $backgroundDarkest;

		}

		QMenu {

			border: 1px solid $backgroundDarkest;
			padding-bottom: 5px;
			padding-top: 5px;
			etch-disabled-text: 0;

		}

		QMenu::item {

			background-color: transparent;
			border: 0px;
			padding: 2px 25px 2px 20px;
			
		}
		
		QMenu::item:disabled {

			color: $foregroundFaded;

		}

		QMenu::right-arrow {
			image: url($GAFFER_ROOT/graphics/subMenuArrow.png);
			padding: 0px 7px 0px 0px;
		}
		
		QMenu::separator {

			height: 1px;
			background: $backgroundDarkest;
			margin-left: 10px;
			margin-right: 10px;
			margin-top: 5px;
			margin-bottom: 5px;

		}
		
		QMenu::indicator {
			padding: 0px 0px 0px 3px;
		}
		
		QMenu::indicator:non-exclusive:checked {
			image: url($GAFFER_ROOT/graphics/menuChecked.png);
		}
		
		QMenu::indicator:exclusive:checked:selected {
			image: url($GAFFER_ROOT/graphics/arrowRight10.png);
		}
		
		QMenu, QTabBar::tab:selected, QPushButton, QHeaderView::section {

			background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 $backgroundLight, stop: 1 $backgroundMid);

		}
		
		QPlainTextEdit {
		
			border: 1px solid $backgroundDark;
		
		}

		QLineEdit, QPlainTextEdit[readOnly="false"] {

			border: 1px solid transparent;
			padding: 1px;
			margin: 0px;

		}

		QLineEdit[readOnly="false"], QPlainTextEdit[readOnly="false"] {

			background-color: $backgroundLighter;

		}

		QLineEdit:focus, QPlainTextEdit[readOnly="false"]:focus {

			border: 2px solid $brightColor;
			padding: 0px;

		}

		QPushButton {

			border: 1px solid $backgroundDarkest;
			border-radius: 3px;
			padding: 4px;
			padding-left: 8px;
			padding-right: 8px;
			min-height: 16px;
			min-width: 16px;

		}

		QPushButton:hover {

			background-color: $backgroundLight;

		}

		QTabWidget::tab-bar {

			left: 10px;

		}

		QTabBar::tab {

			border: 1px solid $backgroundDarkest;
			padding: 4px;
			padding-left: 8px;
			padding-right: 8px;
			border-top-left-radius: 3px;
			border-top-right-radius: 3px;

		}

		QTabBar::tab:selected {

			border-bottom-color: transparent; /* blend into frame below */

		}

		QTabBar::tab:!selected, QSplitter::handle {

			background-color: $backgroundDark;

		}

		QTabBar::tab:hover, QMenu::item:selected, QMenuBar::item:selected, QSplitter::handle:hover,
		QRadioButton#gafferCollapsibleToggle::hover, QPushButton:pressed {

			color: white;
			background-color:	$brightColor;

		}

		/* tab widget frame has a line at the top, tweaked up 1 pixel */
		/* so that it sits underneath the bottom of the tabs.         */
		/* this means the active tab can blend into the frame.        */
		QTabWidget::pane {
			border-top: 1px solid $backgroundDarkest;
			top: -1px;
		}

		QRadioButton#gafferCollapsibleToggle::indicator {

			width: 12px;
			height: 12px;
			background-color: none;

		}

		QRadioButton#gafferCollapsibleToggle::indicator::unchecked {

			image: url($GAFFER_ROOT/graphics/collapsibleArrowDown.png);

		}

		QRadioButton#gafferCollapsibleToggle::indicator::checked {

			image: url($GAFFER_ROOT/graphics/collapsibleArrowRight.png);

		}
		
		QHeaderView::section {
		
			border: 1px solid transparent;
			border-bottom: 1px solid $backgroundDarkest;
			padding: 4px;
		
		}
		
		QScrollBar {
		
			border: 1px solid $backgroundDarkest;
			background-color: $backgroundDark;
			
		}
		
		QScrollBar:vertical {
		
			width: 14px;
			margin: 0px 0px 28px 0px;
			
		}
		
		QScrollBar:horizontal {
		
			height: 14px;
			margin: 0px 28px 0px 0px;
			
		}
		
		QScrollBar::add-page, QScrollBar::sub-page {
			background: none;
 			border: none;
		}
		
		QScrollBar::add-line, QScrollBar::sub-line {
			background-color: $backgroundLight;
			border: 1px solid $backgroundDarkest;
		}
		
		QScrollBar::add-line:vertical {
			height: 14px;
			subcontrol-position: bottom;
			subcontrol-origin: margin;
		}
		
		QScrollBar::add-line:horizontal {
			width: 14px;
			subcontrol-position: right;
			subcontrol-origin: margin;
		}

		QScrollBar::sub-line:vertical {
			height: 14px;
			subcontrol-position: bottom right;
			subcontrol-origin: margin;
			position: absolute;
			bottom: 15px;
		}
		
		QScrollBar::sub-line:horizontal {
			width: 14px;
			subcontrol-position: top right;
			subcontrol-origin: margin;
			position: absolute;
			right: 15px;
		}
		
		QScrollBar::down-arrow {
			image: url($GAFFER_ROOT/graphics/arrowDown10.png);
		}
		
		QScrollBar::up-arrow {
			image: url($GAFFER_ROOT/graphics/arrowUp10.png);
		}
		
		QScrollBar::left-arrow {
			image: url($GAFFER_ROOT/graphics/arrowLeft10.png);
		}
		
		QScrollBar::right-arrow {
			image: url($GAFFER_ROOT/graphics/arrowRight10.png);
		}

		QScrollBar::handle {
			background-color: $backgroundLight;			
			border: 1px solid $backgroundDarkest;
		}
		
		QScrollBar::handle:vertical {
			min-height: 14px;
			border-left: none;
			border-right: none;			
			margin-top: -1px;		
		}
		
		QScrollBar::handle:horizontal {
			min-width: 14px;
			border-top: none;
			border-bottom: none;
			margin-left: -1px;		
		}
		
		QScrollBar::handle:hover {
			background-color: $brightColor;
		}
		
		QCheckBox {
			spacing: 5px;
		}

		QCheckBox::indicator {
			width: 20px;
			height: 20px;
			background-color: transparent;			
		}
		
		QCheckBox::indicator:unchecked {
			image: url($GAFFER_ROOT/graphics/checkBoxUnchecked.png);
		}
		
		QCheckBox::indicator:unchecked:hover {
			image: url($GAFFER_ROOT/graphics/checkBoxUncheckedHover.png);
		}
		QCheckBox::indicator:checked:hover {
			image: url($GAFFER_ROOT/graphics/checkBoxCheckedHover.png);
		}
		
		QCheckBox::indicator:checked {
			image: url($GAFFER_ROOT/graphics/checkBoxChecked.png);
		}

		.QFrame#borderStyleNone {
			border: 1px solid transparent;
			border-radius: 4px;
			padding: 2px;
		}
		
		.QFrame#borderStyleFlat {
			border: 1px solid $backgroundDarkest;
			border-radius: 4px;
			padding: 2px;
		}
		
		QToolTip {
			background-clip: border;
			color: $backgroundDarkest;
			background-color: $brightColor2;
			border: 1px solid $backgroundDarkest;
			padding: 2px;

		}

		"""
		
	).substitute( {
	
		"GAFFER_ROOT" : os.environ["GAFFER_ROOT"],
		"backgroundDarkest" : "#000000",
		"backgroundDark" : "#3c3c3c",
		"backgroundMid" : "#4c4c4c",
		"backgroundLighter" : "#6c6c6c",
		"backgroundLight" : "#7d7d7d",
		"brightColor" : "#779cbd",
		"brightColor2" : "#e5c618",
		"foreground" : "#f0f0f0",
		"foregroundFaded" : "#999999",
	
	} )
	
class _EventFilter( QtCore.QObject ) :

	def __init__( self ) :
	
		QtCore.QObject.__init__( self )
		
	def eventFilter( self, qObject, qEvent ) :
	
		if qEvent.type()==QtCore.QEvent.KeyPress :
						
			widget = Widget._owner( qObject )
			event = GafferUI.KeyEvent(
				Widget._key( qEvent.key() ),
				Widget._modifiers( qEvent.modifiers() ),
			)

			return widget.keyPressSignal()( widget, event )
		
		elif qEvent.type()==QtCore.QEvent.MouseButtonPress :
					
			widget = Widget._owner( qObject )
			event = GafferUI.ButtonEvent(
				Widget._buttons( qEvent.buttons() ),
				IECore.LineSegment3f(
					IECore.V3f( qEvent.x(), qEvent.y(), 1 ),
					IECore.V3f( qEvent.x(), qEvent.y(), 0 )
				),
				Widget._modifiers( qEvent.modifiers() ),
			)

			if event.buttons :
				return widget.buttonPressSignal()( widget, event )
			
		elif qEvent.type()==QtCore.QEvent.MouseButtonRelease :
				
			widget = Widget._owner( qObject )
			event = GafferUI.ButtonEvent(
				Widget._buttons( qEvent.buttons() ),
				IECore.LineSegment3f(
					IECore.V3f( qEvent.x(), qEvent.y(), 1 ),
					IECore.V3f( qEvent.x(), qEvent.y(), 0 )
				),
				Widget._modifiers( qEvent.modifiers() ),
			)

			return widget.buttonReleaseSignal()( widget, event )
			
		elif qEvent.type()==QtCore.QEvent.MouseMove :
				
			widget = Widget._owner( qObject )
			event = GafferUI.ButtonEvent(
				Widget._buttons( qEvent.buttons() ),
				IECore.LineSegment3f(
					IECore.V3f( qEvent.x(), qEvent.y(), 1 ),
					IECore.V3f( qEvent.x(), qEvent.y(), 0 )
				),
				Widget._modifiers( qEvent.modifiers() ),
			)

			return widget.mouseMoveSignal()( widget, event )
			
		elif qEvent.type()==QtCore.QEvent.ToolTip :
		
			widget = Widget._owner( qObject )
			QtGui.QToolTip.showText( qEvent.globalPos(), widget.getToolTip(), qObject )
			return True
			
		return False

# this single instance is used by all widgets
_eventFilter = _EventFilter()
