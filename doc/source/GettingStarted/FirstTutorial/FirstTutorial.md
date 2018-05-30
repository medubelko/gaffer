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


## Starting a New Graph ##

After [installing Gaffer](../InstallingGaffer/InstallingGaffer.md), launch Gaffer [from its directory](../LaunchingGafferFirstTime/LaunchingGafferFirstTime.md) or [using the "gaffer" command](../SettingUpGafferCommand/SettingUpGafferCommand.md). A new Gaffer window will open, and you will be presented with an empty graph in the default UI layout.

![An empty graph in the default layout.](images/defaultLayout.png)


## Loading a Geometry Scene Cache ##

As Gaffer is a tool primarily designed for LookDev, lighting, and VFX process automation, we expect that your scene's modelling and animation will be created in an external tool like Maya, and then imported into Gaffer as an animation cache. Gaffer supports the popular Alembic (.abc) and USD (.usd) file formats, as well as its own native SceneCache (.scc) file format.

Most scenes begin by loading geometry or images via either of the two _reader nodes:_ [SceneReader](../../Reference/NodeReference/GafferScene/SceneReader.md) or [ImageReader](../../Reference/NodeReference/GafferScene/ImageReader.md).

First, load Gaffy's geometry cache:

1. In the [_Node Graph_ tab]() in the lower left of the window, right-click. The New Node drop-down menu will appear.

2. Next, create a _SceneReader_ node: using the drop-down menu, navigate to _Scene > File_, and select **Reader**. The _SceneReader_ node will appear in the _Node Graph_ tab and be selected automatically. Each of the other tabs will update to reflect this selection.
    
    ![A new SceneReader node.](images/emptySceneReader.png) <!-- TODO: add annotation? -->

3. The [_Node Editor_ tab]() in the top-right pane now reads _Node Editor : SceneReader_. Under the _Settings_ sub-tab, in the _File Name_ field, type: `${GAFFER_ROOT}/resources/gafferBot/caches/gafferBot.scc`

4. In the top pane, in the _Viewer_ tab, hover the cursor over the background. Then, hit <span class="keystroke">F</span>. The the view will reframe to cover the whole scene.
    
    ![The bounding box of the selected SceneReader node.](images/sceneReaderBound.png) <!-- TODO: add annotation -->

The _SceneReader_ node has loaded, and the Viewer is showing a bounding box, but the geometry remains invisible. You can confirm that the scene has loaded by examining the _Scene Hierarchy_ tab in the bottom-right pane. It too has updated, and shows that you have *GAFFERBOT* at the root of the scene. In order to view the geometry, you will need to traverse the scene's _locations_ and expand down to the geometry.


## The Scene ##

First, we should clarify what we mean by **scene**. Geometry scene files typically contain a series of directories, called locations, that organize the geometry. At the deepest level of these locations is the geometry primitives themselves. All the parent locations above them are merely symbolic. Gaffer uses this paradigm to both build scenes (by adding, removing, and combining locations), and selectively render the geometry it thinks you need (by only showing geometry primitives that have had their locations expanded).

> ➡ When manipulating scenes, the underlying geometry remains unchanged, and only the scene locations are being modified.

This explicit scene location expansion allows Gaffer to handle highly complex scenes. Gaffer only processes expanded locations in the scene. We informally call this "lazy loading." Currently,only a bounding box is visible in the _Viewer_ tab. This is because:

> ➡ Any geometry that has not had its parent locations expanded is displayed as a bounding box.


### Navigating the Scene Using the Scene Hierarchy ###

Until you navigate the scene's locations in the _Scene Hierarchy_ tab (from here on we will just refer to it as the Scene Hierarchy) and expand further down, Gaffy's geometry will remain invisible. It's time to explore the locations in Gaffy's scene:

1. Select the _SceneReader_ node by clicking it.

2. In the Scene Hierarchy, click the triangle next to *GAFFERBOT*. The *GAFFERBOT* location will expand to show a child location named *C_torso_GRP*.

