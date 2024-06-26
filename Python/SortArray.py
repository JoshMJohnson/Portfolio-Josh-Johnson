# This Python program sorts unsorted arrays of integers given by
# the program itself, as well as given through text files
# using multiple different sorting algorithms 
#
# Sorting algorithms implemented
# - Bubble
# - Selection
# - Merge
# - Insertion
# - Quick
#
# Created By: Josh Johnson

from os import path # used to get relative path for text files
import random # used for random value generation

# bubble sort algorithm
def bubble_sort(array):
    # if the array is already sorted
    swapped = False

    # traverse through all array elements
    for i in range(len(array) - 1):
        # previous i elements are already in place
        for j in range(0, len(array) - i - 1):
            # swap if the current element is greater than the next element
            if array[j] > array[j + 1]:
                swapped = True
                array[j], array[j + 1] = array[j + 1], array[j]
         
        if not swapped:
            return

# selection sort algorithm
def selection_sort(array):
    array_size = len(array)

    # traverse through all array elements
    for i in range(array_size):
        min_index = i

        # select the minimum element in every iteration
        for j in range(i + 1, array_size):
            if array[j] < array[min_index]:
                min_index = j

         # swapping the elements to sort the array if necessary
        if array[i] != array[min_index]:
            (array[i], array[min_index]) = (array[min_index], array[i])

# merge sort algorithm
def merge_sort(array, left_index, right_index):
    if left_index < right_index:
        middle_index = left_index + (right_index - left_index) // 2 # // results in integer division rather than / being double division
 
        # sort first and second halves of sub arrays
        merge_sort(array, left_index, middle_index)
        merge_sort(array, middle_index + 1, right_index)
        merge(array, left_index, middle_index, right_index)

# merges two subarrays of the array
def merge(array, left_index, middle_index, right_index):
    # get sizes of sub arrays
    subarray1_size = middle_index - left_index + 1
    subarray2_size = right_index - middle_index
 
    # create temp arrays
    temp_array1 = [0] * subarray1_size
    temp_array2 = [0] * subarray2_size
 
    # copy data to temp_array1
    for i in range(subarray1_size):
        temp_array1[i] = array[left_index + i]

    # copy data to temp_array2
    for i in range(subarray2_size):
        temp_array2[i] = array[middle_index + 1 + i]

    i, j, k = 0, 0, left_index # multiple variables on the same line
 
    # merge two sorted sub-arrays into one sorted array
    while i < subarray1_size and j < subarray2_size:
        if temp_array1[i] <= temp_array2[j]:
            array[k] = temp_array1[i]
            i += 1
        else:
            array[k] = temp_array2[j]
            j += 1
            
        k += 1
 
    # copy the remaining elements of temp_array1, if there are any
    while i < subarray1_size:
        array[k] = temp_array1[i]
        i += 1
        k += 1
 
    # copy the remaining elements of temp_array2, if there are any
    while j < subarray2_size:
        array[k] = temp_array2[j]
        j += 1
        k += 1

# insertion sort algorithm
def insertion_sort(array):
    for i in range(1, len(array)): 
        key = array[i]
 
        # move elements of arr[0..i-1], that are greater than key, 
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1

        array[j + 1] = key

# quick sort algorithm
#   - this implementation utilizes pivot as the last element in the array
def quick_sort(array, low, high):
    if low < high:
        pivot_index = partition(array, low, high)
 
        # recursive call on the left and right of pivot
        quick_sort(array, low, pivot_index - 1) 
        quick_sort(array, pivot_index + 1, high) 
 
# finds the partition position
def partition(array, low, high):
    pivot = array[high] # set the right-most element as pivot
    i = low - 1 # pointer for greater element
 
    # traverse through all elements comparing each element with pivot
    for j in range(low, high):
        # if element smaller than pivot is found swap it with the greater element pointed by i
        if array[j] <= pivot:
            i += 1
 
            # swapping element at i with element at j if necessary
            if array[i] != array[j]:
                (array[i], array[j]) = (array[j], array[i])
 
    # swap the pivot element with the greater element specified by i if necessary
    if array[i + 1] != array[high]:
        (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1 # position from where partition is done
 
# generates an array with random integers as elements with given array size
def create_random_array(array_size):
    array = []

    for _ in range(array_size):
        element = random.randint(-100, 100) # random value between range; inclusive
        array.append(element)

    return array

# reads a test file and returns an array of elements gathered by the file separated by a space
def read_test_file_into_array(file_name):
    # reading from file
    base_path = path.dirname(__file__) # get current directory location 
    file_path = path.abspath(path.join(base_path, "..", "Test_Files", file_name)) # relative path to the test file
    file1 = open(file_path, "r") # open access to test file
    data = file1.read() # storing file content
    file1.close() # closing the file access to test file

    # creating array from content gathered from test file
    array = [int(i) for i in data.split(' ')] # create array from elements separated by a space in data variable
    return array
     
# prints the contents of the given integer array to stdout
def print_array(array, array_id, ordered, sorting_algorithm):
    if ordered:
        print("Array with ID %d after the %s Sort algorithm is applied:" % (array_id, sorting_algorithm), end=" ") # end parameter prevents new line
    else:
        print("Array with ID %d before the %s Sort algorithm is applied:" % (array_id, sorting_algorithm), end=" ") # end parameter prevents new line
    
    for i in range(len(array)):
        if i == len(array) - 1:
            print("%d" % array[i])
        else:
            print("%d" % array[i], end=", ")

# main function - controls flow of the program
def main():
    array_id = 0 # array ID tracker
    arrays = [0] * 5 # multiplied by 5 for number of algorithms implemented initialized to 0

    # apply sorting algorithms
    # bubble sort - size and values are given by program
    array_one = [3, 66, 45, 23, 9, 0, 11, 2, 7, 49, 21]
    arrays[array_id] = array_one

    print_array(arrays[array_id], array_id, False, "Bubble")
    bubble_sort(arrays[array_id])
    print_array(arrays[array_id], array_id, True, "Bubble")

    # selection sort - size and values are given by program
    array_id += 1
    arrays[array_id] = [55, 4, 32, 62, -2, 4, 6, 9, 99, 12, -12, -5, 4, 55]

    print_array(arrays[array_id], array_id, False, "Selection")
    selection_sort(arrays[array_id])
    print_array(arrays[array_id], array_id, True, "Selection")

    # merge sort - size and values are given by program
    array_id += 1
    arrays[array_id] = create_random_array(10)

    print_array(arrays[array_id], array_id, False, "Merge")
    merge_sort(arrays[array_id], 0, len(arrays[array_id]) - 1)
    print_array(arrays[array_id], array_id, True, "Merge")

    # insertion sort - array size and values are discovered by reading a file
    array_id += 1
    arrays[array_id] = read_test_file_into_array("random_integers_no_duplicates.txt")

    print_array(arrays[array_id], array_id, False, "Insertion")
    insertion_sort(arrays[array_id])
    print_array(arrays[array_id], array_id, True, "Insertion")

    # quick sort - array size and values are discovered by reading a file
    array_id += 1
    arrays[array_id] = read_test_file_into_array("random_integers_with_duplicates.txt")

    print_array(arrays[array_id], array_id, False, "Quick")
    quick_sort(arrays[array_id], 0, len(arrays[array_id]) - 1)
    print_array(arrays[array_id], array_id, True, "Quick")
    
# begins program by calling the main function
main()