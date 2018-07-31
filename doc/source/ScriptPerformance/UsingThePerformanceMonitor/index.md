# Using the Performance Monitor #

Gaffer contains a built-in performance monitor, which can help diagnose and optimize a node graph's performance. With the _Performance Monitor_ switch of your script's _StandardOptions_ node toggled, performance statistics will be sent to the standard output (stdout) during dispatched renders.

> Note :
> Performance statistics using the performance monitor cannot be generated for IPR rendering.

To turn on the performance monitor:

1. Create a _StandardOptions_ node.

2. Connect the node after all the scene building and shader application, but prior to the renderer's task node.

3. With the node selected, expand the _Statistics_ section under _Settings_ in the _Node Editor_.

4. Toggle the switch and then check the box next to _Performance Monitor_.

    ![The performance monitor, activated](images/performanceMonitor.png)

When you dispatch your script to the renderer, performance data will output to the stdout in your terminal. If you are dispatching to a render farm, the farm will receive the stdout.

As an alternative, the [stats app](../../References/CommandLineReference/stats.md) allows the same monitoring to be performed from the command line, without the need to dispatch the script.


## See Also ##

- [Script performance](../index.md)
- [Stats app](../../References/CommandLineReference/stats.md)