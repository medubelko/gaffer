# Scene Context #

<!-- TODO: fix this whole mess -->

In a previous tutorial, we queried a scene using the 

Just as the globals within the scene were represented by a `globals` plug, the objects are represented by an `object` plug. Maybe we can get the camera out using a simple `getValue()` call as before?

```python
globals = script["StandardOptions"]["out"]["object"].getValue()
```

<!-- TODO: screenshot this error: `RuntimeError : line 1 : Exception : Context has no entry named "scene:path"` using a script editor popout window OR a script editor in the top panel -->

That did not work. The problem is that whereas the `globals` are _global_, different objects are potentially available at each point in the scene hierarchy - we need to say which part of the hierarchy we want the object from. Try the following:

```python
with Gaffer.Context( script.context() ) as context :
	context["scene:path"] = IECore.InternedStringVectorData( [ 'world', 'camera' ] )
	camera = script["StandardOptions"]["out"]["object"].getValue()
	print camera
```

The Context class is central to how Gaffer works: a plug can output entirely different values depending on the context in which `getValue()` is called. Here we provided a context as a path within the scene, but for an image node we'd provide a context with a tile location and channel name. Contexts allow Gaffer to multithread efficiently - each thread uses its own Context class so each thread can be querying a different part of the scene or a different location in an image. That was a bit wordy though wasn't it? For now let's pretend we didn't even take this detour and let's use a utility method that does the same thing instead:
