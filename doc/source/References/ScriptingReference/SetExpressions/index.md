# Set Expressions #

Set expressions are convenient methods for taking sets and locations and building a new set from them.

For this reference, we will assume a scene with these objects…

* A
* B
* C
* D
* E

… in these sets:

* **set1:** A B C
* **set2:** B C D
* **set3:** C D E
* **set4:** E


## Operators and Punctuators ##

The following operators and punctuators are supported:

```eval_rst
======================= ======================================
Operator                Behaviour
======================= ======================================
:code:`|`               Union: joins two sets
:code:`&`               Intersection: intersects two sets
:code:`-`               Difference: removes elements from sets
:code:`()`              Parentheses: contents inside parentheses 
                        have their operations performed first
======================= ======================================
```

> Note :
> A blank space between two sets is interpreted by default as a union. Think of it as Gaffer inserting a `|` for you.


### Examples ###

```eval_rst
============================= ==============================
Set Expression                Resulting set                 
============================= ==============================
:code:`set1`                  A B C
:code:`set1 | set2`           A B C D
:code:`set1 set2`             A B C D
:code:`set1 set2 set4`        A B C D E
:code:`set1 & set2`           B C
:code:`set1 - set2`           A
:code:`(set1 | set2) & set3`  C D     
============================= ==============================
```


## Referencing Objects ##

You can directly reference individual objects. An object in a set expression will be interpreted as a set with itself as the only member.


### Examples ###

```eval_rst
======================= ==============================
Set Expression          Resulting set                 
======================= ==============================
:code:`set1 | D`        A B C D
:code:`set1 - C`        A B
:code:`set1 | (D E)`    A B C D E
:code:`set1 & (A B D)`  A B
:code:`set1 - (B C)`    A
======================= ==============================
```


## Operator Precedence ##

Operations in a set expression will execute in the following order: 

1. Difference
2. Intersection
3. Union


### Examples ###

```eval_rst
============================= ==============================
Set Expression                Resulting set                 
============================= ==============================
:code:`set1 | set3 & set4`    A B C E
:code:`set1 - set2 | set4`    A E
:code:`set1 - set3 & set2`    B
============================= ==============================
```

Parenthesis can be used to explicitly change the order of evaluation:

```eval_rst
============================== ==============================
Set Expression                 Resulting set                 
============================== ==============================
:code:`(set1 | set3) & set4`   E
:code:`set1 - (set2 | set4)`   A
:code:`set1 - (set3 & set2)`   A B
============================== ==============================
```