3. Click the triangle next to *C_torso_GRP* to show its child locations.

    ![The scene hierarchy, expanded down two levels.](images/sceneHierarchyExpandedTwoLevels.png) <!-- TODO: add annotation -->

In the _Viewer_ tab, you can now see the bounding boxes of multiple primitives (or groups of primitives), revealing more of the scene's structure. However, it would be tedious to expand the whole scene, location-by-location, in this manner. Instead, you can expand a location, its children, and all their sub-children by <span class="keystroke">Shift</span>-clicking:

1. In the Scene Hierarchy, <span class="keystroke">Shift</span>-click the triangle next to *C_head_GRP*. All the locations under *C_head_GRP* will expand. Now the _Viewer_ tab will display all of the geometry that comprises Gaffy's head.

2. <span class="keystroke">Shift</span>-click the triangle next to *L_legUpper_GRP*. All the locations under *L_legUpper_GRP* will expand. Now the _Viewer_ tab will display all of the geometry that comprises Gaffy's left leg.

    ![The head and left leg geometry, expanded.](images/headAndLegExpanded.png)

> Note :
> You may have noticed that Gaffy's geometry file contains primitives and locations named using specific conventions, with affixes like *C*, *R*, *L*, *GRP*, *CPT* and *REN*. Gaffer places no significance whatsoever on these names, and you or your studio are free to use whichever naming conventions you see fit.


### Navigating the Scene Using the Viewer ###

As you navigated the scene using the Scene Hierarchy, the _Viewer_ tab (from here on we will just refer to it as the Viewer) updated to display the geometry you expanded. Usefully, you can also expand the scene by directly using the Viewer itself. Navigating individual parts of a scene like this can be invaluable when dealing with very complex scenes:

1. In the Viewer, select Gaffy's right leg by click-dragging over its bounding box. The leg's bounding box edges will highlight.

2. Hit <span class="keystroke">↓</span> to expand the selection down one level. The highlighted bounding box will be replaced by two smaller bounding boxes, indicating that you have selected the right leg's children.

3. Hit <span class="keystroke">Shift</span>-<span class="keystroke">↓</span> to fully expand all the right leg's locations.

    ![The head and legs geometry, expanded.](images/headAndLegsExpanded.png) <!-- TODO: make this screenshot select the geometry -->

You can also collapse the selection using the Viewer:

1. With the right leg geometry selected, hit <span class="keystroke">↑</span>.

2. Keep hitting <span class="keystroke">↑</span> until all the geometry is collapsed back into the root bounding box.

You may have noticed that when you expanded and collapsed parts of the scene using the Viewer, the locations and geometry were also highlighted and selected in the Scene Hierarchy. This is because:

> ➡ Manually selecting, expanding, and collapsing elements of the scene using the Viewer is synonymous with using the Scene Hierarchy.


<!-- Section disabled for now. Pinning is more useful to new users and accomplishes the same thing. -->
<!-- ### Fully Expanding the Current Scene in the Viewer ### -->

<!-- Since Gaffy's scene is simple and loads quickly, it would be convenient to automatically keep all of its geometry loaded at all times. To do this, you can tell the Viewer to always expand the whole scene, using the _Expansion_ menu in the Viewer: -->

<!-- 1. At the top of the Viewer, click ![the expansion menu button](images/expansion.png). The expansion menu will drop down. -->

<!-- 2. Select "Expand All". Gaffy will finally become fully visible. -->

<!--     ![The full character geometry.](images/fullyExpanded.png) -->

<!-- This can be especially helpful when you want to see the effect your changes on parts of a scene have within the context of the whole scene. One thing to note about using the _Expansion_ menu: -->

<!-- > ➡ The Viewer's _Expansion_ menu settings apply to whichever scene you have selected. -->

<!-- If you have the Viewer set to fully expand, and your graph contains a different scene, if you select the other scene, that scene's geometry will fully expand. -->

<!-- > Caution :
> In graphs with very complex geometry scenes, setting the Viewer to _Expand All_ will be extremely resource intensive, and may cause lag and instability. -->


### Adjusting the View in the Viewer ###

