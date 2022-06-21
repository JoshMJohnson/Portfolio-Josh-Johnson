/*
 * This C program sorts an unsorted array of integers
 * - Does this in two different ways
 *  - Gets list of integers from a file in one way
 *  - Already has a list of integers in the second way
 * 
 * Created By: Josh Johnson
 */

#include <stdio.h>
#include <stdlib.h>

/* reads a file of integers and creates an unsorted array */
int create_array_from_file();

/* sorts an array in increasing order using selection sort method */
void array_selection_sort(int*, int);

/* swaps two integers in memory */
void swap(int*, int*);

int main() {
    int i;
    int arr_one[9] = {4, 3, 2, 7, 1, 9, 8, 5, 6};
    int* arr_one_pointer = arr_one;

    /* gets list of integers from a file */
    create_array_from_file();

    printf("Array one before ordering: ");

    for (i = 0; i < (sizeof arr_one / sizeof arr_one[0]); i++) {
        if (i == (sizeof arr_one / sizeof arr_one[0]) - 1) {
            printf("%d\n", *(arr_one_pointer + i));
        }
        else {
            printf("%d ", *(arr_one_pointer + i));
        }
    }

    /* sorts array */
    array_selection_sort(arr_one_pointer, sizeof arr_one / sizeof arr_one[0]);

    printf("Array one after ordering: ");

    for (i = 0; i < (sizeof arr_one / sizeof arr_one[0]); i++) {
        if (i == (sizeof arr_one / sizeof arr_one[0]) - 1) {
            printf("%d\n", arr_one[i]);
        }
        else {
            printf("%d ", arr_one[i]);
        }
    }
    
    return EXIT_SUCCESS; /* Same as return 0 */
}

/* reads a file of integers and creates an unsorted array */
int create_array_from_file() {
    FILE* file;

    /* tries to open file */
    if ((file = fopen("../Test_Files/Random_Integers_No_Duplicates.txt", "r")) == NULL) {
        printf("Could not open the file");

        exit(EXIT_FAILURE); /* same as exit(1) */
    }

    /* prints file content character by character to output stream */
    do {
        int num;
        fscanf(file, "%d", &num);

        // TODO: save num into array
        printf("%d\n", num); 
    } while (!feof(file));

    fclose(file);

    return EXIT_SUCCESS;
}

/* sorts an array in increasing order using selection sort method */
void array_selection_sort(int* arr, int n) {
    int i, j, min_idx;
 
    // One by one move boundary of unsorted subarray
    for (i = 0; i < n - 1; i++) {
 
        // Find the minimum element in unsorted array
        min_idx = i;
        for (j = i + 1; j < n; j++)
            if (*(arr + j) < *(arr + min_idx))
                min_idx = j;
 
        // Swap the found minimum element
        // with the first element
        swap((arr + min_idx), (arr + i));
    }
}

/* swaps two integers in memory */
void swap(int* p1, int* p2)
{
    int temp = *p1;
    *p1 = *p2;
    *p2 = temp;
}
