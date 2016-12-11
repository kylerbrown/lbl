'''Functions for working with lbl files

lbl files are represented as a numpy rec array with fields:
name (a unicode string), start, stop.
For events with no explicit stop, stop = start.

typical use:
abcd_intervals = find_seq(read(this/is/a_lbl_file.lbl), 'abcd')
'''
from __future__ import unicode_literals, print_function, absolute_import, division
import numpy as np
import re

__version__ = '0.1.1'

def read(fname):
    '''reads in a lbl file named fname to a list'''
    lines = open(fname, 'r').readlines()[7:]
    if len(lines) == 0:
        raise ValueError('This lbl file is empty')
    stringpairs = [x.split()[::2] for x in lines]
    lbl = [(float(x), y) for x, y in stringpairs]
    labels = []
    times = []
    while len(lbl) > 0:
        start, label = lbl.pop(0)
        if len(label) > 2 and '-0' in label:
            labels.append(label[:-2])
            #find and pop end time
            matches = (i for i, (stop, offlabel)
                       in enumerate(lbl)
                       if offlabel == label[:-2] + '-1')
            stopidx = next(matches, None)
            if stopidx is not None:
                stop = lbl.pop(stopidx)[0]
            else:
                stop = start
            times.append([start, stop])
        else:  # no associated offset
            labels.append(label)
            times.append([start, start])
    dtype = [('name', 'U' + str(max([len(x) for x in labels]))),
             ('start', float), ('stop', float)]
    return np.array([(l, sta, sto) for l, (sta, sto) in zip(labels, times)],
                    dtype=dtype)


def find_seq(lbl_rec, sequence):
    '''returns the onset and offset times of substring 'sequence'
    from lbllist'''
    labels = reduce(lambda x, y: x + y, lbl_rec['name'])
    matches = [m.start() for m in re.finditer('(?=%s)' % (sequence), labels)]
    if matches == []: return []
    starts = lbl_rec['start'][matches]
    stops = lbl_rec['stop'][np.array(matches) + len(sequence) - 1]
    return np.column_stack((starts, stops))


def write(fname, lbl_rec):
    ''' Writes lbl_rec to an lbl file named fname'''
    header = '''signal feasd
type 0
color 121
font *-fixed-bold-*-*-*-15-*-*-*-*-*-*-*
separator ;
nfields 1
#
'''
    f = open(fname, 'w')
    f.write(header)
    for label, start, stop in lbl_rec:
        if start == stop:
            f.write('   %.18e  121 %s\n' % (start, label))
        else:
            f.write('   %.18e  121 %s-0\n' % (start, label))
            f.write('   %.18e  121 %s-1\n' % (stop, label))
