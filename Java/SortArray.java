/*
 * This Java program sorts an unsorted array of integers
 * using multiple different sorting algorithms 
 *
 * Sorting algorithms implemented
 * - Selection Sort
 * - TO DO: Bubble Sort
 * - TO DO: Merge Sort
 * - TO DO: Quick Sort
 * - TO DO: Insertion Sort
 * 
 * Created By: Josh Johnson
 */

 import java.util.ArrayList;
 import java.lang.Math;

 public class SortArray {
    public static void main (String [] args) {
        SortArray sa = new SortArray();

        /* array one - size and values are given by program */
        int[] array_one = new int[20];
        array_one = sa.create_array(array_one);
        sa.print_array(array_one, 1, false, "Selection Sort");
        sa.array_selection_sort(array_one);
        sa.print_array(array_one, 1, true, "Selection Sort");
        
        /* array two - array size and values are discovered by reading a file */
        int[] array_two; 
    }

    /* fills in an initialized array with random values */
    private int[] create_array (int[] arr) {
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
        for (int i = 0; i < (arr.length - 1); i++)
        {
            /* find the minimum element in unsorted array */
            int min_idx = i;
            for (int j = i+1; j < arr.length; j++)
                if (arr[j] < arr[min_idx])
                    min_idx = j;
 
            /* swap the found minimum element with the first element */
            int temp = arr[min_idx];
            arr[min_idx] = arr[i];
            arr[i] = temp;
        }

        return arr;
    }

    /* prints the contents of the given integer array to stdout */
    private void print_array(int[] arr, int arr_id, boolean ordered, String type) {
        if (ordered){
            System.out.print("Array with ID " + arr_id 
            + " after " + type + " algorithm: ");
        }
        else {
            System.out.print("Array with ID " + arr_id 
            + " before " + type + " algorithm: ");
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
