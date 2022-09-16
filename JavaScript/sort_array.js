/*
 * This JavaScript program sorts unsorted arrays of integers given by
 * the program itself, as well as given through text files
 * using multiple different sorting algorithms. 
 * 
 * Must run sorting algorithms that involved a file with nodejs through command line
 *
 * Sorting algorithms implemented
 * - Selection Sort
 * - Bubble Sort
 * - Quick Sort
 * - Insertion Sort
 * - Merge Sort
 * 
 * Created By: Josh Johnson
 */

/* driver code */
/* running variables */
var array_id = 0;
var arrays = new Array(5); // size of array is equal to number of algorithms implemented
var array_size, file_name;

/* selection sort - size and values are given by program */
array_id++;
arrays[array_id - 1] = [2, 5, 6, 1, 4, 8, 7, 9, 3];

print_array(arrays[array_id - 1], false, "Selection");
array_selection_sort(arrays[array_id - 1]);
print_array(arrays[array_id - 1], true, "Selection");

/* bubble sort - size and values are given by program */
array_id++;
array_size = 20;
arrays[array_id - 1] = new Array(array_size);
fill_array_fixed_size(arrays[array_id - 1]);

print_array(arrays[array_id - 1], false, "Bubble");
array_bubble_sort(arrays[array_id - 1]);
print_array(arrays[array_id - 1], true, "Bubble");

/* quick sort - size and values are given by program */
array_id++;
arrays[array_id - 1] = new Array();
array_size = 15;
fill_array_unfixed_size(arrays[array_id - 1], array_size);

print_array(arrays[array_id - 1], false, "Quick");
array_quick_sort(arrays[array_id - 1], 0, arrays[array_id - 1].length - 1);
print_array(arrays[array_id - 1], true, "Quick");

/* insertion sort - array size and values are discovered by reading a file */
array_id++;
arrays[array_id - 1] = new Array();
file_name = "../Test_Files/random_integers_no_duplicates.txt";
read_from_file(arrays[array_id - 1], file_name);

print_array(arrays[array_id - 1], false, "Insertion");
array_insertion_sort(arrays[array_id - 1]);
print_array(arrays[array_id - 1], true, "Insertion");

/* merge sort - array size and values are discovered by reading a file */
array_id++;
arrays[array_id - 1] = new Array();
file_name = "../Test_Files/random_integers_with_duplicates.txt";
read_from_file(arrays[array_id - 1], file_name);

print_array(arrays[array_id - 1], false, "Merge");
array_merge_sort(arrays[array_id - 1], 0, arrays[array_id - 1].length - 1);
print_array(arrays[array_id - 1], true, "Merge");

/* reads from a file and fills array with intergers given in the file */
function read_from_file(arr, file_name) {
    let i, file_data;
    let temp_array = [];
    const fs = require('fs');

    file_data = fs.readFileSync(file_name).toString();
    temp_array = file_data.split(" ");

    /* moves data from local array to global array passed as a parameter */
    for (i = 0; i < temp_array.length; i++) {
        arr.push(parseInt(temp_array[i]));
    }
}

/* fills in an initialized array with random values */
function fill_array_fixed_size(arr) {
    let i, random_value;

    for (i = 0; i < arr.length; i++) {
        random_value = Math.floor(Math.random() * 100) + 1; // random integer from 1-100 inclusive
        arr[i] = random_value;
    }
}

function fill_array_unfixed_size(arr, arr_size) {
    let i, random_value;

    for  (i = 0; i < arr_size; i++) {
        random_value = Math.floor(Math.random() * 50) + 1; // random integer from 1-50 inclusive
        arr.push(random_value);
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

/* performs a quick sort algorithm */
function array_quick_sort(arr, low, high) {
    if (low < high) {
        let index = partition(arr, low, high);

        /* separately sort elements before and after partition */
        array_quick_sort(arr, low, index - 1);
        array_quick_sort(arr, index + 1, high);
    }
}

/* 
 * takes the last element as pivot, places the pivot element at 
 * correct position in sorted array, and places all smaller elements
 * to the left of the pivot and all greater elements to right of pivot 
 */
function partition(arr, low, high) {
    let pivot = arr[high];
    let i = low - 1;

    for (let j = low; j <= high - 1; j++) {
        if (arr[j] < pivot) {
            i++;
            swap(arr, i, j);
        }
    }

    swap(arr, i + 1, high);
    return i + 1;
}

/* swaps two elements within array arr */
function swap(arr, i, j) {
    let temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}

/* performs an insertion sort algorithm */
function array_insertion_sort(arr) {
    let i, j, key; 

    for (i = 1; i < arr.length; i++) { 
        key = arr[i]; 
        j = i - 1; 
   
        while (j >= 0 && arr[j] > key) { 
            arr[j + 1] = arr[j]; 
            j--; 
        } 

        arr[j + 1] = key; 
    } 
}

/* performs a merge sort algorithm */
function array_merge_sort(arr, left_index, right_index) {
    /* recursively calls itself to divide the array until array size becomes one */
    if (left_index < right_index) {
        let middle_index = left_index + parseInt((right_index - left_index) / 2);

        /* sort first and second halves of array */
        array_merge_sort(arr, left_index, middle_index);
        array_merge_sort(arr, middle_index + 1, right_index);

        /* merge the sorted sub-arrays */
        merge(arr, left_index, middle_index, right_index);
    }
}

/* takes an array, splits it in half, and merges into one sorted array */
function merge(arr, left_index, middle_index, right_index) {
    let i, j, k;    
    let sub_arr_one_size = middle_index - left_index + 1;
    let sub_arr_two_size = right_index - middle_index;

    let temp_arr_one = new Array(sub_arr_one_size);
    let temp_arr_two = new Array(sub_arr_two_size);

    /* copy data to temp arrays */
    for (i = 0; i < sub_arr_one_size; i++) {
        temp_arr_one[i] = arr[left_index + i];
    }
    for (i = 0; i < sub_arr_two_size; i++) {
        temp_arr_two[i] = arr[middle_index + i + 1];
    }

    i = 0; j = 0; k = left_index;

    /* merge two sorted sub-arrays into one sorted array */
    while (i < sub_arr_one_size && j < sub_arr_two_size) {
        if (temp_arr_one[i] <= temp_arr_two[j]) {
            arr[k] = temp_arr_one[i];
            i++;
        } else {
            arr[k] = temp_arr_two[j];
            j++;
        }

        k++;
    }

    /* copy remaining elements of temp_arr_one if any */
    while (i < sub_arr_one_size) {
        arr[k] = temp_arr_one[i];
        i++;
        k++;
    }

    /* copy remaining elements of temp_arr_two if any */
    while (j < sub_arr_two_size) {
        arr[k] = temp_arr_two[j];
        j++;
        k++;
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
