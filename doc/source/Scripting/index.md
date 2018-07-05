# Scripting #

Gaffer's architecture is built from a combination of C++ and Python script. Much of the core API has hooks in Python: much of the GUI is written in Python, Gaffer plugins are Python modules, and the .gfr file format is simply a Python script.

There is a direct one-to-one correspondence between the C++ and Python APIs for Gaffer, so if you start out using one, you can easily transfer your work to the other. This makes it relatively straightforward to prototype in Python, but convert to C++ if performance becomes an issue, or to spend most of your time coding in C++ but still be comfortable writing some GUI code in Python.

The following topics cover various subjects related to the scripting API, the built-in script and code interfaces, and script- and code- specific nodes.

<!-- TODO: WHERE TO PUT THIS? That some plugs are visible only in the _Node Editor_ and others only in the _Graph Editor_ might give the false impression that only the plugs in the _Graph Editor_ can be connected. In fact, this is not the case. As a general rule, almost any plug can be given an input connection. -->


## Tutorials ##

Before diving in to the scripting API, we recommend completing the [Scripting Basics tutorial](../Tutorials/ScriptingBasics/index.md). The following tutorials cover more advanced and specialized topics.

- [Tutorial: Querying a Scene]()
- [Tutorial: Using the OSLCode Node]()
- [Tutorial: Creating a Configuration File]()
- [Tutorial: Adding a Menu Item]()


## Script Editor ##

Gaffer's interface has a built-in _Script Editor_ for interactively building and modifying the node graph in Python, as well as for testing code in the Gaffer API.

- [The Script Editor](ScriptEditor/index.md)
- [Using the Script Editor](UsingTheScriptEditor/index.md)


## Scripting Architecture ##

The following topics describe some of the Python architecture underlying Gaffer's UI and files.

- [Script Files](ScriptFiles/index.md)
- [Special Variables](SpecialVariables/index.md)
- [Compound Plugs](CompoundPlugs/index.md)
- [Configuration Files](ConfigurationFiles/index.md)


## Scripting Nodes ##

Gaffer has a handful of special scripting nodes that can evaluate arbitrary Python script or OSL code when the main script is dispatched.

- [Expression Node](ExpressionNode/index.md)
- [OSLCode Node](OSLCodeNode/index.md)
- [PythonCommand Node](PythonCommandNode/index.md)
- [SystemCommand Node](SystemCommandNode/index.md)


<!-- TOC -->

```eval_rst
.. toctree::
    :titlesonly:
    :hidden:
    :maxdepth: 1

    ScriptEditor/index.md
    UsingTheScriptEditor/index.md
    ScriptFiles/index.md
    SpecialVariables/index.md
    ImportingModules/index.md
    CompoundPlugs/index.md
    ConfigurationFiles/index.md
    ExpressionNode/index.md
    OSLCodeNode/index.md
    PythonCommandNode/index.md
    SystemCommandNode/index.md
```
