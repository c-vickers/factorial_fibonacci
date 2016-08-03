# Factorial Functions
# Factorial Iteration
def factorial(num):
    """ Returns the factorial of a given num.
    
        >>> factorial(5)
        120
        
        >>> factorial(7)
        5040
        
        >>> factorial(3)
        6
        
        >>> factorial(11)
        39916800

        >>> factorial(33)
        8683317618811886495518194401280000000L

        >>> factorial(0)
        1

        >>> factorial(1)
        1

    """

    total = 1
    while num >= 2:
        total *= num
        num = num-1
    return total


#Factorial Recursive
def rec_factorial(num):
    """ Returns the factorial of a given num.
    
        >>> rec_factorial(5)
        120
        
        >>> rec_factorial(7)
        5040
        
        >>> rec_factorial(3)
        6
        
        >>> rec_factorial(11)
        39916800

        >>> rec_factorial(33)
        8683317618811886495518194401280000000L

        >>> rec_factorial(0)
        1

        >>> rec_factorial(1)
        1

    """

    if num == 0:
        return 1
    else:
        return num * rec_factorial(num-1)


# Fibonacci Functions
# Fibonacci Iterative
def fibonacci(n):
    """Prints the Fibonacci Series up to n places.

        >>> fibonacci(5)
        [1, 1, 2, 3, 5]

        >>> fibonacci(7)
        [1, 1, 2, 3, 5, 8, 13]

        >>> fibonacci(3)
        [1, 1, 2]

        >>> fibonacci(11)
        [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

        >>> fibonacci(0)
        

        >>> fibonacci(1)
        [1]
    """

    if n > 0:
        sequence = [1,]
        int1, int2 = 1,1
        for i in range(n-1):
            int1, int2 = int2, (int1 + int2)
            sequence.append(int1)
        return sequence


def fibowhile(n):
    """Prints the Fibonacci Series up to n places.

        >>> fibowhile(5)
        [1, 1, 2, 3, 5]

        >>> fibowhile(7)
        [1, 1, 2, 3, 5, 8, 13]

        >>> fibowhile(3)
        [1, 1, 2]

        >>> fibowhile(11)
        [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

        >>> fibowhile(0)
        []

        >>> fibowhile(1)
        [1]
    """

    mylist = []
    int1, int2 = 1,1
    while n > 0:
        mylist.append(int1)
        int1, int2 = int2, (int1 + int2)
        n -= 1
    return mylist

# Fibonacci Recursive
def rec_fibonacci(n, int1=0, int2=1, mylist=[]):
    """Prints the Fibonacci Series up to n places.

        >>> rec_fibonacci(5, mylist=[])
        [1, 1, 2, 3, 5]

        >>> rec_fibonacci(7, mylist=[])
        [1, 1, 2, 3, 5, 8, 13]

        >>> rec_fibonacci(3, mylist=[])
        [1, 1, 2]

        >>> rec_fibonacci(11, mylist=[])
        [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

        >>> rec_fibonacci(0, mylist=[])
        []

        >>> rec_fibonacci(1, mylist=[])
        [1]
    """
    if n == 0:
        return mylist
    else:
        int1, int2 = int2, (int1+int2)
        mylist.append(int1)
        return rec_fibonacci((n-1), int1, int2, mylist)




if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print

