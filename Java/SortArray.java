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
import java.util.Scanner;
import java.io.FileNotFoundException;
import java.io.File;
import java.lang.Math;

 public class SortArray {
    public static void main (String [] args) {
        SortArray sa = new SortArray();

        /* array one - size and values are given by program */
        int[] array_one = new int[20];
        array_one = sa.fill_array(array_one);
        sa.print_array(array_one, 1, false, "Selection Sort");
        sa.array_selection_sort(array_one);
        sa.print_array(array_one, 1, true, "Selection Sort");
        
        /* array two - array size and values are discovered by reading a file */
        ArrayList<Integer> arr_two_list = sa.create_array_from_file();
        int[] array_two = sa.create_array_from_list(arr_two_list);
        sa.print_array(array_two, 2, false, "Selection Sort");
        sa.array_selection_sort(array_two);
        sa.print_array(array_two, 2, true, "Selection Sort");
    }

    /* reads from a file of integers and adds elements to an arraylist */
    private ArrayList<Integer> create_array_from_file() {
        ArrayList<Integer> list = new ArrayList<Integer>();

        try{
            File file_in = new File("../Test_Files/Random_Integers_With_Duplicates.txt");
            Scanner reader = new Scanner(file_in);

            while (reader.hasNextInt()) {
                int value = reader.nextInt();
                list.add(value);
            }

            System.out.println("Successfully read from file");
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
    private int[] fill_array (int[] arr) {
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
            for (int j = i + 1; j < arr.length; j++)
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