Like in other 3D tools, you can adjust the angle, field of view, and position of the virtual camera in the Viewer.

* To rotate, <span class="keystroke">Alt</span>-click and drag.
* To dolly in and out, <span class="keystroke">Alt</span>-right click and drag.
    * You can also dolly by scrolling the middle mouse.
* To track from side to side, <span class="keystroke">Alt</span>-middle click and drag.

> Tip :
> If you lose sight of the scene and cannot find your place again, you can always refocus on the currently selected location by hovering the cursor over the Viewer and hitting <span class="keystroke">F</span>.

Feel free to take some time to look at Gaffy from different angles and positions.


## Creating and Setting Up a Camera ##

Before you can render anything, you will need to create a camera to render from. Like how you created a _SceneReader_ node to load in the geometry, you will create another node to generate a camera.

Earlier, you learned how to find a node by navigating the New Node menu in the _Node Graph_ tab (from here on we will refer to it as just the Node Graph). If you know the name of the node you wish to create, and do not feel like navigating the menu, you can use the menu's search:

1. Hover the cursor over the background in the _Node Graph_ tab.

2. Right-click. The New Node menu will open.

    > Tip :
    > With the cursor hovering over the node graph, you can also hit <span class="keystroke">Tab</span> to open the New Node menu.

3. Type `Camera`. A new submenu will appear, showing your search results. By default, _Camera_ will be highlighted.

4. Hit <span class="keystroke">Enter</span> to create a new _Camera_ node.

    ![A new Camera node.](images/camera.png)

As before, the newly created node will be selected automatically, and the Viewer, Scene Hierarchy, and _Node Editor_ tab will update to this new selection.


## Nodes, Scenes, and Plugs ##

So far, your graph is set up as such: The _SceneReader_ node is outputting a scene containing Gaffy's geometry, and the _Camera_ node is outputting a scene containing a camera. However, since neither node is connected, each scene remains separate. This is because each node in Gaffer outputs an entire self-contained scene hierarchy at its position in the graph. If they aren't connected somewhere later in the graph, the two scenes will never interface with each other. A key part to understand about the node graph is that:

> ➡ Each node is a container for the scene it has loaded or that has been provided to it.

You can test this by clicking the background of the node graph, and observing that once the you have no node selected, the Scene Hierarchy goes blank. The scene is not persistent throughout the graph, but is instead carried by the nodes. This will become very relevant when you begin combinging scenes together and selectively modifying parts of a scene.

On the topic of deselecting, accidentally deselecting a node can be confusing, because when no node is selected, each tab in the UI will go blank. This is because:

> ➡ By default, the Viewer, Scene Hierarchy, and _Node Editor_ tab update to reflect the selected node, or go blank when no node is selected.

You can select each node to view its scene in the Viewer, but for them to actually occupy the same scene (and later render together) you will need to combine them into a single scene at some point later in the graph. You can connect them together using a _Group_ node via their **plugs**, and you can also rearrange the nodes to better represent the visual hierarchy.


### Plugs ###

Gaffer allows scenes to be built and modified by creating connections between nodes. For most nodes, the scene flows into it through its input, is then modified by the node, and then flows out through it. A node's inputs and outputs are called **plugs**, and are represented in the Node Graph as colored circles around a node's edges.

<!-- TODO: add close-up of nodes -->


## Selecting, Moving, and Duplicating Nodes ##

You may have already noticed that you can intuitively click and drag the nodes around in the Node Graph.

* To select multiple nodes, click the Node Graph background and drag around multiple 
    * You can also add or remove a node from your selection by holding <span class="keystroke">Shift</span> and clicking the node.
* You can copy and paste nodes using the standard <span class="keystroke">Ctrl</span>-<span class="keystroke">C</span> and <span class="keystroke">Ctrl</span>-<span class="keystroke">V</span> combinations.

You can also pan and zoom around the Node Graph, just like in the Viewer.

* To pan the view, <span class="keystroke">Alt</span>-click and drag.
    * You can also pan by middle-clicking and dragging.
