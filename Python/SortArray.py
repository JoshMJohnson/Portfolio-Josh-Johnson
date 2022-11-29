# This Python program sorts unsorted arrays of integers given by
# the program itself, as well as given through text files
# using multiple different sorting algorithms 
#
# Sorting algorithms implemented
# - Bubble
# - Selection
# - TODO: Merge
# - TODO: Insertion
# - TODO: Quick
#
# Created By: Josh Johnson

from os import path # used to get relative path for text files

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
 
# prints the contents of the given integer array to stdout
def print_array(array, array_id, ordered, sorting_algorithm):
    if ordered:
        print("Array with ID %d after %s Sort algorithm applied:" % (array_id, sorting_algorithm), end=" ") # end parameter prevents new line
    else:
        print("Array with ID %d before %s Sort algorithm applied:" % (array_id, sorting_algorithm), end=" ") # end parameter prevents new line
    
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

    
# begins program by calling the main function
main()