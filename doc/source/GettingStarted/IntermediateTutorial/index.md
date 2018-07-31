# Tutorial: Everything but the Kitchen Sink #

In this tutorial, we will build a slightly more complicated scene than in the ["Assembling the Gaffer Bot" tutorial](../BeginnerTutorial/index.md), and use some of Gaffer's useful scene hierarchy-building features to quickly add appropriate lighting, texturing, and shading to the various pieces pf geometry, as well as add a small amount of set decoration.

For the purposes of this tutorial, we assume that you have completed the beginner tutorial, and are familiar with basic Gaffer interface usage, creating and connecting nodes, and manipulating the Node Graph.

By the end of this tutorial, you will be familiar with:

* Creating, assigning, and filtering sets in the scene hierarchy
* Using the _Parent_, _Prune_, and _Isolate_ nodes to modify the scene hierarchy
* Manipulating object positioning with the _PointConstraint_ node
* Adding point lights and emissive surface shaders
* Applying an instancer to replicate geometry
* Adding _Dot_ nodes and backdrops to visually organize the Node Graph


## Load the Script ##

To save time in the initial graph setup, we've included a pre-built script for you.

> Note :
> For the purposes of this instruction, we will assume you have installed Gaffer to `/opt/` folder.

To load the script:

1. Go to _File > Open..._ to open the _Open script_ window.

2. In the file path at the bottom of the window, type the name of kitchen script:
    * Linux: `/opt/!GAFFER_VERSION!-linux/resources/scripts/kitchen.gfr`
    * OSX: `opt/!GAFFER_VERSION!-osx/resources/scripts/kitchen.gfr`

3. Click _Open_ to load the preliminary graph.

    [The loaded script.]() <!-- TODO: default script -->


As you can see, the graph has a _SceneReader_ node, a _Camera_ node, a _Point Light_ node, a _Group_ node below each of them, and an isolated chain of the standard render settings nodes at the bottom.


## Build a Meaningful Hierarchy ##

Currently, every node in the graph that creates a location in the scene has a generic name. In order for the scene's hierarchy to have meaning, you should strive to give unique, readable names that communicate the function or intent for each object and location. This will become increasingly helpful once you start adding more geometry, cameras, and lights. You should also give _Group_ nodes that encapsulate the objects unique names to signal their contents.


### Renaming Nodes  ###

Every node in the graph has a **node name**:

> ➡ Node name: the name that appears on the node in the _Node Graph_ tab.

Further, every node in the graph that _creates_ an object or a location in the scene (such as _Group_ nodes, _SceneReader_ nodes, and _Camera_ nodes) contains a **scene name**:

> ➡ Scene name: the name of the object or location that the node creates, as it appears in the _Scene Hierarchy_ tab. This is the name that the node adds to the scene, which can be referenced by other nodes.

> Caution :
> Giving two nodes the same scene name may cause downstream nodes to point to objects or locations that no longer exist. If two nodes have the same scene name, and are added to the same position in the scene hierarchy, Gaffer will automatically append a number to the name of the first node to prevent them from conflicting. For example, if you connect two nodes named _Camera_ to a _Group_ node, the first _Camera_ node will be renamed _Camera1_ in the _Group_ node's hierarchy.

First, give some unique names to the _SceneReader_, _Camera_, and _Point Light_ nodes:

