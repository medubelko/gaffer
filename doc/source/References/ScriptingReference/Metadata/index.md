# Metadata #

The UI for plugs and nodes is defined using a metadata convention. This
makes it easy to customise the UI for a specific node type, or even for a
specific node instance.

The following is a reference for names of the most common metadata items.

<!-- TODO: Decide if items of the first column should be code. -->

## General ##

```eval_rst
=================== =============================== ============================
Name                Purpose                         Example Values
=================== =============================== ============================
label               Node's label in Node Graph      :code:`"My Label"`
description         Describes the purpose of a      :code:`"Turns on the shader"`
                    node or plug
icon                Name of an image file used to   :code:`"myNodeIcon.png"`
                    represent a node
documentation:url   Link to node's documentation    :code:`http://www.gafferhq.org`
userDefault         Overrides the default value of  :code:`3.14159`
                    a plug
preset:<name>       Specifies a named preset value  :code:`"preset:Max"`, :code:`1`
=================== =============================== ============================
```


## Node Editor Layout ##

```eval_rst
=================== =============================== ============================
Name                Purpose                         Example Values
=================== =============================== ============================
layout:divider      Places a divider after the plug :code:`True`
layout:index        Integer index in the layout     :code:`0` (first), :code:`-1` (last)
                    order
layout:section      Specifies the section the plug  :code:`TabName.SectionName`
                    belongs in
layout:accessory    Places widget on same line as   :code:`True`
                    previous widget
=================== =============================== ============================
```


## Node Graph Layout ##

```eval_rst
====================== ================================ ================================
Name                   Purpose                          Example Values
====================== ================================ ================================
nodule:color           Plug color                       :code:`imath.Color3f( 0, 1, 0 )`
connectionGadget:color Input connection color           :code:`imath.Color3f( 1, 0, 0 )`
nodeGadget:color       Node color                       :code:`imath.Color3f( 0, 0, 1 )`
noduleLayout:section   Which edge the plug appears on   :code:`"left"`, :code:`"right"`, :code:`"top"`, :code:`"bottom"`
noduleLayout:visible   Show/hide the plug               :code:`True` (visible), :code:`False` (hidden)
====================== ================================ ================================
```


## Viewer Layout ##

```eval_rst
====================== ================================ ================================
Name                   Purpose                          Example Values
====================== ================================ ================================
layout:divider         Places a divider after the plug  :code:`True`
layout:index           Integer index in the layout      :code:`0` (first), :code:`-1` (last)
                       order
toolbarLayout:section  The edge of the viewer the plug  :code:`"Left"`, :code:`"Right"`, :code:`"Top"`, :code:`"Bottom"`
                       appears on
====================== ================================ ================================
```


## PlugValueWidgets ##

Custom widget types can be registered for use in the Node Editor by adding `"plugValueWidget:type"` metadata to a plug. The table below lists the relevant widget types by plug type.

> Note :
> Not all widget types are compatible with all plug types.

```eval_rst
========================== ================================ ==================================================
Plug Type                  Purpose                          PlugValueWidgetType
========================== ================================ ==================================================
Plug (and subclasses)      Hide the plug permanently        :code:`""`
Plug (and subclasses)      Display the input connection     :code:`"GafferUI.ConnectionPlugValueWidget"`
ValuePlug (and subclasses) Show a menu of presets           :code:`"GafferUI.PresetsPlugValueWidget"`
IntPlug                    Display a checkbox               :code:`"GafferUI.BoolPlugValueWidget"`
StringPlug                 Allow multi-line text entry      :code:`"GafferUI.MultiLineStringPlugValueWidget"`
StringPlug                 Show a file chooser              :code:`"GafferUI.FileSystemPathPlugValueWidget"`
StringVectorDataPlug       Show a file chooser              :code:`"GafferUI.FileSystemPathVectorDataPlugValueWidget"`
========================== ================================ ==================================================
```

These widget types may be further customised using additional metadata, as follows.


### BoolPlugValueWidget ###

```eval_rst
================================= ========================== ====================
Name                              Purpose                    Example values
================================= ========================== ====================
boolPlugValueWidget:displayMode   Change display style       :code:`"checkBox"`, :code:`"switch"`
================================= ========================== ====================
```

### FileSystemPathPlugValueWidget ###

These options also apply to the FileSystemPathVectorDataPlugValueWidget.

```eval_rst
================================= ============================== ====================
Name                              Purpose                        Example values
================================= ============================== ====================
path:bookmarks                    Specify which bookmarks to use :code:`"image"`
path:leaf                         Don't accept directories       :code:`True`
path:valid                        Only accept files that exist   :code:`True`
fileSystemPath:extensions         Specify valid file types       :code:`"jpg jpeg png"`
fileSystemPath:extensionsLabel    Describe valid file types      :code:`"Web images"`
fileSystemPath:includeSequences   Display file sequences         :code:`True`
================================= ============================== ====================
```
