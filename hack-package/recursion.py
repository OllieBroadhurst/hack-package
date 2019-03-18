def sum_array(array):

    '''Return sum of all items in array'''
    array = array.flatten()
    n = len(array)
    if len(array) > 1:
        array[0] += array[n-1]
        return sum_array(array[0:n-1])
    else:
        return array[0]


def fibonacci(n):

    '''Return nth term in fibonacci sequence'''
    if n <= 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)


def factorial(n):

    '''Return n!'''
    if n <= 1:
        return n
    else:
        return n * factorial(n-1)


def reverse(word):

    '''Return word in reverse'''
    n = len(word)
    if n == 1:
        return word
    else:
        return reverse(word[-1]) + reverse(word[:-1])
        n -= 1
