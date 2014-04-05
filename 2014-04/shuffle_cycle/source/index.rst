=================
 shuffle_cycle()
=================

| Doug Hellmann
| PyATL
| 10 April 2014

Combine shuffle() and cycle()
=============================

random.shuffle()
  Rearrange order of elements in a list randomly.
itertools.cycle()
  Iterate over the elements in a sequence infinitely.
shuffle_cycle()
  Iterate over the elements in a sequence, in random order, infinitely.

Python 2
========

.. literalinclude:: shuffle_cycle.py

Python 2 Output
===============

::

    $ python source/shuffle_cycle.py
    a
    c
    b
    c
    b
    a
    b
    c
    a
    b

Python 3
========

.. literalinclude:: shuffle_cycle3.py
   :language: python3
