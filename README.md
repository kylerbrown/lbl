lbl
===

A python library for reading/writing and manipulating lbl files.
Lbl files are represented within python as a numpy record array with fields 'name', 'start', and 'stop'.
This format is useful for writing data to the [arf](https://github.com/dmeliza/arf) file format.

Typical usage:
---------------

    import lbl
    lbldata = lbl.read('this/is/a_lbl_file.lbl')        #  returns a rec array
    abcd_intervals = lbl.find_seq(lbldata, 'abcd')  #  returns a list of time intervals

What are lbl files?
--------------------
The lbl standard uses the following format:
* 7 lines of garbage (the header)

After the header, each line represents an entry with space separated elements.
* The first element is a floating point time stamp
* the second element is garbage (the number 121)
* the third element is the label or name.

Label conventions
------------------
Labels can be strings of any length. If a label has both a start and a stop time, 
the start label is an entry with '-0' appended to it, while the stop label has '-1' appended.

Example lbl file
-------------------
    signal feasd
    type 0
    color 121
    font *-fixed-bold-*-*-*-15-*-*-*-*-*-*-*
    separator ;
    nfields 1
    #
       15.445851  121 A
       15.520200  121 a-0
       15.595700  121 a-1
       15.747526  121 a-0
       15.818300  121 a-1
       15.928394  121 a-0
       15.991940  121 a-1
       16.053200  121 b-0
       16.192361  121 b-1
       16.230769  121 c-0
       16.350176  121 c-1
       16.395300  121 d-0
       16.740300  121 d-1
       16.847382  121 V
       17.010093  121 C



Requirements
------------
* numpy

Installation
-------------
    git clone https://github.com/kylerbrown/lbl.git
    cd lbl
    python setup.py install
