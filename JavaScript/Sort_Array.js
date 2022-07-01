/*
 * This JavaScript program sorts an unsorted array of integers given by
 * the program itself, as well as given through text files
 * using multiple different sorting algorithms 
 *
 * Sorting algorithms implemented
 * - Selection Sort
 * - Bubble Sort
 * - TO DO: Insertion Sort
 * - TO DO: Quick Sort
 * - TO DO: Merge Sort
 * 
 * Created By: Josh Johnson
 */

/* running variables */
var array_id = 0;

/* selection sort - size and values are given by program */
var array_one = [2, 5, 6, 1, 4, 8, 7, 9, 3];
array_id++;

print_array(array_one, false, "Selection");
array_selection_sort(array_one);
print_array(array_one, true, "Selection");

/* bubble sort - size and values are given by program */
var array_two = new Array(20);
array_id++;

fill_array(array_two);
print_array(array_two, false, "Bubble");
array_bubble_sort(array_two);
print_array(array_two, true, "Bubble");

/* fills in an initialized array with random values */
function fill_array(arr) {
    let i, random_value;

    for (i = 0; i < arr.length; i++) {
        random_value = Math.floor(Math.random() * 100) + 1; // random integer from 1-100
        arr[i] = random_value;
    }
}

/* performs a selection sort algorithm */
function array_selection_sort(arr) {
    let i, j, min_idx;
  
    for (i = 0; i < arr.length - 1; i++) {
        /* Find the minimum element in unsorted array */
        min_idx = i;
        for (j = i + 1; j < arr.length; j++) {
            if (arr[j] < arr[min_idx]) {
                min_idx = j;
            }
        }

        /* swap the found minimum element with the first element */
        if (min_idx != i) {
            let temp = arr[min_idx];
            arr[min_idx] = arr[i];
            arr[i] = temp;
        }
    }
}

/* performs a bubble sort algorithm */
function array_bubble_sort(arr) {
    let i, j;

    for(i = 0; i < arr.length; i++) {
        for(j = 0; j < (arr.length - i -1); j++) {
            if(arr[j] > arr[j + 1]) {
                var temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
            }
        }
    }
}

/* prints the contents of the given integer array to stdout */
function print_array(arr, ordered, algorithm_type) {
    let i;

    if (ordered) {
        process.stdout.write("Array with ID " + array_id + " after " 
            + algorithm_type + " Sort algorithm applied: ");
    } else {
        process.stdout.write("Array with ID " + array_id + " before " 
            + algorithm_type + " Sort algorithm applied: ");
    }

    for (i = 0; i < arr.length; i++) {
        if (i == (arr.length - 1)) {
            console.log(arr[i]);
            break;
        }

        process.stdout.write(arr[i] + " ");
    }
}