1. Rename the _SceneReader_ node:
    1. Select the _SceneReader_ node.
    2. In the _Node Editor_ tab, set the _Node Name_ (above the Node Editor's tabs) to `kitchen`
    3. In the _Node Editor_ tab's _Settings_ tab, set the _Name_ to `kitchen`

2. Set the _Node Name_ and _Name_ values of the _Camera_ node, only name them `main`

3. Set the names of those values of the _Point Light_ to `overhead`

    <!-- TODO: image of the Node Graph so far -->

Next, give the _Group_ nodes some useful names:

1. First node: `geometry`

2. Second node: `cameras`

3. Third node: `lights`

    <!-- TODO: image of the Node Graph so far -->

### Using the _SubTree_ Node ###

So far, each of the _Group_ nodes has its own scene, but none are connected. As in the Gaffer Bot tutorial, you should combine all the scenes for them to work together. This time, you can use a shortcut.

To quickly group multiple nodes together:

1. Select all three group nodes.

2. Without deselecting, create another _Group_ node.

    <!-- TODO: image of the Node Graph so far -->

As you can see, all three _Group_ nodes were automatically joined to the new _Group_ node.

To verify that the hierarchy is working, you should fully expand all three groups (<kbd>Shift</kbd>-click ![the **arrows**](images/arrow.png) in the _Scene Hierarchy_ tab), then use the _Viewer_ tab to look at all the geometry.

With this setup, the geometry, light, and camera groups are kept in respective silos, and will not be able to accidentally interfere with each other and potentially break the scene. Later, when you add more lights to the scene, you can easily add them to the _Lights_ group. In a more complex scene, you could do the same for geometry and cameras.


### Using the _SubTree_ Node ###

Now the scene hierarchy has all 3 _Group_ nodes combined, under a central _Group_ node. This means that every object and location has the parent location `/group/` in the hierarchy. This is unnecessary, so you can use the _SubTree_ node to clip out the `group` parent location, and turn the three sub-groups into the parent locations.

To remove the central `/group/` parent location:

1. Create a _SubTree_ node and connect it to the last _Group_ node.

2. In the 


Now the geometry, light, and camera groups are kept at the root of the hierarchy.

<!-- TODO: GET IMAGE ENGINE SCENE. NO POINT CONTINUING UNTIL THAT'S CONFIGURED -->

## Additional Scene Setup ##

Before starting to add shaders and textures to the scene, you should adjust the camera settings to give you a wider shot, and configure the settings nodes to use the new hierarchy.


### Adjusting the Camera ###

Set up a good angle and field of view (FOV):

1. In the Node Editor, under the _Settings_ tab, set _Field Of View_ to `80`

2. Adjust the camera's position and angle:
    1. Again in the Node Editor, switch to the _Transform_ tab.
    2. Set _Translate_ to `-200` `150` `200`
    3. Set _Rotate_ to `-10` `-55` `0`


### Configuring the  ###



1. Add the main camera to the scene's settings:
    1. Select the _StandardOptions_ node.
    2. In the Node Editor, toggle the switch next to the _Camera_ value to activate it.
    3. In the Scene Hierarchy, expand the _cameras_ location.
    4. Click and drag the _camera_ object onto the _Camera_ value's field in the Node Editor.
    
    <!-- ![`cameras/main` being dragged.]() TODO -->

    The value's field will now read `cameras/main`

2. Add an output render type to the scene's settings:
    1. Select the _Outputs_ node.
    2. In the _Node Editor_ tab, click ![the **plus** button](images/plus.png) and select  _Interactive > Beauty_ from the drop-down menu.


### Increasing the Output Resolution ###

The _StandardOptions_ node by default renders at VGA resolution (640x480). Since the kitchen is a wide scene, and more of the scene's detail could be picked out with a bigger render image, it would be a good idea to increase the render resolution to HD resolution (1920x1080):

1. Select the _StandardOptions_ node.

2. In the Node Editor, under the _Settings_ tab, toggle the switch next to _Resolution_ value's field to activate it.

3. Set _Resolution_ to `1920` `1080`


### Adding Another Viewer Tab ###

As with the Gaffer Bot tutorial, you will want another Viewer tab pinned to the interactive renderer's node, so you can easily switch between viewing the geometry and the render.

First, pin the main Viewer to the last node carrying the scene:

1. Select the _AppleseedRender_ node.

2. Click ![the pin button](images/targetNodesUnlocked.png) at the top-right corner of the top pane to pin the Viewer.

Then, create another Viewer and pin it to the _Catalogue_ node:

2. In the top pane (where the Viewer resides), click [the layout button](images/layoutButton.png) at the top-right. The layout menu will drop down.

3. Select _Viewer_. Another Viewer will open in a new tab next to the first Viewer.

3. Select the _Catalogue_ node.

4. Frame the Viewer on the render output (hover over the Viewer and hit <kbd>F</kbd>).

5. Click ![the pin button](images/targetNodesUnlocked.png) at the top-right corner of the top pane.


## Constraints ##


### Point Lights ###




## Scene Sets ##

This kitchen has a rich assortment of geometry: light sources, paintings, and objects built from a mixture of metals, ceramics, plastics, vinyls, and wood. If we are to texture, shade, and light, and do a small bit of set decoration on this scene, there are more than a trivial number of geometry locations to account for.

Just like when you shaded, textured, and lit Gaffy, the most effective way to build the look of this scene would be to use filters to selectively apply shaders to the various bits of geometry. You are already familiar with filtering by a location's path using the _PathFilter_ node, so that might be an option. But, if you browse the kitchen's locations in the Scene Hierarchy, you will notice that the scene's hierarchy is built corresponding to the spatial location of the objects, rather than by type. Items that would be made of similar material, such as the bowl on the table and the plates in the sink, are in different parts of the hierarchy, and have different names. Making this even more challenging is that several objects are made of multiple different materials. Using _PathFilter_ nodes to assign the same or similar shaders to so many parts in so many disparate locations would require at best a significant number of filter nodes, and at worst filtering the filters.

Using **sets** will solve this problem. Sets are essentially path filters that have their own name, that you can reference elsewhere: for instance, you could create a set named "Plates," and add the geometry location of each plate. Later, whenever you wanted to manipulate the plates, you would only need to refer to the "Plates" set, instead of re-filtering the plates again.


### Creating a "Ceramics" Set ###


### Creating a "Cabinets" Set ###


### Creating a "Floor" Set ###


## Textures ##


## Recap ##

remind user of what they learned


## See Also ##

* [Tutorial: Assembling the Gaffer Bot](../BeginnerTutorial/index.md)
* [Tutorial: Turntable Tutorial](../TurntableTutorial/index.md)
* [Tutorial: Basic Scripting](../BasicScriptingTutorial/index.md)
* [Graph flow](../../UnderstandingTheNodeGraph/GraphFlow/index.md)
* [Node types](../../UnderstandingTheNodeGraph/NodeTypes/index.md)