* To zoom in and out, <span class="keystroke">Alt</span>-right-click and drag.
    * You can also zoom by scrolling the middle mouse.


## Connecting Plugs ##

It's time to put all this into practice, and connect the _SceneReader_ and _Camera_ nodes to combine their scenes:

1. Click the background of the Node Graph to deselect all nodes.

2. Create a _Group_ node _(Scene > Hierarchy > Group)_.

3. Arrange the nodes by clicking and dragging them into position.
	* Move the _SceneReader_ node to the left.
	* Move the _Camera_ node to the right.
	* Move the _Group_ node below the other nodes.

4. Click and drag the _SceneReader_ node's _out_ plug (at the bottom; blue) onto the _Group_ node's _in0_ plug (at the top; also blue). As you drag, a node pipe will appear. Once you connect them, a second input plug (_in1_) will appear on the _Group_ node, next to the first.

5. Click and drag the _Camera_ node's _out_ plug onto the _Group_ node's _in1_ plug.

    ![A new Group node.](images/group.png)

The _Group_ node is now generating a new scene combining the input scenes from the node above it under a new parent location called _group_. You can see this new hierarchy by selecting the _Group_ node and examining the Scene Hierarchy.

Only the combined scene at the _Group_ node has been modified. The upstream nodes' scenes are unaffected. You can verify this by reselecting one of them and checking the Scene Hierarchy.


## Positioning the Camera ##

Next, you should reposition the camera so that it frames Gaffy. To do this, you need to edit values in the _Node Editor_ tab (from here on we will just refer to it as the Node Editor).:

> Note :
> In the previous section, we referred to the inputs and outputs of the nodes as **plugs**, and connected them by dragging and dropping within the Node Graph. But in fact, the _Translate_ and _Rotate_ values you just edited in the _Camera_ node are _also_ plugs: they also provide input to the node, and can also be connected together if needed. The Node Graph and Node Editor each display only a subset of the available plugs for ease of use. This will become more relevant in advanced tutorials, when we cover expressions and scripting.

To adjust the camera:

1. Select the _Camera_ node.

2. In the Node Editor, click the **Transform** tab.

3. Edit the _Translate_ and _Rotate_ fields to set the camera's position:
    * Set _Translate_ to `19` `13` `31`
    * Set _Rotate_ to `0` `30` `0`

    ![The transform fields.](images/cameraTransform.png) <!-- TODO: adjust the window so the Transform fields are fully visible, and reduce the image's height -->

4. Select the _Group_ node in the Node Graph, then hover the mouse over the Viewer, and hit <span class="keystroke">F</span> to see Gaffy and the camera in the same framing.


## Rendering Your First Image ##

Now that you have defined the layout of your scene, you should perform a quick test-render to check that everything is working as expected. To do that, you need to place some render-related nodes to define your script's render settings.

1. Select the _Group_ node in the Node Graph.

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

2. Specify the camera in the Node Editor:
	1. Click the _Camera_ header to expand its section.
	2. Toggle the switch next to the _Camera_ field to enable it.
	3. Type `/group/camera` into the _Camera_ field.

Next, you need to add an image type to render:

1. Select the _Outputs_ node.

2. In the Node Editor, click ![the plus button](images/plus.png) and select  _Interactive > Beauty_ from the drop-down menu.

With all the settings complete, start the interactive renderer:

1. Select the _InteractiveAppleseedRender_ node.

2. In the Node Editor, click the **play button** to start the renderer.

3. Select the _Catalogue_ node.

4. Hover the cursor over the Viewer and hit <span class="keystroke">F</span> to frame the _Catalogue_ node's preview image.

    ![The first render.](images/firstRender.png)

Congratulations! You have successfully rendered your first image. Gaffy is currently lacking shading, lighting, and texturing. We will move on to those soon. First, you should adjust the UI to provide yourself a more optimal workflow.


## Pinning a Tab to a Node ##

As mentioned earlier, the Viewer, Scene Hierarchy, and Node Editor each show their respective outputs of the currently selected node. This is not always convenient, because often you will need to edit one node while viewing the output of another. You can solve this by **pinning** a tab while a node is selected, which keeps that tab focused on that node.

