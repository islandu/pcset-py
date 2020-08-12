# pcset-py
Python class that implements common features of pitch-class sets.

See [Set theory (music)](https://en.wikipedia.org/wiki/Set_theory_(music) for a primer on pitch-class set theory.

## Properties
* `normal_order` provides a list of the pitch classes in normal order
* `prime_form` provides a list representing the pitch-class set's prime form
* `interval_class_vector` provides a list representing the pitch-class set's interval-class vector

## Methods
* `add_pc()` adds a pitch class to the set
* `remove_pc()` removes a pitch class from the set
* `t_n()` transposes the set by a given pitch-class interval
* `i_n()` inverts the set about a given index number
* `issubset()` returns True if PCSet object is a subset of the passed PCSet argument
* `issuperset()` returns True if PCSet object is a superset of the passed PCSet argument
* `difference()` returns a new PCSet object representing the difference of two PCSet objects
* `intersection()` returns a new PCSet object representing the intersection of two PCSet objects
* `union()` returns a new PCSet object representing the union of two PCSet objects

## Test program

```python
# Test program

if __name__ == '__main__':
    pcset_a, pcset_b = PCSet(10, 4, 9, 6), PCSet(4, 1, 8, 2)
    print('Console representations of 2 test PCSet objects:')
    print(pcset_a, pcset_b, sep='\n')
    print('Prime forms of 2 test PCSet objects:')
    print(pcset_a.prime_form, pcset_b.prime_form, sep='\n')
    print('Interval-class vectors of 2 test PCSet objects:')
    print(
        pcset_a.interval_class_vector,
        pcset_b.interval_class_vector,
        sep='\n'
    )
    print('Union of 2 test PCSet objects:')
    print(pcset_a.union(pcset_b))
    print('Difference of 2 test PCSet objects:')
    print(pcset_a.difference(pcset_b))
    print('Intersection of 2 test PCSet objects:')
    print(pcset_a.intersection(pcset_b))
```

Output of test program:

```
Console representations of 2 test PCSet objects:
PCSet: {4, 6, 9, 10}
PCSet: {1, 2, 4, 8}
Prime forms of 2 test PCSet objects:
[0, 1, 4, 6]
[0, 1, 3, 7]
Interval-class vectors of 2 test PCSet objects:
[1, 1, 1, 1, 1, 1]
[1, 1, 1, 1, 1, 1]
Union of 2 test PCSet objects:
PCSet: {1, 2, 4, 6, 8, 9, 10}
Difference of 2 test PCSet objects:
PCSet: {6, 9, 10}
Intersection of 2 test PCSet objects:
PCSet: {4}
```
