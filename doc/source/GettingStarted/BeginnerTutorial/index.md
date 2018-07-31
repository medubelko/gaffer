# Tutorial: Assembling the Gaffer Bot #

This tutorial is intended to give you a first taste of Gaffer by covering the basic operations and concepts. The goal is for you to learn to make renders of a basic scene as quickly as possible, and provide a minimal basis for further exploration using the rest of the the Gaffer documentation. It will cover a lot of ground quickly, and some details will be glossed over.

By the end of this tutorial you will have built a basic scene with Gaffer's robot mascot, Gaffy, and render an output image. You will learn the following lessons, but not necessarily in this order: 

* Gaffer UI fundamentals
* Creating and connecting nodes
* Importing geometry
* Constructing a basic scene hierarchy
* Adding basic script settings
* Importing textures
* Building a simple shader
* Applying a shader to geometry
* Creating an environment light
* Using an interactive renderer

> Note :
> This tutorial will use the Appleseed renderer, as it is included with Gaffer out of the box. While the Appleseed-specific nodes that we use here can be substituted with equivalents from Arnold or 3Delight, we recommend that you complete this tutorial using Appleseed before moving on to your renderer of choice.


## Starting a New Script ##

After [installing Gaffer](../InstallingGaffer/index.md), launch Gaffer [from its directory](../LaunchingGafferFirstTime/index.md) or [using the "gaffer" command](../SettingUpGafferCommand/index.md). A new Gaffer window will open, and you will be presented with an empty graph in the default UI layout.

![An empty graph in the default layout.](images/defaultLayout.png)

> Note :
> While Gaffer is a node graph application, and you will mainly be interacting with a graph, to avoid confusion between Gaffer files and the node graph, we will refer to the projects/files you work on as **scripts**.


## Importing a Geometry Scene Cache ##

As Gaffer is a tool primarily designed for LookDev, lighting, and VFX process automation, we expect that your scene's modelling and animation will be created in an external tool like Maya, and then imported into Gaffer as a geometry/animation cache. Gaffer supports the standard Alembic (.abc) and USD (.usd) file formats, as well as its own native SceneCache (.scc) file format. Most scenes begin by importing geometry or images via either of the two _reader nodes:_ [SceneReader](../../Reference/NodeReference/GafferScene/SceneReader.md) or [ImageReader](../../Reference/NodeReference/GafferScene/ImageReader.md).

First, load Gaffy's geometry cache with a _SceneReader_ node:

1. In the _Node Graph_ tab in the lower left of the window, right-click. The node creation menu will appear.

2. Using the drop-down menu, select _Scene > File > Reader_. The _SceneReader_ node will appear in the _Node Graph_ tab and be selected automatically. Each of the other tabs will update to reflect this selection.
    
    ![A new SceneReader node.](images/emptySceneReader.png) <!-- TODO: add annotation? -->

3. The _Node Editor_ tab in the top-right pane now reads _Node Editor : SceneReader_. Under its _Settings_ sub-tab, in the _File Name_ value's field, type: `${GAFFER_ROOT}/resources/gafferBot/caches/gafferBot.scc`

4. Hover the cursor over the background of the _Viewer_ tab (in the top pane). Then, hit <kbd>F</kbd>. The view will reframe to cover the whole scene.
    
    ![The bounding box of the selected SceneReader node.](images/sceneReaderBound.png) <!-- TODO: add annotation -->

The _SceneReader_ node has loaded, and the _Viewer_ tab is showing a bounding box, but the geometry remains invisible. You can confirm that the scene has loaded by examining the _Scene Hierarchy_ tab in the bottom-right pane. It too has updated, and shows that you have *GAFFERBOT* at the root of the scene. In order to view the geometry, you will need to traverse the scene's locations and expand down to the geometry.

> ➡ By default, the _Viewer_, _Node Editor_, and _Scene Hierarchy_ tabs update to reflect the selected node, and go blank when no node is selected.


## The Scene Hierarchy ##

When you load a geometry cache, Gaffer only reads its scene hierarchy: at no point does it write to the file. This lets you manipulate the scene's locations without risk to the source file.

> ➡ Scenes hierarchies in Gaffer can have their locations non-destructively hidden, added to, changed, and deleted.

<!-- TODO: move this paragraph somewhere more appropriate -->

