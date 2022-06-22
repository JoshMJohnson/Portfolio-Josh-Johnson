/*
 * This C program sorts an unsorted array of integers
 * using multiple different methods 
 *
 * Sorting algorithms implemented
 * - Selection Sort
 * - TODO Bubble Sort
 * - TODO Merge Sort
 * - TODO Quick Sort
 * - TODO Insertion Sort
 * 
 * Created By: Josh Johnson
 */

#include <stdio.h>
#include <stdlib.h>

/* singly linked list of nodes */
typedef struct node {
    int value;
    struct node* next;
} node_t;

/* reads a file of integers and creates an unsorted singly linked list of nodes */
node_t* create_linked_list_from_file();

/* selection sort method */
void array_selection_sort(int*, int);

/* swaps two integers in memory */
void swap(int*, int*);

int main() {
    int i;
    int arr_one[9] = {4, 3, 2, 7, 1, 9, 8, 5, 6};
    int* arr_one_pointer = arr_one;
    node_t* head = NULL;
    node_t* current = NULL;
    int* arr_two;
    int arr_two_size = 0;

    /* gets list of integers from a file */
    head = create_linked_list_from_file();

    /* get number of elements in list */
    current = head;

    while (current != NULL) {
        arr_two_size++;
        current = current->next;
    }

    // create an array with those elements from the list
    arr_two = (int*) malloc(arr_two_size*sizeof(int));
    current = head;

    for (i = 0; i < arr_two_size; i++) {
        *(arr_two + i) = current->value;
        current = current->next;
    }

    printf("Array one before ordering: ");

    for (i = 0; i < (sizeof arr_one / sizeof arr_one[0]); i++) {
        if (i == (sizeof arr_one / sizeof arr_one[0]) - 1) {
            printf("%d\n", *(arr_one_pointer + i));
        }
        else {
            printf("%d ", *(arr_one_pointer + i));
        }
    }
    
    printf("Array two before ordering: ");

    for (i = 0; i < arr_two_size; i++) {
        if (i == arr_two_size - 1) {
            printf("%d\n", *(arr_two + i));
        }
        else {
            printf("%d ", *(arr_two + i));
        }
    }

    /* sorts array */
    array_selection_sort(arr_one_pointer, sizeof arr_one / sizeof arr_one[0]);
    array_selection_sort(arr_two, arr_two_size);

    printf("Array one after ordering: ");

    for (i = 0; i < (sizeof arr_one / sizeof arr_one[0]); i++) {
        if (i == (sizeof arr_one / sizeof arr_one[0]) - 1) {
            printf("%d\n", arr_one[i]);
        }
        else {
            printf("%d ", arr_one[i]);
        }
    }

    printf("Array two after ordering: ");

    for (i = 0; i < arr_two_size; i++) {
        if (i == arr_two_size - 1) {
            printf("%d\n", arr_two[i]);
        }
        else {
            printf("%d ", arr_two[i]);
        }
    }
        
    return EXIT_SUCCESS; /* Same as return 0 */
}

/* TODO: creates an array from a singly linked list of nodes */


/* reads a file of integers and creates an unsorted array */
node_t* create_linked_list_from_file() {
    FILE* file;
    node_t* head = NULL;
    node_t* current = NULL;

    /* tries to open file */
    if ((file = fopen("../Test_Files/Random_Integers_No_Duplicates.txt", "r")) == NULL) {
        printf("Could not open the file");

        exit(EXIT_FAILURE); /* same as exit(1) */
    }

    /* prints file content character by character to output stream */
    do {
        int num;

        fscanf(file, "%d", &num);

        // save num into array
        if (head == NULL) {
            head = (node_t*) malloc(sizeof(node_t));
            head->value = num;
            head->next = NULL;
            continue;
        }

        current = head;

        /* traverse to the last existing element in the current list */
        while(current->next != NULL) {
            current = current->next;
        }

        current->next = (node_t*) malloc(sizeof(node_t));
        current->next->value = num;
        current->next->next = NULL;
    } while (!feof(file));

    fclose(file);

    return head;
}

/* selection sort method */
void array_selection_sort(int* arr, int n) {
    int i, j, min_idx;
 
    /* one by one move boundary of unsorted subarray */
    for (i = 0; i < n - 1; i++) {
        /* find the minimum element in unsorted array */
        min_idx = i;
        for (j = i + 1; j < n; j++)
            if (*(arr + j) < *(arr + min_idx))
                min_idx = j;
 
        /* swap the found minimum element with the first element */
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
