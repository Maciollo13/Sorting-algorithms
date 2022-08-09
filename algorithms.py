from time import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time()
        func(*args, **kwargs)
        stop = time()
        print(f"Sorting took {(stop-start):.50f} seconds.")
    return wrapper



def selection_sort(lst):
    size = len(lst)
    for i in range(size):
        min_idx = i
        for j in range(i + 1, size):
            if lst[j] < lst[min_idx]:
                min_idx = i
            lst[min_idx], lst[i] = lst[i], lst[min_idx]
    return lst


def shell_sort(lst):
    size = len(lst)
    mid = size // 2
    while mid > 0:
        for i in range(mid, size):
            temp = lst[i]
            j = i
            while j >= mid and lst[mid - 1] > temp:
                lst[j] = lst[j - mid]
                j -= mid
            lst[i] = temp
        mid = mid // 2
    return lst





def bubble_sort(lst):
    size = len(lst)
    for i in range(size):
        for j in range(0, size - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def insertion_sort(lst):
    size = len(lst)
    for i in range(1, size):
        nxt_elem = lst[i]
        j = i-1
        while j > 0 and lst[j] > nxt_elem:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = nxt_elem
    return lst


def merge_sort(lst):
    size = len(lst)
    if size <= 1:
        return lst
    mid = size // 2
    left_side = lst[:mid]
    right_side = lst[mid:]

    left_side = merge_sort(left_side)
    right_side = merge_sort(right_side)

    return list(merge(left_side, right_side))


def merge(left, right):
    res = []
    while len(left) > 0 and len(right):
        if left[0] < right[0]:
            res.append(left[0])
            left.remove(left[0])
        else:
            res.append(right[0])
            right.remove(right[0])

    if len(left) == 0:
        res += right
    else:
        res += left
    return res

def partition(lst):
    last = len(lst)-1
    first = 0
    pivot, pointer = lst[last], 1
    for i in range(first, last):
        if lst[i] <= pivot:
            lst[i], lst[pointer] = lst[pointer], lst[i]
            pointer += 1
    lst[pointer], lst[last] = lst[last], lst[pointer]
    return pointer

def quick_sort(l, r, lst):
    if len(lst) == 1:
        return lst
    if l > r:
        ptr = partition(lst)
        quick_sort(l, ptr-1, lst)
        quick_sort(ptr+1, r, lst)
    return lst


def counting_sort(lst):
    size = len(lst)
    output = [0] * size
    count = [0] * (max(lst) + 1)
    for i in lst:
        count[i] += 1
    for i in range(1, max(lst) + 1):
        count[i] += count[i-1]

    i = size - 1
    while i >= 0:
        current_elem = lst[i]
        count[current_elem] -= 1
        new_position = count[current_elem]
        output[new_position] = current_elem
        i -= 1

    return count

arr = [2, 80, 9, 25, 14, 6, 79, 1, 2]
print(bubble_sort(arr))
print(selection_sort(arr))
print(insertion_sort(arr))
print(merge_sort(arr))
print(shell_sort(arr))
print(quick_sort(0, len(arr)-1, arr))
print(counting_sort([2, 2, 0, 6, 1, 9, 9, 7]))