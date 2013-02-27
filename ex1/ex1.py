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

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
