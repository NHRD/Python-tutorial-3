def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    result =  sum(values) / len(values)
    return result

if __name__ == "__main__":
    import doctest
    doctest.testmod()