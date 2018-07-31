# Script Performance #

As with most VFX processes and software, Gaffer scripts – in both senses of your project files and the code that goes into them – are subject to performance considerations. If you're not careful, your graph easily compute excessive recursion or unintendedly impactful processes, and the structure that brought about the drop in performance can be difficult to spot. Developing a basic understanding of how Gaffer evaluates graphs, and the complexity pitfalls users commonly encounter, can help you mitigate performance setbacks.

* [Performance best practices](LaunchingGafferFirstTime/index.md)
* [Using the performance monitor](UsingThePerformanceMonitor/index.md)

<!-- TODO * [Multithreading](Multithreading/index.md) -->
<!-- TODO * [Deferred execution](DeferredExecution/index.md) -->

```eval_rst
.. toctree::
    :hidden:

    PerformanceBestPractices/index.md
    UsingThePerformanceMonitor/index.md
..
    Multithreading/index.md
..
    DeferredExecution/index.md
```