Further, Gaffer uses locations in the scene's hierarchy to selectively render the geometry you need: expanded locations have their geometry shown in the _Viewer_ tab, while collapsed locations appear only as bounding boxes. This on-demand geometry loading allows Gaffer to handle highly complex scenes (we informally call it "lazy loading"). Currently, only a bounding box is visible in the _Viewer_ tab.

> ➡ Only geometry that has its parent locations expanded will display in the _Viewer_ tab.

> ➡ Geometry that has not had its parent locations expanded is displayed as a bounding box.


### Navigating the Scene Using the _Scene Hierarchy_ tab ###

Until you navigate the scene's locations in the _Scene Hierarchy_ tab and expand further down, Gaffy's geometry will remain invisible.

Use the _Scene Hierarchy_ tab to view Gaffy's geometry:

1. Make sure the _SceneReader_ node is selected (if it isn't, click it).

2. In the _Scene Hierarchy_ tab, click the triangle next to *GAFFERBOT*. The *GAFFERBOT* location will expand to show a child location named *C_torso_GRP*.

3. Click ![the triangle](images/collapsedLocation.png) next to *C_torso_GRP* to show its child locations.

    ![The scene hierarchy, expanded down two levels.](images/sceneHierarchyExpandedTwoLevels.png) <!-- TODO: add annotation -->

In the _Viewer_ tab, you can now see the bounding boxes of multiple geometry primitives (or groups of primitives), revealing more of the scene's structure. However, it would be tedious to expand the whole scene, location-by-location, in this manner. Instead, you can use a shortcut.

Expand a location, its children, and all their sub-children by <kbd>Shift</kbd>-clicking:

1. In the _Scene Hierarchy_ tab, <kbd>Shift</kbd>-click ![the triangle](images/collapsedLocation.png) next to *C_head_GRP*. All the locations under *C_head_GRP* will expand. Now the _Viewer_ tab will display all of the geometry that comprises Gaffy's head.

2. <kbd>Shift</kbd>-click ![the triangle](images/collapsedLocation.png) next to *L_legUpper_GRP*. All the locations under *L_legUpper_GRP* will expand. Now the _Viewer_ tab will display all of the geometry that comprises Gaffy's left leg.

    ![The head and left leg geometry, expanded.](images/headAndLegExpanded.png)

> Note :
> Gaffy's geometry file contains primitive and location names with affixes like *C*, *R*, *L*, *GRP*, *CPT* and *REN*. Gaffer places no significance whatsoever on these names, and you or your studio are free to use whichever naming conventions you see fit.


### Navigating the Scene Using the _Viewer_ tab ###

As you navigated the scene using the _Scene Hierarchy_ tab, the _Viewer_ tab updated to display the geometry you expanded. Usefully, you can also expand the scene by directly using the _Viewer_ tab itself. Navigating individual parts of a scene like this can be invaluable when dealing with very complex scenes.

Use the arrow keys to navigate the scene hierarchy in the _Viewer_ tab:

1. In the _Viewer_ tab, select Gaffy's right leg by click-dragging over its bounding box. The leg's bounding box will highlight.

2. Hit <kbd>↓</kbd> to expand the selection down one level. The highlighted bounding box will be replaced by two smaller bounding boxes, indicating that you have selected the right leg's children.

3. Hit <kbd>Shift</kbd>-<kbd>↓</kbd> to fully expand all the right leg's locations.

    ![The head and legs geometry, expanded.](images/headAndLegsExpanded.png) <!-- TODO: make this screenshot select the geometry -->

You can also collapse the selection using the _Viewer_ tab:

1. With the right leg geometry selected, hit <kbd>↑</kbd>.

2. Keep hitting <kbd>↑</kbd> until all the geometry is collapsed back into the root bounding box.

You may have noticed that when you expanded and collapsed parts of the scene using the _Viewer_ tab, the locations and geometry were also highlighted and selected in the _Scene Hierarchy_ tab. This is because:

> ➡ Manually selecting, expanding, and collapsing elements of the scene in the _Viewer_ tab is synonymous with using the _Scene Hierarchy_ tab.


<!-- Section disabled for now. Pinning is more useful to new users and accomplishes the same thing. -->
<!-- ### Fully Expanding the Current Scene in the _Viewer_ tab ### -->

<!-- Since Gaffy's scene is simple and loads quickly, it would be convenient to automatically keep all of its geometry loaded at all times. To do this, you can tell the _Viewer_ tab to always expand the whole scene, using the _Expansion_ menu in the _Viewer_ tab: -->

<!-- 1. At the top of the _Viewer_ tab, click ![the expansion menu button](images/expansion.png). The expansion menu will drop down. -->

<!-- 2. Select "Expand All". Gaffy will finally become fully visible. -->

<!--     ![The full character geometry.](images/fullyExpanded.png) -->

<!-- This can be especially helpful when you want to see the effect your changes on parts of a scene have within the context of the whole scene. One thing to note about using the _Expansion_ menu: -->

<!-- > ➡ The _Viewer_ tab's _Expansion_ menu settings apply to whichever scene you have selected. -->

<!-- If you have the _Viewer_ tab set to fully expand, and your graph contains a different scene, if you select the other scene, that scene's geometry will fully expand. -->

<!-- > Caution :
> In scripts with very complex geometry scenes, setting the _Viewer_ tab to _Expand All_ will be extremely resource intensive, and may cause lag and instability. -->


## Adjusting the View in the _Viewer_ tab ##

Like in other 3D tools, you can adjust the angle, field of view, and position of the virtual camera in the _Viewer_ tab.

* To rotate, <kbd>Alt</kbd>-click and drag.
* To dolly in and out, <kbd>Alt</kbd>-right click and drag.
    * You can also dolly by scrolling the middle mouse.
* To track from side to side, <kbd>Alt</kbd>-middle click and drag.

> Tip :
> If you lose sight of the scene and cannot find your place again, you can always refocus on the currently selected geometry/location by hovering the cursor over the _Viewer_ tab and hitting <kbd>F</kbd>.


## Creating and Setting Up a Camera ##

Before you can render anything, you will need to create a camera to render from. Just like how you created a _SceneReader_ node to load in the geometry, you will create another node to generate a camera.

Earlier, you learned how to find a node by navigating the node creation menu in the _Node Graph_ tab. If you know the name of the node you wish to create, and do not feel like navigating the menu, you can use the menu's search:

1. Hover the cursor over the background in the _Node Graph_ tab.

2. Right-click. The node creation menu will open.

    > Tip :
    > With the cursor hovering over the _Node Graph_ tab, you can also hit <kbd>Tab</kbd> to open the node creation menu.

3. Type `Camera`. A list of search results will appear. By default, _Camera_ will be highlighted.

4. Hit <kbd>Enter</kbd> to create a new _Camera_ node.

    ![A new Camera node.](images/camera.png)

As before, the newly created node will be selected automatically, and the _Viewer_, _Scene Hierarchy_, and _Node Editor_ tabs will update to reflect this new selection.


## Nodes, Scenes, and Plugs ##

So far, your script is set up as such: The _SceneReader_ node is outputting a scene containing Gaffy's geometry, and the _Camera_ node is outputting a scene containing a camera. Since neither node is connected, each scene remains separate. This is because each node in Gaffer outputs an entire self-contained scene hierarchy at its position in the graph. If they aren't connected somewhere later in the graph, the two scenes will never interface with each other. A key part to understand about the node graph is that:

> ➡ Each node contains either the scene that has been passed to it through a plug, or the scene that it creates.

<!-- TODO: find a better location for this paragraph? -->

> Note :
> Since scenes in Gaffer contain more than just geometry, we will generically refer to everything in the scene hierarchy that isn't a location as an **object**.

In short, the scene is not a single hierarchy that exists in the background of the graph, but is instead carried by the nodes. You can test this by clicking the background of the _Node Graph_ tab, and observing that once the you have no node selected, the _Scene Hierarchy_ tab goes blank. This will become very relevant when you begin combining scenes together and selectively modifying a scene's locations.

For your two nodes to occupy the same scene (and later render together), you will need to combine them into a single scene at some point later in the graph. You can connect them together using a _Group_ node via their **plugs**, and you can also rearrange the nodes to better represent the visual hierarchy.


### Plugs ###

Gaffer allows scenes to be built and modified by creating connections between nodes. For most nodes, the scene flows into it through its input, is then modified by the node, and then flows out through it. A node's inputs and outputs are called **plugs**, and are represented in the _Node Graph_ tab as colored circles around a node's edges.

<!-- TODO: add close-up of nodes -->

### Connecting Plugs ###

It's time to connect the _SceneReader_ and _Camera_ nodes to combine their scenes:

1. Click the background of the _Node Graph_ tab to deselect all nodes.

2. Create a _Group_ node _(Scene > Hierarchy > Group)_.

3. Click and drag the _SceneReader_ node's _out_ plug (at the bottom; blue) onto the _Group_ node's _in0_ plug (at the top; also blue). As you drag, a node connector will appear. Once you connect them, a second input plug (_in1_) will appear on the _Group_ node, next to the first.

4. Click and drag the _Camera_ node's _out_ plug onto the _Group_ node's _in1_ plug.

    ![A new Group node.](images/group.png)

The _Group_ node is now generating a new scene combining the input scenes from the node above it under a new parent location called _group_. You can see this new hierarchy by selecting the _Group_ node and examining the _Scene Hierarchy_ tab.

Only the combined scene at the _Group_ node has been modified. The upstream nodes' scenes are unaffected. You can verify this by reselecting one of them and checking the _Scene Hierarchy_ tab.


### Selecting, Moving, and Duplicating Nodes ###

You may have noticed that you can intuitively click and drag the nodes around in the _Node Graph_ tab. Nodes can also be manipulated using other standard selection and copy-paste actions.

* To select multiple nodes, click and drag on the background of the _Node Graph_ tab.
    * You can also add or remove a node from your selection by holding <kbd>Shift` and clicking the node.
* You can copy and paste nodes using the standard <kbd>Ctrl</kbd>-<kbd>C</kbd> and <kbd>Ctrl</kbd>-<kbd>V</kbd> combinations.

You can pan and zoom around the _Node Graph_ tab, just like in the _Viewer_ tab.

* To pan the view, <kbd>Alt</kbd>-click and drag.
    * You can also pan by middle-clicking and dragging.
* To zoom in and out, <kbd>Alt</kbd>-right-click and drag.
    * You can also zoom by scrolling the middle mouse.
* To focus on the currently selected node, hover the cursor over the _Node Graph_ tab and hit <kbd>F</kbd>.

Try organizing the graph:

1. Click and drag the _SceneReader_ node to the left.
2. Click and drag the _Camera_ node to the right.
3. Click and drag the _Group_ node below the other two nodes.

    <!-- ![Rearranged nodes.]()  TODO -->


## Positioning the Camera ##

Next, you should reposition the camera so that it frames Gaffy.

To do this, you need to edit values in the _Node Editor_ tab:

1. Select the _Camera_ node.

2. In the _Node Editor_ tab, click the **Transform** tab.

3. Edit the _Translate_ and _Rotate_ values to set the camera's position:
    * Set _Translate_ to `19` `13` `31`
    * Set _Rotate_ to `0` `30` `0`

    ![The transform values.](images/cameraTransform.png)

4. Select the _Group_ node, then hover the cursor over the _Viewer_ tab, and hit <kbd>F</kbd> to see Gaffy and the camera in the same framing.

> Note :
> In the previous section, we referred to the inputs and outputs of the nodes as **plugs**, and connected them by dragging and dropping within the _Node Graph_ tab. But in fact, the _Translate_ and _Rotate_ values you just edited in the _Camera_ node are _also_ plugs: they also provide input to the node, and can also be connected together if needed. The _Node Graph_ and _Node Editor_ tabs each display only a subset of the available plugs for ease of use.


## Rendering Your First Image ##

Now that you have defined the layout of your scene, you should perform a quick test-render to check that everything is working as expected. To do that, you need to place some render-related nodes to define your script's render settings.

1. Select the _Group_ node.

2. Create a _StandardOptions_ node _(Scene > Globals > StandardOptions)_. It will automatically connect to the output of the _Group_ node and become selected.

3. Create an _AppleseedOptions_ node _(Appleseed > Options)_. It will connect automatically to the output of the _StandardOptions_ node and become selected.

4. Create an _Outputs_ node _(Scene > Globals > Outputs)_. It will connect and become selected like the others.

5. Create an _InteractiveAppleseedRender_ node _(Appleseed > InteractiveRender)_.

6. Create a _Catalogue_ node _(Image > Utility > Catalogue)_. It doesn't need to be connected. Instead, place it next to the _InteractiveAppleseedRender_ node.

    ![The render-related nodes.](images/renderSettings.png)

Briefly, here is the function of each of these nodes:
* _StandardOptions_ node: Determines the camera, resolution, and blur settings of the scene.
* _AppleseedOptions_ node: Determines the settings of the Appleseed renderer.
* _Outputs_ node: Determines what kind of output render will be created.
* _InteractiveAppleseedRender_ node: An instance of Appleseed's interactive (responsive) renderer.
* _Catalogue_ node: A global list of images/renders that you can preview within Gaffer. Renders you generate will appear in this node's list.

In keeping with what we said earlier about scenes being passed to nodes: with the exception of the _Catalogue_ node, each of these render nodes only apply to the scene delivered to them through their input plugs. If you had another unconnected scene running in parallel, none of these render settings would apply to it.

Although the scene contains a camera, you will need to point the _StandardOptions_ node to it:

1. Select the _StandardOptions_ node.

2. Specify the camera using the _Node Editor_ tab:
	1. Click the _Camera_ header to expand its section.
	2. Toggle the switch next to the _Camera_ value to enable it.
	3. Type `/group/camera` into the _Camera_ value's field.

Next, you need to add an image type to render:

1. Select the _Outputs_ node.

2. In the _Node Editor_ tab, click ![the plus button](images/plus.png) and select  _Interactive > Beauty_ from the drop-down menu.

With all the settings complete, start the interactive renderer:

1. Select the _InteractiveAppleseedRender_ node.

2. In the _Node Editor_ tab, click the **play button** to start the renderer.

3. Select the _Catalogue_ node.

4. Hover the cursor over the _Viewer_ tab and hit <kbd>F</kbd> to frame the _Catalogue_ node's preview image.

    ![The first render.](images/firstRender.png)

Congratulations! You have successfully rendered your first image. Gaffy is currently lacking shading, lighting, and texturing. We will move on to those soon. First, you should adjust the UI to provide yourself a more optimal workflow.


## Pinning a Tab to a Node ##

As mentioned earlier, the _Viewer_, _Scene Hierarchy_, and _Node Editor_ tabs each show their respective outputs of the currently selected node. This is not always convenient, because often you will need to edit one node while viewing the output of another. You can solve this by **pinning** a tab while a node is selected, which keeps that tab focused on that node.

To make switching between vieweing Gaffy's geometry and the render easier, you can modify the UI so you're working with two Viewers. First, start by pinning the last node in the graph that contains the scene:

1. Select the _InteractiveAppleseedRender_ node.

2. Click ![the pin button](images/targetNodesUnlocked.png) at the top-right
  of the top pane. The pin button will highlight (![highlighted pin](images/targetNodesLocked.png)).

The _Viewer_ tab is now locked to the _InteractiveAppleseedRender_ node's scene (which contains all of the parts from its upstream scenes), and will only show that scene, even if you deselect it or select a different node.

Next, pin the same node to the _Scene Hierarchy_ tab. This time, use the middle-click shortcut:

1. Middle-click and drag the _InteractiveAppleseedRender_ node from the _Node Graph_ tab into the
  _Scene Hierarchy_ tab.
  
As with the _Viewer_ tab, the _Scene Hierarchy_ tab will now remain locked to the output of _InteractiveAppleseedRender_, regardless of your selection. Now you are free to select any node for editing in the _Node Editor_ tab, but you will always be viewing the final results of the last node in the graph.

For the final adjustment to the UI, create another _Viewer_ tab and pin the _Catalogue_ node to it.

1. At the top-right of the top pane, click ![the layout menu button](images/layoutButton.png). The layout menu will open.

2. Select _Viewer_. A new _Viewer_ tab will open.

3. Middle-click and drag the _Catalogue_ node onto the new _Viewer_ tab. That _Viewer_ tab is now pinned to that node.

Now you can switch between the scene's geometry (first _Viewer_ tab) and the rendered image (second _Viewer_ tab). Now it is time to shade Gaffy.


## Adding Shaders and Lighting ##

It's time to add shaders and lighting. It will help to think of a graph as being composed of three distinct phases: generating the geometry, applying the lighting and shading, and rendering. Lights act like another component of the scene, so you can combine one with the scene nodes. The shaders, however, are different: in order for the renderer nodes to apply to the geometry and to inherit the shaders, you will need to add them somewhere between the scene-creating nodes and render nodes.


### Making Some Space ###

Since you will be adding shaders nodes between the scene nodes and the render nodes, you will first need to add some space in the graph.

To create some empty space in the centre of the graph:

1. Select the lower five nodes by clicking and dragging over them.
2. Drag the nodes down.

    ![The graph with some added space.](images/renderSettingsWithGap.png)


### Adding a Shader ###

Now that you have more space, add some shading nodes:

1. Below and to the left of the _Group_ node, create a _Disney Material_ node *(Appleseed > Shader > Material > As_Disney_Material)*.

2. In the _Node Editor_ tab, give the shader some reflective surface properties:
	* Set _Specular_ to `0.6`
	* Set _Roughness_ to `0.35`

3. With the _Disney Material_ node still selected, create a _ShaderAssignment_ node _(Scene > Attributes > ShaderAssignment)_.

4. Click and drag the _ShaderAssignment_ node onto the connector connecting the _Group_ and _StandardOptions_ nodes. The _ShaderAssignment_ node will be interjected between them.

    ![The ShaderAssignment and Disney Material nodes.](images/firstShaderAssignment.png)

Note that the input and output plugs on the Disney Material node flow from left to right. This is because in Gaffer:

> ➡ Scenes flow from top to bottom, and shaders flow from left to right.

In your newly shaded graph, the _ShaderAssignment_ node takes the material flowing in from the left and assigns it to Gaffy's geometry flowing in from the top. Now that Gaffy has received a proper material assignment, you will need to light the scene.


### Adding an Environment Light ###

Lights, like geometry and cameras, are objects that need to be combined with the main scene. For simplicity, you should add a global environment light:

1. Create a _PhysicalSky_ node _(Appleseed > Environment > PhysicalSky)_.

2. Place it next to the _Camera_ node.

3. In the _Node Editor_ tab, adjust the node's angle and brightness:
	* Set the _Sun Phi Angle_ to `100`
	* Set the _Luminance_ to `2.5`

4. Connect the _PhysicalSky_ node's _out_ plug to the _Group_ node's _in3_ plug.

<!-- TODO: image with environment light connected to the Group node ![A new and connected environment light node.](a.png) -->

For the light to take effect, you will need to enable environment lighting in the _AppleseedOptions_ node:

1. Select the _AppleseedOptions_ node.

2. In the _Node Editor_ tab, expand the _Environment_ section.

3. Toggle the switch next to the _Environment Light_ value to enable it.

4. Type `/group/light` into the _Environment Light_ value's field.

The interactive render will now be in the process of updating, and you will be able to see Gaffy with some basic shaders and lighting.

![The first render with shaders and lighting.](images/firstLighting.png)


### Adding Textures ###

As Gaffy is looking a bit bland, you should assign some textures to the shader:

1. Create an _Appleseed Color Texture_ node *(Appleseed > Shaders > Texture2d > As_color_texture)*.

2. In the _Node Editor_ tab, point the node to the textures:
	1. Type `${GAFFER_ROOT}/resources/gafferBot/textures/base_COL/base_COL_` into the _Filename_ value's field.
	2. Select `mari` from the _UDIM_ drop-down menu.

3. In the _Node Graph_ tab, connect the _AppleSeed Color Texture_ node's _ColorOut_ plug to the _Disney Material_ node's _BaseColor_ plug. Gaffy's textures will now mix with the shader, and the render will update to show the combined results.

    ![Gaffy with textures.](images/textures.png)


### Adding Another Shader ###

With the textures assigned, the surface of all of Gaffy's geometry looks the same, because the material shader is applying to everything. To fix this, you should create an additional metallic shader and apply it selectively to different parts of the geometry.

Begin by creating another shader:

1. Create another _Disney Material_ node.

2. In the _Node Editor_ tab, give the shader some metallic properties:
	1. Set _Metallic_ to `0.8`
	2. Set _Roughness_ to `0.4`

3. With the new _Disney Material_ node still selected, create another _ShaderAssignment_ node

4. Click and drag the new _ShaderAssignment_ node onto the connector under the first _ShaderAssignment_ node. The new _ShaderAssignment_ node will come after the fist shader in the graph flow.

    ![A second shader on the node graph.](images/secondShaderAssignment.png)

The _Viewer_ tab will update to show the new shader.

![The second shader, rendered.](images/secondShaderAssignmentRender.png)

You will immediately notice something is wrong: _all_ the geometry is metallic. The new shader has overridden the previous one. This is because:

> ➡ The last _ShaderAssignment_ node applied to geometry in a scene takes precedence over all others.

### Filtering a Shader ###

In order to selectively apply a shader to only certain parts of the scene's geometry, you will need to **filter** the shader assignment, using a filter node that selects parts of a scene by name:

1. Create a _PathFilter_ node _(Scene > Filters > PathFilter)_.

2. In the _Node Editor_ tab, click ![the plus button](images/plus.png) next to _Paths_. This will add a new text field.

3. Double-click the text field and type `/group/GAFFERBOT/C_torso_GRP/C_head_GRP/C_head_CPT/L_ear001_REN`. This is the full path to Gaffy's left ear.

4. Connect the _PathFilter_ node's _out_ plug to the filter input on the right hand side of the _ShaderAssignment1_ node's filter plug (yellow; on the right).

    ![The connected _PathFilter_ node.](images/filterConnection.png)

Now when you check the render, you will see that the chrome shader is only applied to Gaffy's left ear. There are many other parts of Gaffy that could use the chrome treatment, but it would be tedious for you to manually enter multiple locations. There are two ways you can more easily add geometry to the filter: using text wildcards, and interacting directly with the geometry.


#### Filtering Using Wildcards ####

A wildcard tells text interpreters to take a value of any length where there is an asterisk (`*`). They are useful if you know part of a path, but don't want to have to look up or type it in its entirety. Earlier, you used `/group/GAFFERBOT/C_torso_GRP/C_head_GRP/C_head_CPT/L_ear001_REN`, which only pointed to the left ear. You could apply the filter to _both_ ears by adding wildcards to the `/L_ear001_REN` location in the path.

To use a wildcard in the path filter:

1. Select the _PathFilter_ node.

2. In the _Node Editor_ tab, double-click the path field you created earlier, and change it to `/group/GAFFERBOT/C_torso_GRP/C_head_GRP/C_head_CPT/*_ear*`. The filter will now match the left and the right ears.


#### Filtering by Dragging Selections ####

As your final operation, you should add the metallic shader to the rest of the appropriate parts of Gaffy.

This time, you can add to the path filter using a visual method:

1. In the _Viewer_ tab, switch to the tab containing the 3D geometry view.
2. Zoom and pan to Gaffy's face.
3. Click the eyebrows to select them.
4. <kbd>Shift</kbd>-click the mouth to add it to the selection.

    ![The face, with selection.](images/faceSelection.png)

5. Click and drag the selection, and hold it over the _PathFilter_ node without releasing. The cursor will change to ![the "replace objects" icon](images/replaceObjects.png).

6. While still dragging, hold <kbd>Shift</kbd>. The cursor will change to ![the "add objects" icon](images/addObjects.png). You are now adding to the path, rather than replacing it.

7. Release the selection over the _PathFilter_ node. This will add them as new path fields to the node.

Just as objects can be added by holding <kbd>Shift</kbd>, they can be removed (![the "remove objects" icon](images/removeObjects.png)) by holding <kbd>Control</kbd>. With this in mind, you can add and remove objects from path filter as you see fit. Remember to switch between the _Viewer_ tabs to check the render output as it updates. After adding Gaffy's hands and bolts to the filter, you should arrive at an image similar to this:

![The final render.](images/finalRender.png)


## Recap ##

Congratulations! You've built and rendered your first scene in Gaffer.

You should now have a basic understanding of Gaffer's interface, the concept of a scene and how it flows, how to manipulate the scene, how to interact with and adjust the interface, and how to add geometry, lights, textures, and shaders.

This provide a solid basis for your further learning and exploration. Follow the links below to learn more.

## See Also ##

* [Installing Gaffer](../InstallingGaffer/index.md)
* [Launching Gaffer for the first time](../LaunchingGafferFirstTime/index.md)
* [Setting up the "Gaffer" command](../SettingUpGafferCommand/index.md)
* [Tutorial: Everything But the Kitchen Sink](../IntermediateTutorial/index.md)
* [Graph flow](../../UnderstandingTheNodeGraph/GraphFlow/NodeTypes/index.md)
* [Node types](../../UnderstandingTheNodeGraph/GraphFlow/GraphFlow/index.md)
* [Manipulating the scene hierarchy](../../WorkingWithScenes/ManipulatingSceneHierarchy/index.md)