To make switching between vieweing Gaffy's geometry and the render easier, you can modify the UI so you're working with two Viewers. First, start by pinning the last node in the graph that contains the scene:

1. Select the _InteractiveAppleseedRender_ node.

2. Click ![the pin button](images/targetNodesUnlocked.png) at the top-right
  of the top pane. The pin button will highlight (![highlighted pin](images/targetNodesLocked.png)).

The Viewer is now locked to the _InteractiveAppleseedRender_ node's scene (which contains all of the parts from its upstream scenes), and will only show that scene, even if you deselect it or select a different node.

Next, pin the same node to the Scene Hierarchy. This time, use the middle-click shortcut:

1. Middle-click and drag the _InteractiveAppleseedRender_ node from the Node Graph into the
  Scene Hierarchy.
  
As with the Viewer, the Scene Hierarchy will now remain locked to the output of _InteractiveAppleseedRender_, regardless of your selection. Now you are free to select any node for editing in the Node Editor, but you will always be viewing the final results of the last node in the graph.

For the final adjustment to the UI, create another Viewer and pin the _Catalogue_ node to it.

1. At the top-right of the top pane, click ![the layout menu button](images/layoutButton.png). The layout menu will open.

2. Select _Viewer_. A new Viewer tab will open.

3. Middle-click and drag the _Catalogue_ node onto the new Viewer. That Viewer is now pinned to that node.

Now you can switch between the scene's geometry (first Viewer tab) and the rendered image (second Viewer tab). Now it is time to shade Gaffy.


## Adding Shaders and Lighting ##

Right now, all the nodes are tightly packed together, so it will be tricky to add any shaders.

It's time to add shaders and lighting. It will help to think of a graph as being composed of three distinct phases: generating the geometry, applying the lighting and shading, and rendering. Lights act like another component of the scene, so you can combine one with the scene nodes. The shaders, however, are different: in order for the renderer nodes to apply to the geometry and to inherit the shaders, you will need to add them somewhere between the scene-creating nodes and render nodes.

### Making Some Space ###

It will thus be useful to logically organize the node graph, by sectioning off areas to keep nodes responsible for each of the three phases.

Before adding a shader, create some empty space in the centre of the node graph:

1. In the Node Graph, select the lower five nodes by clicking and dragging over them.
2. Drag the nodes down to leave some space in the middle.

    ![The graph with some added space.](images/renderSettingsWithGap.png)

### Adding a Shader ###

Now you have enough space to add some shading nodes:

1. Below and to the left of the _Group_ node, create a _Disney Material_ node *(Appleseed > Shader > Material > As_Disney_Material)*.

2. In the Node Editor, give the shader some reflective surface properties:
	* Set the _Specular_ to `0.6`
	* Set the _Roughness_ to `0.35`
3. With the _Disney Material_ node still selected, create a _ShaderAssignment_ node _(Scene > Attributes > ShaderAssignment)_.

4. Click and drag the _ShaderAssignment_ node onto the pipe connecting the _Group_ and _StandardOptions_ nodes. The _ShaderAssignment_ node will be interjected between them.

    ![The ShaderAssignment and Disney Material nodes.](images/firstShaderAssignment.png)

Note that the input and output plugs on the Disney Material node flow from left to right. This is because in Gaffer:

> ➡ Scenes flow from top to bottom, and shaders flow from left to right.

In your newly shaded graph, the _ShaderAssignment_ node takes the material flowing in from the left and assigns it to Gaffy's geometry flowing in from the top. Now that Gaffy has received a proper material assignment, you will need to light the scene.


### Adding an Environment Light ###

Lights, like scene readers and cameras, are anoter component that need to be combined with the main scene. For simplicity, we recommend that you add a global environment light:

1. Create a _PhysicalSky_ node _(Appleseed > Environment > PhysicalSky)_.

2. Place it next to the _Camera_ node.

