def bubble_sort(items):

    '''Return array of items , sorted in ascending order'''
    ordered_list = items.copy()
    for i in range(len(ordered_list)):
        for j in range(len(ordered_list[::-1]) - 1):
            if ordered_list[j] > ordered_list[j + 1]:
                ordered_list[j] = ordered_list[j+1]
                ordered_list[j+1] = ordered_list[j]


def merge_sort(items):

    '''Return array of items, sorted in ascending order'''
    def merge(A, B):
        new_list = []
        while len(A) > 0 and len(B) > 0:
            if A[0] < B[0]:
                new_list.append(A[0])
                A.pop(0)
            else:
                new_list.append(B[0])
                B.pop(0)

        if len(A) == 0:
            new_list = new_list + B
        if len(B) == 0:
            new_list = new_list + A

        return new_list


    def merge_sort(items):

        len_i = len(items)
        if len_i == 1:
            return items

        mid_point = int(len_i / 2)
        i1 = merge_sort(items[:mid_point])
        i2 = merge_sort(items[mid_point:])

        return merge(i1, i2)

    return merge_sort(items)

def quicksort(items):

    '''Return array of items, sorted in ascending order'''
    len_i = len(items)

    if len_i <= 1:
        return items

    pivot = items[-1]
    small = []
    large = []
    dup = []
    for i in items:
        if i < pivot:
            small.append(i)
        elif i > pivot:
            large.append(i)
        elif i == pivot:
            dup.append(i)

    small = quicksort(small)
    large = quicksort(large)

    return small + dup + large
