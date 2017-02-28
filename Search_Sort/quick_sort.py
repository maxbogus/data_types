"""Implement quick sort in Python.
Input a list.
Output a sorted list."""


def quicksort(array):
    quickSortHelper(array, 0, len(array) - 1)


def quickSortHelper(array, first, last):
    if first < last:
        splitpoint = partition(array, first, last)
        quickSortHelper(array, first, splitpoint - 1)
        quickSortHelper(array, splitpoint + 1, last)


def partition(array, first, last):
    pivotvalue = array[first]
    leftmark = first + 1
    rightmark = last

    done = False
    while not done:
        while leftmark <= rightmark and array[leftmark] <= pivotvalue:
            leftmark += 1

        while array[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = array[leftmark]
            array[leftmark] = array[rightmark]
            array[rightmark] = temp

    temp = array[first]
    array[first] = array[rightmark]
    array[rightmark] = temp

    return rightmark


test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print test
