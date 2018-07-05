# Special Variables #

Gaffer scripts have some special reserved variables.


## The "script" Variable ##

In Gaffer's project files, the variable to invoke the main script's context is the `script` variable. When building the node graph of your script, nodes are added using this variable's context. Consequently, whenever you add or remove scripts


## The "parent" Variable ##

In Gaffer's project files, the variable to invoke the containing node is the `parent` variable. This variable

TODO: Because with scripts, you're never sure whether you're pasting into a main file or a reference node.


## See Also ##

- [Using the Script Editor](../UsingTheScriptEditor/index.md)
- [Script File Formats](../ScriptFileFormats/index.md)
