/*
 * This Java program sorts unsorted arrays of integers given by
 * the program itself, as well as given through text files
 * using multiple different sorting algorithms. 
 *
 * Sorting algorithms implemented
 * - Bubble Sort
 * - Selection Sort
 * - Merge Sort
 * - Insertion Sort
 * - Quick Sort
 * 
 * Created By: Josh Johnson
 */

import java.util.ArrayList;
import java.util.Scanner;
import java.io.FileNotFoundException;
import java.io.File;
import java.lang.Math;

 public class SortArray {
    public static void main (String[] args) {
        SortArray sa = new SortArray();
        int array_id = 0;
        int[][] arrays = new int[5][]; // size of array is equal to number of algorithms implemented
        
        /* applying sorting algorithms */
        /* bubble sort - size and values are given by program */
        array_id++;
        arrays[array_id - 1] = new int[] {2, 6, 5, 8, 1, 9, 3, 4, 7};

        sa.print_array(arrays[array_id - 1], array_id, false, "Bubble");
        sa.array_bubble_sort(arrays[array_id - 1]);
        sa.print_array(arrays[array_id - 1], array_id, true, "Bubble");

        /* selection sort - size and values are given by program */
        array_id++;
        arrays[array_id - 1] = new int[20];
        sa.fill_array(arrays[array_id - 1]);

        sa.print_array(arrays[array_id - 1], array_id, false, "Selection");
        sa.array_selection_sort(arrays[array_id - 1]);
        sa.print_array(arrays[array_id - 1], array_id, true, "Selection");

        /* merge sort - size and values are given by program */
        array_id++;
        arrays[array_id - 1] = new int[15];
        sa.fill_array(arrays[array_id - 1]);

        sa.print_array(arrays[array_id - 1], array_id, false, "Merge");
        sa.array_merge_sort(arrays[array_id - 1], 0, arrays[array_id - 1].length - 1);
        sa.print_array(arrays[array_id - 1], array_id, true, "Merge");

        /* insertion sort - array size and values are discovered by reading a file */
        array_id++;
        String file_name = "../Test_Files/random_integers_no_duplicates.txt";
        ArrayList<Integer> array_list = sa.create_array_from_file(file_name);
        arrays[array_id - 1] = sa.create_array_from_list(array_list);

        sa.print_array(arrays[array_id - 1], array_id, false, "Insertion");
        sa.array_insertion_sort(arrays[array_id - 1]);
        sa.print_array(arrays[array_id - 1], array_id, true, "Insertion");

        /* quick sort - array size and values are discovered by reading a file */
        array_id++;
        file_name = "../Test_Files/random_integers_with_duplicates.txt";
        array_list = sa.create_array_from_file(file_name);
        arrays[array_id - 1] = sa.create_array_from_list(array_list);

        sa.print_array(arrays[array_id - 1], array_id, false, "Quick");
        sa.array_quick_sort(arrays[array_id - 1], 0, arrays[array_id - 1].length - 1);
        sa.print_array(arrays[array_id - 1], array_id, true, "Quick");
    }

    /* reads from a file of integers and adds elements to an arraylist */
    private ArrayList<Integer> create_array_from_file(String file_name) {
        ArrayList<Integer> list = new ArrayList<Integer>();

        try{
            File file_in = new File(file_name);
            Scanner reader = new Scanner(file_in);

            while (reader.hasNextInt()) {
                int value = reader.nextInt();
                list.add(value);
            }

            reader.close();
        } catch (FileNotFoundException e) {
            System.err.println("Could not find file");
            e.printStackTrace();
        }

        return list;
    }

    /* creates an array from an arraylist */
    private int[] create_array_from_list(ArrayList<Integer> list) {
        int arr_size = list.size();
        int[] arr = new int[arr_size];

        for (int i = 0; i < list.size(); i++) {
            arr[i] = list.get(i);
        }

        return arr;
    }

    /* fills in an initialized array with random values */
    private void fill_array(int[] arr) {
        int value;

        for (int i = 0; i < arr.length; i++) {
            value = (int) (Math.random() * 100) + 1; // random integer 1-100
            arr[i] = value;
        }
    }

    /* performs a selection sort algorithm */
    private void array_selection_sort(int[] arr) { 
        for (int i = 0; i < (arr.length - 1); i++) {
            /* find the minimum element in unsorted portion array */
            int min_idx = i;
            for (int j = i + 1; j < arr.length; j++) {
                if (arr[j] < arr[min_idx])
                    min_idx = j;
            }
 
            /* swap the found minimum element with the first element */
            if (min_idx != i) {
                int temp = arr[min_idx];
                arr[min_idx] = arr[i];
                arr[i] = temp;
            }
        }
    }

    /* performs a bubble sort algorithm */
    private void array_bubble_sort(int[] arr) {
        for (int i = 0; i < arr.length - 1; i++) {
            for (int j = 0; j < arr.length - i - 1; j++) {
                /* swap arr[j+1] and arr[j] */
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }

    /* performs a merge sort algorithm */
    private void array_merge_sort(int[] arr, int left_index, int right_index) {
        /* recursively calls itself to divide the array until array size becomes one */
        if (left_index < right_index) {
            int middle_index = left_index + (right_index - left_index) / 2;
 
            /* sort first and second halves of array */
            array_merge_sort(arr, left_index, middle_index);
            array_merge_sort(arr, middle_index + 1, right_index);
 
            /* merge the sorted sub-arrays */
            merge(arr, left_index, middle_index, right_index);
        }
    }

    /* takes an array, splits it in half, and merges into one sorted array */
    private void merge(int[] arr, int left_index, int middle_index, int right_index) {
        int i, j, k;
        int sub_arr_one_size = middle_index - left_index + 1;
        int sub_arr_two_size = right_index - middle_index;

        int[] temp_arr_one = new int[sub_arr_one_size];
        int[] temp_arr_two = new int[sub_arr_two_size];
 
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

    /* performs an insertion sort algorithm */
    private void array_insertion_sort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int key = arr[i];
            int j = i - 1;
 
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }

            arr[j + 1] = key;
        }
    }

    /* performs a quick sort algorithm */
    private void array_quick_sort(int[] arr, int low, int high) {
        if (low < high) {
            int index = partition(arr, low, high);
    
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
    private int partition(int[] arr, int low, int high) {
        int temp;
        int pivot = arr[high];
        int i = low - 1;
    
        for (int j = low; j <= high - 1; j++) {
            if (arr[j] < pivot) {
                i++;

                /* swap two elements */
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
            }
        }

        /* swap two elements */
        temp = arr[i+1];
        arr[i+1] = arr[high];
        arr[high] = temp;

        return i + 1;
    }
    
    /* prints the contents of the given integer array to stdout */
    private void print_array(int[] arr, int arr_id, boolean ordered, String sorting_type) {
        if (ordered){
            System.out.print("Array with ID " + arr_id 
                + " after " + sorting_type + " Sort algorithm applied: ");
        }
        else {
            System.out.print("Array with ID " + arr_id 
                + " before " + sorting_type + " Sort algorithm applied: ");
        }

        for (int i = 0; i < arr.length; i++) {
            if (i == (arr.length - 1)) {
                System.out.println(arr[i]);
                break;
            }

            System.out.print(arr[i] + " ");
        }
    }
 }
