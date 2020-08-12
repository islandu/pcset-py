"""
pcset.py
PCSet (pitch-class set) class definition
"""

from __future__ import annotations
from itertools import combinations
from typing import List, NoReturn


class PCSet:
    """Defines a pitch-class set object"""

    # Magic methods

    def __init__(self, *pcs: int):
        """Constructs a PCSet instance from the given integers"""
        self._pcs = {PCSet._check_n(pc) for pc in pcs}

    def __iter__(self):
        """Enables direct iteration over contents of PCSet object"""
        for pc in self._pcs:
            yield pc

    def __len__(self):
        """Returns the cardinality of the PCSet object"""
        return len(self._pcs)

    def __repr__(self):
        """Console representation of the PCSet object (same as __str__)"""
        return str(self)

    def __str__(self):
        """String cast of PCSet object (class name and normal order)"""
        return 'PCSet: {}{}{}'.format(
            '{', ', '.join(str(pc) for pc in self.normal_order), '}'
        )

    # Const methods (properties)

    @property
    def normal_order(self) -> List[int]:
        """Returns a list of the pitch-class integers in normal order"""
        sorted_pcs = sorted(self._pcs)

        scores = [
            sum(1 << ((pc_b - pc_a) % 12) for pc_b in sorted_pcs)
            for pc_a in sorted_pcs
        ]

        min_index = scores.index(min(scores))
        return PCSet._rotate_list(sorted_pcs, min_index)

    @property
    def prime_form(self) -> List[int]:
        """Returns a list representing the PCSet object's prime form"""
        transpositions = [
            sorted((pc_b - pc_a) % 12 for pc_b in self._pcs)
            for pc_a in self._pcs
        ]

        inverted_pcs = {-pc % 12 for pc in self._pcs}

        inversions = [
            sorted((pc_b - pc_a) % 12 for pc_b in inverted_pcs)
            for pc_a in inverted_pcs
        ]

        t_scores = [sum(1 << pc for pc in lst) for lst in transpositions]
        i_scores = [sum(1 << pc for pc in lst) for lst in inversions]
        min_t, min_i = (min(lst) for lst in (t_scores, i_scores))

        if min_t <= min_i:
            return transpositions[t_scores.index(min_t)]
        else:
            return inversions[i_scores.index(min_i)]

    @property
    def interval_class_vector(self) -> List[int]:
        """
        Returns a list representing the PCSet object's interval-class vector
        """

        result = [0] * 6

        for pc_a, pc_b in combinations(self._pcs, 2):
            pc_ivl = (pc_b - pc_a) % 12

            if pc_ivl > 6:
                pc_ivl = -pc_ivl % 12

            result[pc_ivl - 1] += 1

        return result

    # Non-const methods

    def add_pc(self, pc: int) -> NoReturn:
        """Adds the given integer to the PCSet object"""
        self._pcs.add(PCSet._check_n(pc))

    def remove_pc(self, pc: int) -> NoReturn:
        """Removes the given integer from the PCSet object (if present)"""
        try:
            self._pcs.remove(pc)
        except KeyError:
            pass

    def t_n(self, n: int) -> NoReturn:
        """Transposes the PCSet object by the given pitch-class interval"""
        PCSet._check_n(n)
        self._pcs = {(pc + n) % 12 for pc in self._pcs}

    def i_n(self, n: int) -> NoReturn:
        """Inverts the PCSet object about the given index number"""
        PCSet._check_n(n)
        self._pcs = {(n - pc) % 12 for pc in self._pcs}

    # Set methods

    def issubset(self, other: PCSet) -> bool:
        """Returns True if self is a subset of the given PCSet object"""
        return self._pcs.issubset(other._pcs)

    def issuperset(self, other: PCSet) -> bool:
        """Returns True if self is a superset of the given PCSet object"""
        return self._pcs.issuperset(other._pcs)

    def difference(self, other: PCSet) -> PCSet:
        """Returns the difference of self and the given PCSet object"""
        result = PCSet()
        result._pcs = self._pcs.difference(other._pcs)
        return result

    def intersection(self, other: PCSet) -> PCSet:
        """Returns the intersection of self and the given PCSet object"""
        result = PCSet()
        result._pcs = self._pcs.intersection(other._pcs)
        return result

    def union(self, other: PCSet) -> PCSet:
        """Returns the union of self and the given PCSet object"""
        result = PCSet()
        result._pcs = self._pcs.union(other._pcs)
        return result

    # Helper functions (private static methods)

    @staticmethod
    def _check_n(n: int) -> int:
        """
        Validates integer as pitch-class, interval, or index number (0-11)
        """

        if 0 <= n <= 11:
            return n
        else:
            raise ValueError(
                "pitch class, interval, or index number must be 0-11"
            )

    @staticmethod
    def _rotate_list(input_list: list, front_index: int) -> list:
        """Rotates list to begin at the given index"""
        return input_list[front_index:] + input_list[:front_index]


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
