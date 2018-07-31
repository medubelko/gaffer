# Tutorial: Turn 'til the Cows Come Home #

In this tutorial, we will demonstrate how to build a simple turntable for showing dailies of a character in various lighting and shading environments.

In this tutorial, you will learn:

* Making the script automatically adjust the scene to fit the frame
* Setting up an HDRI
* Setting up a transform
* Setting up a basic script to adjust the transform each frame
* Importing a .grf script
* Rendering files to disk
* Using _Task_ nodes to combine input images


## Load the Base Script ##

As with other tutorials, we have saved you some time by providing a script with some of the node graph already complete.

The script can be found in `!GAFFER_VERSION!/resources/scripts/turntable.gfr`

<!-- TODO: image of graph -->

The graph has:

* A section for _SceneReader_ nodes
* Cameras for previewing and rendering
* A _Box node_ containing the light rigs
* A second _Box_ node for rotating the scene
* A third _Box_ node containing the shaders
* A final _Box_ node for executing the render passes


## Box Nodes ##

A _Box_ node is a container that collects nodes and hides them from the main view. It is useful for simplifying the node graph's visual presentation, encapsulating a set of nodes that serve a particular function, and making user-defined modular graphs.

You can adjust the _Node Graph_ tab's view to go inside or outside _Box_ nodes:

* View the contents of a _Box_ node by selecting it and hitting <kbd>↓</kbd>.
* Move out of the _Box_ node by moving the cursor inside the _Node Graph_ tab and hitting <kbd>↑</kbd>.
* _Box_ nodes can be nested inside _Box_ nodes.  You can move further in (selection and hitting <kbd>↓</kbd>) or out (hitting <kbd>↑</kbd>) of the nest.

Once inside a _Box_ node, the _Node Graph_ tab will only display the _Box_ node's contents. The _Node Graph_ tab's label will indicate your depth within the graph.


## Light Rigs ##

First, you should create some light rigs. Begin by entering the _Box_ node named _lightRigs_.

<!-- TODO: image of the inside of lightRigs -->




## See Also ##

* [](../IntermediateTutorial/index.md)
* [](../ContactSheetTutorial/index.md)
* []()