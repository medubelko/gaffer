# Tutorial: Using The OSLCode Node #

Using OSL to build shaders opens up a new world of possibilities for complex and customized looks and shading. Gaffer's built-in OSLCode node enables execution of arbitrary code in OSL. This tutorial will demonstrate how to build a very rudimentary striped shader. This tutorial will cover the folling topics:

- Inputting basic code into the OSLCode node
- Adding input and output parameter plugs to the OSLCode node

Before starting this tutorial, we recommend completing the [Assembling the Gaffer Bot](../../GettingStarted/index.md) and [Introductiont to Scripting](../GettingStarted/index.md) starter tutorials.


## Creating a One-Line Shader ##

First, we will demonstrate how to create a basic shader and apply some parameter plugs to it.

1. Create an OSLCode node and select it. The _Viewer_ and _Node Editor_ will show a shader with empty values.

    ![Default OSLCode node in Viewer](images/viewerShader.png "Default OSLCode node in Viewer")

    ![Default OSLCode node in Node Editor](images/nodeEditorShader.png "Default OSLCode node in Node Editor")

2. In the _Node Editor_, in the _Inputs_ section, click ![the plus icon](images/plus.png "The plus icon") and select _Float_ from the drop-down menu. A Float input plug named _Input1_ will appear.

3. Double-click the _Input1_ label, and rename it to `width`.

4. Set the Width value to `0.025`.

5. In the _Outputs_ section, click ![the plus icon](images/plus.png "The plus icon") and select _Color_ from the drop-down menu. A Color output plug named _Output1_ will appear.

6. Double-click the _Output1_ label, and rename it to `stripes`.

7. Any OSL code can be inputted to generate output from the input parameter plugs. Try typing a simple striped pattern into the _Code_ input field:

    ```
    stripes = aastep( 0, sin( v * M_PI / width ) )
    ```

    ![OSLCode node's parameters and plugs](images/nodeEditorShaderParameters.png "OSLCode node's parameters and plugs")

Since shader previews in the _Viewer_ are interactive, the _Viewer_ will automatically update to show your striped shader.

![The shader ball, with stripes](images/viewerShaderStripes.png "The shader ball, with stripes")

> Tip :
> To reference a plug from the _Inputs_ or _Outputs_ sections in your OSL code, drag and drop its label onto the _Code_ input field. This is key to referring to the Color Spline input, which uses a special syntax.


## Creating a Multi-Line Shader ##

Here we will demonstrate a few additional shader parameter plugs, with some slightly more complex code.

Try adding some color and wobble to your shader:

1. Add a color input parameter plug and rename it to `color1`.

2. Add another color input parameter plug and rename it to `color2`.

3. Click the color swatch (the black rectangle) at the far-right of the plug.
    
    ![The color plugs](images/nodeEditorColorInputs.png "The color plugs")

    For each plug, pick a color of your choosing.

4. Update the code:

    ```
    float vv = v + 0.05 * pnoise( u * 20, 4 );
    float m = aastep( 0, sin( vv * M_PI / width ) );
    stripes = mix( color1, color2, m );
    ```

![The shader ball with stripes and colors](images/viewerShaderStripesColors.png "The shader ball with stripes and colors")


## Recap ##

While this was quick introduction with a very simple shader, you should now be equipped to use the OSLCode node by interactively adding input and output parameter plugs and editing code.


## See Also ##

- [Scripting Nodes](../ScriptingNodes/index.md)
