lbl
===

A python library for reading/writing and manipulating lbl files

what are lbl files?
--------------------
The lbl standard using the following format:
* 7 lines of garbage (the header)

After the header, each line represents an entry with space sepparated elements.
* The first element is a floating point time stamp
* the second element is garbage (the number 121)
* the third element is the label or name.

label conventions
------------------

requirements
------------
*python 2.x
*numpy
