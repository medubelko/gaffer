# Tutorial: Querying a Scene #

Gaffer has a simple API for querying the scene at different positions in the node graph. In this tutorial we will demonstrate how to use this API to traverse a scene hierarchy and examine its state. In this tutorial, we will cover the following items:

- Referencing the main `out` plug
- Referencing the `globals` scene plug
- Using the utility methods for querying scene objects:
    - `object()` method
    - `parameters()` method
    - `transform()` method
    - `fullTransform()` method
    - `attributes()` method
    - `childNames()` method

Before continuing, we highly recommend you complete the [Scripting Basics tutorial](../../Tutorials/ScriptingBasics/index.md).

Before you start, load the following script from your resources folder: `gaffer-!GAFFER_VERSION!-linux/resources/tutorials/queryingScene.gfr`. This simple script contains two grouped geometry primitives and a camera.


## Scene Queries ##

Scene nodes output the scene through their primary `out` plug (the _out_ plug at the bottom of the node in the _Graph Editor_). The `out` plug will be your gateway to all scene queries.


### Querying scene options ###

Make your first query by retrieving the scene's global settings. These are the settings added to the scene by each of the various Options nodes:

```python
globals = script["StandardOptions"]["out"]["globals"].getValue()
print type( globals )
print globals
print globals.keys()
print globals["option:render:camera"].value
print globals["option:render:resolution"].value
```

Although the _out_ plug appears as a single plug in the _Graph Editor_, it is actually a [compound plug](../CompoundPlugs/index.md) with several child plugs, each plug representing a setting added by an Option node. Using the `getValue()` method on the _out_ plug's `globals` child plug returns an IECore.CompoundObject() class containing a dictionary (note the curly braces):

![The output of the CompoundObject](images/scriptOutputCompoundObject.png "The output of the CompoundObject")

> Note :
> To retrieve the value of dictionary keys inside a plug, use the `value` method.


### Querying an object ###

The `"option:render:camera"` key indicates that the script renders through a camera at the `"/world/camera"` scene location, so, try to retrieve the object representing the camera. While the global settings within the scene are contained in the `globals` plug, objects cannot easily be referenced using the `objects` plug without specifying the [scene context](../SceneContext/index.md). The simple workaround is the `object()` method, which takes a scene location:

```python
camera = script["StandardOptions"]["out"].object( "/world/camera" )
print camera
```

<!-- TODO: screenshot of result -->


### Querying an object's parameters ###

The camera's parameters are also like a dictionary, so querying them is equally simple. Try the following:

```
print camera.parameters().keys()
print camera.parameters()["projection"].value
print camera.parameters()["projection:fov"].value
print camera.parameters()["clippingPlanes"].value
```

<!-- TODO: screenshot of result -->


### Querying an object's transform ###

Referencing the camera object and its parameters is a start, but we don't know where it is located spatially. Unsurprisingly, scene transforms (not the same as a node's transform plugs) are represented as another child plug alongside `globals` and `object`, and they can be queried the same way. This time, use the `transform()` method:

```
transform = script["StandardOptions"]["out"].transform( "/world/camera" )
print transform
```

<!-- TODO: screenshot of result -->

That gave us the local scene transform for the camera object in the form of a matrix. we could also use the `fullTransform()` method if we wanted the global scene transform.

You should be able to guess by now that we can get at the sphere's scene object and transform in the same way:

```
sphereObject = script["StandardOptions"]["out"].object( "/world/geometry/sphere" )
sphereTransform = script["StandardOptions"]["out"].transform( "/world/geometry/sphere" )
```

<!-- TODO: screenshot of result -->


### Querying an object's attributes ###

But what about the CustomAttributes node that was applied to the sphere? How can we query what that did? Not surprisingly, the attributes of the sphere are retrieved via an `attributes` plug, or more conveniently an `attributes()` method:

```
a = script["StandardOptions"]["out"].attributes( "/world/geometry/sphere" )
print a.keys()
print a["myString"].value
```

If the sphere had a shader assigned to it, that would appear as `a["shader"]`, but we've deliberately left that out for now to keep this tutorial renderer agnostic.


## Traversing the Hierarchy ##

One of the key features of the above queries was that they were random access. We provided prior knowledge of the hierarchy to decide what to query, enabling you to query scene locations without needing to first query their parent locations. In a real situation, you might not have this knowledge – and your code will not even know that a location like `"/world/geometry/sphere"` exists. We need a means of querying the scene hierarchy first, so that we can then query the contents at each location. Scene structure is communicated with another plug alongside the others - this time one called `childNames`. Fortunately, there is the `childNames()` utility method to return a scene path given a context.

Start at the root of the hierarchy:

```
print script["StandardOptions"]["out"].childNames( "/" )
print script["StandardOptions"]["out"].childNames( "/world" )
```

<!-- TODO: screenshot of result -->

Rather than limiting you to manual exploration, try this simple recursive function that traverses the scene and prints what it finds:

```
import os

def visit( scene, path ) :

	print path
	print "\tTransform : " + str( scene.transform( path ) )
	print "\tObject : " + scene.object( path ).typeName()
	print "\tAttributes : " + " ".join( scene.attributes( path ).keys() )
	print "\tBound : " + str( scene.bound( path ) ) + "\n"
	for childName in scene.childNames( path ) :
		visit( scene, os.path.join( path, str( childName )  ) )

visit( script["StandardOptions"]["out"], "/" )
```

## Recap ##

That is essentially all there is to querying a scene. There's a little more to learn in terms of the APIs for the particular Cortex objects that might be returned by a query, but the above examples hopefully provide a good starting point for exploration.


## See Also ##

- [Using the Script Editor](../ScriptEditor/index.md)
- [Script Files](../ScriptFiles/index.md)
