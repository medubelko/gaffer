# Common Operations #


## Node Operations ##


### Create a node ###

```
import GafferScene
node = GafferScene.Sphere()
script.addChild( node )
```


### Delete a node ###

```
script.removeChild( node )
```


### Rename a node ###

```
node.setName( "newName" )
```


## Plug Operations ##


### Get a plug's value ###

```
value = node["plugName"].getValue()
```


### Set a plug's value ###

```
node["plugName"].setValue( value )
```


### Create a connection ###

```
destinationNode["inputPlugName"].setInput( sourceNode["outputPlugName"] )
```


### Delete a connection ###

```
node["inputPlugName"].setInput( None )
```


## Script Operations ##

These operations apply to the `script` variable, which is the project-level context, and root, of every Gaffer script.


### Get a node by name ###

```
node = script["nodeName"]
```


### Loop over all nodes ###

```
for node in script.children( Gaffer.Node ) :
    # Loop-scope code goes here
```


### Write script to file ###

```
script.serialiseToFile( "/path/to/file.gfr" )
```


### Get the file path to the script ###

```
script["fileName"].getValue()
```


### Query a script-level context variable ###

```
script.context()["project:rootDirectory"]
```


### Select a node ###

```
script.selection().clear()
script.selection().add( script["nodeName"] )
```


### Get the frame range ###

```
start = script["frameRange"]["start"].getValue()
end = script["frameRange"]["end"].getValue()
```

### Set the current frame ###

```
script.context().setFrame( frame )
```


## Metadata Operations ##


### Register a value for a plug or node

```
Gaffer.Metadata.registerValue( plug, "name", value )
Gaffer.Metadata.registerValue( node, "name", value )
```


### Query a value for a plug or node

```
Gaffer.Metadata.value( plug, "name" )
Gaffer.Metadata.value( node, "name" )
```


## Scene Operations ##


### Get an option ###

```
g = node["out"]["globals"].getValue()
o = g["option:render:camera"].value
```


### Get an object at a location ###

```
o = node["out"].object( "/path/to/location" )
```


### Get the local transform at a location ###

```
matrix = node["out"].transform( "/path/to/location" )
```


### Get the full (world) transform at a location ###

```
node["out"].fullTransform( "/path/to/location" )
```


### Get the local bounding box of a location ###

```
bound = node["out"].bound( "/path/to/location" )
```


### Get the local attributes of a location ###

```
attributes = node["out"].attributes( "/path/to/location" )
attribute = attributes["name"].value
```


### Get the full (inherited + local) attributes of a location ###

```
attributes = node["out"].fullAttributes( "/path/to/location" )
attribute = attributes["name"].value
```


### Recurse through the scene hierarchy ###

```
def visit( scene, path ) :

	for childName in scene.childNames( path ) :
		visit( scene, os.path.join( path, str( childName )  ) )

visit( node["out"], "/" )
```
