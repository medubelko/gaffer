# Performance Best Practices #

Gaffer is designed to gracefully handle very large scenes by deferring the generation of each location until requested by the user or renderer. It is also designed to be flexible, affording the user a great deal of control in how scenes are generated. These two goals can sometimes be at odds. 

Here we will discuss the performance implications of various choices you might make in your Gaffer scripts, and provide some guidelines for keeping them running smoothly.


## Complexity and Node Graph Structure ##

A very rough estimate for the complexity of a scene can be made by considering the number of its locations, and the number of nodes through which each location passes. For instance, we might say that 10 locations passing through 10 nodes (`10 * 10 = 100`) is roughly equivalent to 20 locations passing through 5 nodes (`20 * 5 = 100`). When you consider that most scenes are comprised of a number of assets, each with an associated shader look, you can use this knowledge to structure your node graphs for the best performance.

Let's consider a scene containing 4 assets, with the geometry cache for each imported into Gaffer through separate _SceneReader_ nodes. Each asset has a LookDev setup from an accompanying _Reference_ node, placed downstream of the _SceneReader_ nodes. This presents us with two options for structuring the node graph. We can either:

* _Graph1:_ Group all the assets together, and then apply the LookDev nodes in series.

![Grouping then applying LookDev](images/groupFirst.png)

* _Graph2:_ First apply the LookDev nodes, and then group all the resulting scenes together.

![Applying LookDev then grouping](images/groupSecond.png)

For the sake of simplicity, let's assume that each asset's scene contains 1000 locations, and each LookDev subgraph contains 100 nodes. Now we can estimate each of the graphs' performance load.

```
graph1 = locations * nodes
       = (locationsPerModel * numberOfAssets) * (nodesPerLook * numberOfAssets)
       = (1000 * 4) * (100 * 4)
       = 4000 * 400
       = 1600000

graph2 = locations * nodes
       = locationsPerModel * numberOfAssets * nodesPerLook
       = 1000 * 4 * 1000
       = 400000
```

This results in a performance difference with a factor of **4**, just from simple graph restructuring. This difference is tied to the number of assets: if the scene had 100 assets, we would be looking at a performance difference with a factor of **100**.

Formally, we can state that grouping second has linear complexity with respect to the number of assets, while grouping first has quadratic complexity. Practically, that means that grouping second is a dramatically better approach, and should be the first consideration when structuring large graphs.

> Tip :
> Apply look development to geometry before combining them into a single scene.

> Tip :
> When possible, group component scenes as late as possible in the node graph.

The guidelines above are not intended to discourage you from editing a large scene. They only apply to the use of published models and LookDev. Much of the flexibility and power Gaffer provides comes from the ability to edit a large scene after a scene is built; this is invaluable when making edits on a per-shot or per-sequence basis. 


## Path Wildcards ##

The `'...'` wildcard in node path expressions means "match any number of names." So, in a large geographical scene, `'/world/.../house'` would return:

* `'/world/village/house'`
* `'/world/country/state/metropolis/neighbourhood/street/house'`

This can be very useful, but it comes at a price. Certain operations in Gaffer require the scene hierarchy to be searched for all matches below a particular location. The wildcard `'...'` tells the expression to go deeper, searching at every level of the hierarchy for any child (or a child of a child of a child) that matches. For large scenes, this becomes very expensive.

> Tip :
> Limit the use of `'...'` in path expressions.

The most expensive expression possible is `'/.../something'`, because it instructs Gaffer to "search _every_ location of the whole scene." While this can be necessary at times, it is likely that a more precise wildcard search will provide the same results, with better performance. 

For instance, if you know that all the matches are within a single asset, an expression such as `/AssetA/.../something` will limit the search to that asset only. Alternatively, if you know that all the matches are at a specific depth, expressions such as `/*/something` or `/*/*/something` would yield the same result without needing to visit deeper locations. Small changes such as this can have a significant impact on scene performance, so it is always worth your time to make expressions as precise as possible.

> Note :
> The `'...'` wildcard isn't _always_ costly. For simple nodes such as _ShaderAssignment_ and _Attributes_, the performance difference is negligible. This is because those nodes can operate on a single location in isolation, and never need to consider the big picture of the scene as a whole. Generally, only hierarchy-altering nodes such as _Prune_ and _Isolate_ are particularly performance sensitive to the `'...'` wildcard. In general, it is best to maintain a wariness surrounding `'...'`, and to make path expressions as precise as possible – at the very least, it will help make your intentions clear to anyone who might inherit your scripts.


## Expressions ##

Python is an excellent language, but it is not the quickest, with its limited multithreading support. In contrast, OSL is reasonably quick, and multithreads well. In situations where an expression will be evaluated frequently (such as once per scene location), the equivalent OSL expression can give significantly improved performance over Python. For instance, tests using a per-instance expression of 100,000 instances yielded a 2× speedup in total scene generation time when using one thread, and a 16× speedup when using 12 threads.

> Tip :
> In expressions where performance is a concern, use OSL instead of Python.

However, Python should not be entirely avoided. It can access databases, the filesystem, and the  Gaffer and Cortex modules, providing far more flexibility than OSL. Typically, if a Python expression does not access `context["scene:path"]` or another frequently changing variable, Gaffer's caching mechanisms will ensure that the expression will be run only once, keeping everything running as smoothly as possible.


## Instancing ##

The _Instancer_ node is capable of generating a very high number of locations, so it too can have a significant performance impact. Because it also supports per-instance variation through the use of expressions on its upstream instance graph, it must evaluate the entire instance graph for every given instance.

Using the rough complexity metric of `complexity = numberOfLocations * numberOfNodes` from earlier, keep in mind these guidelines for the _Instancer_ node:

> Tip :
> - Use the _Instancer_ node carefully and with moderation.
> - Use a minimum of nodes to generate the input for the upstream instance graph that connects to the _instance_ input plug. If necessary, consider baking the instance graph to a cache and loading it in with a _SceneReader_ node.
> - Use a minimum of nodes below the _Instancer_ node to modify the scene containing all the resulting instances.
> - Group or parent the instances into the main scene as late as possible in the node graph.
> - Try and assign shaders and set attributes at a location in the scene hierarchy above all the instances, rather than on a per-instance basis.


## Performance Monitor ##

Gaffer has a [performance monitor](../UsingThePerformanceMonitor/index.md) and a [stats app](../../References/CommandLineReference/stats.md) that can be used to measure and compare the real performance of your graph.

> Tip :
> When performance is critical, use the performance monitor or the stats app.


## See Also ##

<!-- TODO - [Multithreading](Multithreading/index.md) -->
<!-- TODO - [Deferred execution](DeferredExecution/index.md) -->

- [Using the performance monitor](../UsingThePerformanceMonitor/index.md)