3. In the Node Editor, adjust the node's angle and brightness:
	* Set the _Sun Phi Angle_ to `100`
	* Set the _Luminance_ to `2.5`

4. Connect the _PhysicalSky_ node's _out_ plug to the _Group_ node's _in3_ plug.

<!-- ![A new and connected environment light node.](a.png) -->
<!-- TODO: image with environment light connected to the Group node. -->

<!-- NOTE: This will be covered in a later article. Further, this shortens this tutorial. -->

<!-- The quickest way of doing this would be to connect it in to the next available input on the Group node, but this time we'll take a different approach. Often when collaborating with others, you'll receive scenes which already contain the geometry and cameras, and it'll be inconvenient to use a Group node because it introduces a new level into the scene hierarchy. In these cases, we can use a Parent node to insert a new child anywhere in the input scene. -->

<!-- - Deselect the PhysicalSky node
- Create a Parent node (_/Scene/Hierarchy/Parent_)
- _Left-Drag_ it between the Group and ShaderAssignment nodes to insert it.
- Enter `/` in the Parent field in the NodeEditor, so that we'll be parenting the light directly under the scene root.
- Connect the output of the light node into the second (child) input of the Parent node. -->

<!-- ![Parenting Node Graph](images/parentingNodeGraph.png) -->

<!-- We should have successfully inserted the light into the scene hierarchy, without affecting the structure of the rest of the scene. -->

<!-- ![Parenting Scene Hierarchy](images/parentingSceneHierarchy.png) -->

For the light to take effect, you will need to enable environment lighting in the _AppleseedOptions_ node:

1. Select the _AppleseedOptions_ node.

2. In the Node Editor, expand the _Environment_ section

3. Toggle the switch next to the _Environment Light_ field to enable it.

4. Type `/group/light` into the _Environment Light_ field.

The interactive render will now be in the process of updating, and you will be able to see Gaffy with some basic shaders and lighting.

![The first render with shaders and lighting.](images/firstLighting.png)


### Adding Textures ###

As Gaffy is looking a bit bland, we recommend you assign some textures to the shader:

1. Create an _Appleseed Color Texture_ node *(Appleseed > Shaders > Texture2d > As_color_texture)*.

2. In the Node Editor, point the node to the textures:
	1. Type `${GAFFER_ROOT}/resources/gafferBot/textures/base_COL/base_COL_` into the _Filename_ field.
	2. Select `mari` from the _UDIM_ drop-down menu.

3. In the Node Graph, connect the _AppleSeed Color Texture_ node's _ColorOut_ plug to the _Disney Material_ node's _BaseColor_ plug. Gaffy's textures will now mix with the shader, and the render will updated to show the combined results.

    ![Gaffy with textures.](images/textures.png)


### Adding Another Shader ###

With your the textures assigned, the surface of all of Gaffy's geometry looks the same, because the material shader is applying to everything. To fix this, you should create an additional metallic shader and apply it selectively to different parts of the geometry.

Begin by creating another shader:

1. Create a _Disney Material_ node as before *(Appleseed > Shader > Material > As_Disney_Material)*

2. In the Node Editor, give the shader some metallic properties:
	1. Set the _Metallic_ to `0.8`
	2. Set the _Roughness_ to `0.4`

3. Create a _ShaderAssignment_ node as before *(Scene > Attributes > ShaderAssignment)*, and make sure the new material is connected into it.

4. Click and drag the new _ShaderAssignment_ node onto the pipe under the first _ShaderAssignment_ node. The new _ShaderAssignment_ node will come after the fist shader in the graph flow.

    ![A second shader on the node graph.](images/secondShaderAssignment.png)

The viewer will update to show the new shader.

![The second shader, rendered.](images/secondShaderAssignmentRender.png)

You will immediately notice something is wrong: _all_ the geometry is metallic. The new shader has overridden the previous one. This is because:

> ➡ The last _ShaderAssignment_ node applied to geometry in a scene takes precedence over all others.

### Filtering a Shader ###

In order to selectively apply a shader to only certain parts of the scene's geometry, you will need to **filter** the shader assignment, using a filter node that selects parts of a scene by name.:

