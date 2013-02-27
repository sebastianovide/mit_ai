#!/usr/bin/python


class Exercise:

    """
    Cube of a number for exmaple:

    >>> Exercise().cube(3)
    27
    """
    def cube(self,n):
        """
        >>> [Exercise().cube(n) for n in range(6)]
        [0, 1, 8, 27, 64, 125]
        """
        return n**3


    def factorial(self,n):
        """
        >>> [Exercise().factorial(n) for n in range(6) + [13]]
        [1, 1, 2, 6, 24, 120, 6227020800]
        >>> Exercise().factorial(-1)
        Traceback (most recent call last):
        ...
        Exception: factorial: input must not be negative
        """
        if n<0:
            raise Exception, "factorial: input must not be negative"
        result = 1;
        for i in range(n):
            result *= (i+1)
        return result

    def count_pattern(self, pattern, lst):
        """
        >>> Exercise().count_pattern()
        Traceback (most recent call last):
        ...
        TypeError: count_pattern() takes exactly 3 arguments (1 given)
        >>> Exercise().count_pattern(('a'),('a','b'))
        1
        >>> Exercise().count_pattern(('a', 'b'), ('a','b', 'c', 'e', 'b', 'a', 'b', 'f'))
        2
        >>> Exercise().count_pattern(('a','b', 'a'), ('g', 'a', 'b', 'a', 'b', 'a', 'b', 'a'))
        3
        """
        def pattern_in_location(i):
            for j in range(len(pattern)):
                if pattern[j] != lst[j+i]:
                    return False
            return True

        matches = 0
        for i in range(len(lst) - len(pattern) + 1):
            matches += 1 if pattern_in_location(i) else 0
            
        return matches

    def depth(self, exp):
        """
        >>> Exercise().depth('x')
        0
        >>> Exercise().depth(1)
        0
        >>> Exercise().depth(('expt', 'x', 2))
        1
        >>> Exercise().depth(('+', ('expt', 'x', 2), ('expt', 'y', 2)))
        2
        >>> Exercise().depth(('/', ('expt', 'x', 5), ('expt', ('-', ('expt', 'x', 2), 1),('/', 5, 2))))
        4
        """
        if (isinstance (exp, (str, int, float))):
            return 0
        
        return 1 + max(self.depth(x) for x in exp)

    def tree_ref(self, tree, idx):
        """
        >>> tree = (((1, 2), 3), (4, (5, 6)), 7, (8, 9, 10))
        >>> len(tree)
        4
        >>> Exercise().tree_ref(tree,(3,1))
        9
        >>> Exercise().tree_ref(tree,(0,))
        ((1, 2), 3)
        >>> Exercise().tree_ref(tree,(2,))
        7
        
        """
        el = tree[idx[0]]
        if len(idx) == 1:
            return el
        
        return self.tree_ref(el, idx[1:])

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
