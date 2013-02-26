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

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    
