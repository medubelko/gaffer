# The _Script Editor_ #

Gaffer's _Script Editor_ lets you build and modify the node graph, edit and adjust the underlying code of your project file, test expressions, and display results.

![The Script Editor](images/scriptEditorBlank.png "The Script Editor")

The _Script Editor_ is split into two areas. The bottom-half is a text field for inputting code, and it functions much like any other basic text editor. The top-half is a readout that displays the code you execute and any resulting output, such as output commands like `print`. Errors will appear in the output in red.

![Errors in the output field](images/scriptEditorError.png "Errors in the output field")

When dropping node or plug references and values into the _Script Editor_, the editor does not automatically add a new line or clear the current line.

When using the _Script Editor,_ importing the `Gaffer` and `IECore` modules is not required, because they are already loaded.


## See Also ##

- [Using the Script Editor](../UsingTheScriptEditor/index.md)
