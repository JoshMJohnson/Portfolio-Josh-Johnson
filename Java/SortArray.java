/*
 * This Java program sorts an unsorted array of integers
 * using multiple different sorting algorithms 
 *
 * Sorting algorithms implemented
 * - Selection Sort
 * - Bubble Sort
 * - Insertion Sort
 * - Quick Sort
 * - TO DO: Merge Sort
 * 
 * Created By: Josh Johnson
 */

import java.util.ArrayList;
import java.util.Scanner;
import java.io.FileNotFoundException;
import java.io.File;
import java.lang.Math;

 public class SortArray {
    public static void main (String [] args) {
        SortArray sa = new SortArray();
        
        /* applying sorting algorithms */
        /* selection sort - size and values are given by program */
        int[] array_one = new int[20];
        array_one = sa.fill_array(array_one);
        sa.print_array(array_one, 1, false, "Selection");
        sa.array_selection_sort(array_one);
        sa.print_array(array_one, 1, true, "Selection");

        /* bubble sort - size and values are given by program */
        int[] array_two = {2, 5, 3, 9, 21, 56, 1, 2, 7, 3, 99, 65, 21, 8};
        sa.print_array(array_two, 2, false, "Bubble");
        sa.array_bubble_sort(array_two);
        sa.print_array(array_two, 2, true, "Bubble");

        /* insertion sort - array size and values are discovered by reading a file */
        ArrayList<Integer> array_three_list = sa.create_array_from_file("../Test_Files/Random_Integers_No_Duplicates.txt");
        int[] array_three = sa.create_array_from_list(array_three_list);
        sa.print_array(array_three, 3, false, "Insertion");
        sa.array_insertion_sort(array_three);
        sa.print_array(array_three, 3, true, "Insertion");

        /* quick sort - array size and values are discovered by reading a file */
        ArrayList<Integer> array_four_list = sa.create_array_from_file("../Test_Files/Random_Integers_With_Duplicates.txt");
        int[] array_four = sa.create_array_from_list(array_four_list);
        sa.print_array(array_four, 4, false, "Quick");
        sa.array_quick_sort(array_four, 0, array_four.length - 1);
        sa.print_array(array_four, 4, true, "Quick");

        /* TO DO: merge sort - array size and values are discovered by reading a file */
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
    private int[] fill_array(int[] arr) {
        int value;

        for (int i = 0; i < arr.length; i++) {
            value = (int) (Math.random()*100) + 1; // random integer 1-100
            arr[i] = value;
        }

        return arr;
    }

    /* performs a selection sort algorithm */
    private int[] array_selection_sort(int[] arr) { 
        /* one by one move boundary of unsorted subarray */
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

        return arr;
    }

    /* performs a bubble sort algorithm */
    private int[] array_bubble_sort(int[] arr) {
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

        return arr;
    }

    /* performs an insertion sort algorithm */
    private int[] array_insertion_sort(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            int key = arr[i];
            int j = i - 1;
 
            /* 
             * move elements of arr[0..i-1], that are greater than key, 
             * to one position ahead of their current position 
             */
            while (j >= 0 && arr[j] > key) {
                arr[j + 1] = arr[j];
                j--;
            }

            arr[j + 1] = key;
        }

        return arr;
    }

    /* performs a quick sort algorithm */
    private int[] array_quick_sort(int[] arr, int low, int high) {
        if (low < high) {
            int index = partition(arr, low, high);
    
            /* separately sort elements before and after partition */
            array_quick_sort(arr, low, index - 1);
            array_quick_sort(arr, index + 1, high);
        }

        return arr;
    }

    /* 
     * takes the last element as pivot, places the pivot element at 
     * correct position in sorted array, and places all smaller elements
     * to the left of the pivot and all greater elements to right of pivot 
     */
    private int partition(int[] arr, int low, int high) {
        int temp;
        int pivot = arr[high];
        int i = (low - 1);
    
        for(int j = low; j <= high - 1; j++) {
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

        return (i + 1);
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
