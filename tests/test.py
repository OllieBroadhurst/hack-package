import numpy as np
from hackpackage import recursion, sorting

def test_functions():

    assert recursion.sum_array(np.array([[1,2,3], [4,5,6], [7,8,9]])) == 45
    assert recursion.fibonacci(7) == 13
    assert recursion.factorial(7) == 5040
    assert recursion.reverse('Hello') == 'olleH'

    test_list [5,8,1,2,9,9,4]

    assert sorting.bubble_sort(test_list) == [1, 2, 4, 5, 8, 9, 9]
    assert sorting.merge_sort(test_list) == [1, 2, 4, 5, 8, 9, 9]
    assert sorting.quicksort(test_list) == [1, 2, 4, 5, 8, 9, 9]

print(test_functions())
