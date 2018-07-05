# Script Files #

Gaffer's script files are serialized Python scripts that contain all the code necessary to reconstruct a saved node network. When you save a file in Gaffer, it interprets the existing graph and serializes it to an unbinarized file with a Gaffer extension (.gfr or .grf) using regular UTF-8 encoding.

Node graphs in Gaffer scripts and those copy-pasted from the _Graph Editor_ use the same syntax, and are safely interchangeable. If you find yourself struggling to find a way of scripting something, you can open a Gaffer script in an external text editor and examine how it is constructed. Nodes in the _Graph Editor_ can be copied (select the nodes, then hit <kbd>Ctrl</kbd> + <kbd>C</kbd>), pasted into the _Script Editor_ or an external text editor. You can also open a Gaffer script in a text editor, and examine how it is constructed.

Additionally, since Gaffer is open source, you can find examples in the [source code itself](https://github.com/GafferHQ/gaffer/tree/!GAFFER_VERSION!).


### Format: .gfr ###

Gaffer scripts saved as whole projects use the .gfr ("Gaffer") extension.


### Format: .grf ###

Gaffer scripts saved as references for importation by Reference nodes use the .grf ("Gaffer reference file") extension.

> Note :
> The Reference node will only import scripts with the .grf extension. To import a .gfr file into a Reference node, changes its extension to .grf.


## Dictionary Syntax ##

Gaffer scripts use Python's [dictionary syntax and notation](https://docs.python.org/2/tutorial/datastructures.html#dictionaries) to build a compendium of instances of node classes, and instances of plug classes as children of the nodes. Each node and plug are connected together in a parent-child hierarchy to build a dependency graph, which the Gaffer application interprets as a node graph. Using Python dictionary syntax and notation, plugs are parented to nodes, and nodes are parented to the `script` variable.

If you are familiar with Python, you will know that there are multiple ways to add classes to a dictionary, such as `script["newNode"] = Gaffer.Node`. But, Python dictionaries require unique names, the `addChild()` method is safer and preferable because it prevents duplicate names. It ensures a node or plug will not replace an existing node or plug by automatically adding an iteration index to its name in case of conflict. If you use other methods, you might erroneously replace an existing node or plug by reusing its name. 

> Tip :
> Use the `addChild()` method to add nodes and plugs.


## Sample Gaffer File ##

Below are the contents of a sample Gaffer file containing a SceneReader and a Camera node connected to a Group node:

<!-- Note: removed Metadata values, as they are apparently obsolete? -->

```python
import Gaffer
import GafferScene
import IECore
import imath

__children = {}

__children["SceneReader"] = GafferScene.SceneReader( "SceneReader" )
parent.addChild( __children["SceneReader"] )
__children["Group"] = GafferScene.Group( "Group" )
parent.addChild( __children["Group"] )
__children["Group"]["in"].addChild( GafferScene.ScenePlug( "in1" ) )
__children["Group"]["in"].addChild( GafferScene.ScenePlug( "in2" ) )
__children["Camera"] = GafferScene.Camera( "Camera" )
parent.addChild( __children["Camera"] )
__children["Group"]["in"]["in0"].setInput( __children["SceneReader"]["out"] )
__children["Group"]["in"]["in1"].setInput( __children["Camera"]["out"] )

del __children
```

Here is a breakdown of the format:


### Imports ###

Upon creation, the Gaffer script automatically detects which modules are in use in the active application, and adds them as `import` statements at the beginning of the file.


### "Metadata" ###

> Note :
> The `Gaffer.Metadata` lines are deprecated, and can be safely ignored.


### "parent" and "__children" variables ###

Since Gaffer does not truly distinguish between scripts intended as independent files and scripts intended as reference nodes (other than by their file extensions), scripts are serialized without using the root `script` variable. Instead, they use the `parent` variable. If the script is loaded as a file, the `parent` variable will default to `script`. If the script is imported into a Reference node, `parent` will point to the node.

Scripts also use a private `__children` variable to create a temporary dictionary, which has nodes added to it during the serialization. When the script builds the node graph in the application, it buffers nodes and plugs before they are added to the node graph.


## See Also ##

- []()
- []()