1. Create a _PathFilter_ node _(Scene > Filters > PathFilter)_.

2. In the Node Editor, click ![the plus button](images/plus.png) next to _Paths_. This will add a new text field.

3. Double-click the text field and type `/group/GAFFERBOT/C_torso_GRP/C_head_GRP/C_head_CPT/L_ear001_REN`. This is the full path to Gaffy's left ear (as taken from the Scene Hierarchy).

4. Connect the _PathFilter_ node's _out_ plug to the filter input on the right hand side of the _ShaderAssignment1_ node's filter plug (yellow; on the right).

    ![The connected _PathFilter_ node.](images/filterConnection.png)

Now when you check the render, you will see that the chrome shader is only applied to Gaffy's left ear.

However, there are many other parts of Gaffy that could use the chrome treatment. You might want to apply the chrome shader to more geometry, but it would be tedious for you to manually enter multiple locations. There are two ways you can do this faster: using text wildcards, and interacting directly with the geometry.


#### Filtering Using Wildcards ####

A wildcard is an asterisk (`*`) used to tell text interpreters, "take any value of any length where there is an asterisk." They are useful if you know part of a path, but don't want to have to look up or type it in its entirety. In the case of the metallic shader and filtering Gaffy's ears, you used `/group/GAFFERBOT/C_torso_GRP/C_head_GRP/C_head_CPT/L_ear001_REN`, which only pointed to the left ear. You could apply the filter to _both_ ears by emending `*_ear*` to the path. Try it:

1. Select the _PathFilter_ node.

2. In the Node Editor, double-click the path field you created earlier, and change it to `/group/GAFFERBOT/C_torso_GRP/C_head_GRP/C_head_CPT/*_ear*`. The `*` automatically matches any sequence of characters, so the filter will now match the left and the right ears.


#### Filtering by Dragging Selections ####

As your final operation on Gaffy, you should add the metallic shader to the rest of the appropriate bits. This time, you can use the visual method:

1. In the Viewer, switch to the tab containing the 3D geometry view.
2. Zoom and pan to Gaffy's face.
3. Click the eyebrows to select them.
4. <span class="keystroke">Shift</span>-click the mouth to add it to the selection.

    ![The face, with selection.](images/faceSelection.png)

5. Click and drag the selection, and hold it over the Node Graph without releasing. The cursor will change to ![the "move objects" icon](images/objects.png) to indicate you are dragging the selection.

6. Drag and hover selection over the _PathFilter_ node. The cursor will change to ![the "replace objects" icon](images/replaceObjects.png).

7. Hold <span class="keystroke">Shift</span>. This will switch your action to "add objects" mode.  The cursor will change to ![the "add objects" icon](images/addObjects.png).

8. Release the selection over the _PathFilter_ node. This will add them as new path fields to the node.

Just as objects can be added by holding <span class="keystroke">Shift</span>, they can be removed by holding <span class="keystroke">Control</span>. With this in mind, you can add and remove objects from the shader assignment as you see fit. Remember to switch the Viewer tabs to check the render output as it updates. After adding Gaffy's hands and bolts to the filter, you should arrive at an image something like this:

![The final render.](images/finalRender.png)


## Recap ##

Congratulations! You've built and rendered your first scene in Gaffer.

You should now have a basic understanding of Gaffer's interface, the concept of a scene and how it flows, how to manipulate the scene, how to interact with and adjust the interface, and how to add geometry, lights, textures, and shaders.

This provide a solid basis for your further learning and exploration. Follow the links below to learn more.

## See Also ##

* [Tutorial: Everything But the Kitchen Sink](../SecondTutorial/SecondTutorial.md)
* [Graph Flow](../../UnderstandingTheNodeGraph/GraphFlow/NodeTypes.md)
* [Node Types](../../UnderstandingTheNodeGraph/GraphFlow/GraphFlow.md)
* [Manipulating the Scene Hierarchy](../../WorkingWithScenes/ManipulatingSceneHierarchy/ManipulatingSceneHierarchy.md)
