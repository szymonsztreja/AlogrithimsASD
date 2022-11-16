import random

import numpy as np
import time
import sys
import math

sys.setrecursionlimit(100001)

# randNumbers = np.random.randint(1, 101, 100000)
# insertionSortNumbers = random_list.copy()
random_list = []
for i in range(100000):
    random_list.append(random.randint(1000, 1000000))
heapsortNumber = random_list.copy()
mergeArray = random_list.copy()


def quick_sort_time_execution(array):
    start = time.time()
    quick_sort(array, 0, len(array) - 1)
    end = time.time()
    print(end - start)
    return array


def quick_sort(array, p, r):
    if (p < r):
        j = partition(array, p, r)
        quick_sort(array, p, j - 1)
        quick_sort(array, j + 1, r)


def partition(array, p, r):
    pivot = array[r]
    smaller = p
    for j in range(p, r):
        if array[j] <= pivot:
            array[smaller], array[j] = array[j], array[smaller]
            smaller = smaller + 1
    array[smaller], array[r] = array[r], array[smaller]
    return smaller


def max_heapify(array, i):
    l = 2 * i
    r = 2 * i + 1

    if l <= len(array) and array[l] > array[i]:
        largest = l
    else:
        largest = i

    if r <= len(array) and array[r] > array[largest]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]

        max_heapify(array, largest)


def max_heap_sort(array):
    start = time.time()
    heapsize = math.floor(len(array) / 2) - 1
    for i in range(heapsize):
        max_heapify(heapsortNumber, i)

    # for i in range( len(array) - 1):
    #     array[i], array[0] = array[0], array[i]
    #     max_heapify(array, i)

    end = time.time()
    print(end - start)


def insertion_sort(array):
    start = time.time()
    for x in range(1, len(array)):
        currentValue = array[x]

        j = x - 1
        while j >= 0 and array[j] > currentValue:
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = currentValue
    end = time.time()
    print(end - start)


def merge(merge_array, left_half, right_half):
    left_size = len(left_half)
    right_size = len(right_half)

    i = j = k = 0

    while i < left_size and j < right_size:
        if left_half[i] <= right_half[j]:
            merge_array[k] = left_half[i]
            i += 1
        else:
            merge_array[k] = right_half[j]
            j += 1
        k += 1

    while i < left_size:
        merge_array[k] = left_half[i]
        i += 1
        k += 1

    while j < right_size:
        merge_array[k] = right_half[j]
        j += 1
        k += 1


def merge_sort(merge_array):
    array_length = len(merge_array)

    if array_length < 2:
        return

    mid_index = array_length // 2
    left_half = merge_array[:mid_index]
    right_half = merge_array[mid_index:]
    # left_half = [mid_index]
    # right_half = [array_length - mid_index]

    # for x in range(mid_index):
    #     left_half[x] = merge_array[x]
    #     print(left_half[x])
    #     print(x)
    #
    # for p in range(mid_index, array_length):
    #     right_half[p - mid_index] = merge_array[p]

    merge_sort(left_half)
    merge_sort(right_half)

    merge(merge_array, left_half, right_half)


def merge_sort_time(merge_array):
    start = time.time()
    merge_sort(merge_array)
    end = time.time()
    print(end)


# print(randNumbers)
print("Unsorted quicksort: ")
sortedArray = quick_sort_time_execution(random_list)
# print(sortedArray)
print("Sorted quicksort: ")
# quick_sort_time_execution(sortedArray)
# print(randNumbers)
print("Descending order quicksort")

# descendingQS = random_list.sort(reverse=True)
# print(descendingQS)
# quick_sort_time_execution(descendingQS)
# print(descendingQS)
print("XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
print("MERGESORT:")
merge_sort_time(mergeArray)
print("SORTED MERGESORT:")
merge_sort_time(mergeArray)
descendingMS = sorted(random_list, reverse=True)
print("DESCDENDING MERGESORT:")
merge_sort_time(descendingMS)











# print("Unsorted array")
# # print(insertionSortNumbers)
# print("Unsorted insertionsort: ")
# insertion_sort(insertionSortNumbers)
# # print(insertionSortNumbers)
# print("Sorted insertionsort: ")
# insertion_sort(insertionSortNumbers)
# # print(insertionSortNumbers)
# descendingIS = np.sort(insertionSortNumbers)[::-1]
# # print(descendingIS)
# insertion_sort(descendingIS)
# # print(descendingIS)
