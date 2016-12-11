'''tests for the lbl python library'''
from __future__ import unicode_literals, print_function, absolute_import, division
import lbl
import numpy as np
import os.path

def test_writeread(tmpdir):
    fname = os.path.join(tmpdir.dirname, 'temp.lbl')
    times = np.reshape(np.arange(0,20), (-1,2))
    labels = [chr(i) for i in np.arange(10) + 65]
    dtype = [('name', np.unicode_, max([len(x) for x in labels])),
             ('start', float), ('stop', float)]
    rec_array = np.array([(l, sta, sto) for l, (sta, sto) in zip(labels, times)],
                    dtype=dtype)
    lbl.write(fname, rec_array)
    rec_array2 = lbl.read(fname)
    for x, y in zip(rec_array['name'], rec_array2['name']):
        assert x == y, 'label named do not match'
    assert np.all(np.isclose(rec_array['start'], rec_array2['start'])), 'starts do not match'
    assert np.all(np.isclose(rec_array['stop'], rec_array2['stop'])), 'stops do not match'
