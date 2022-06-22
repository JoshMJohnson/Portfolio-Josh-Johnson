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

/* singly linked list of nodes struct */
typedef struct node {
    int value;
    struct node* next;
} node_t;

/* reads from a file of integers and creates an unsorted singly linked list of nodes */
node_t* create_linked_list_from_file();

/* returns the number of nodes within the linked list that has no sentinal nodes */
int size_of_list(node_t*);

/* creates an array from a singly linked list of nodes */
void create_array_from_list(node_t*, int*, int);

/* performs a selection sort algorithm */
void array_selection_sort(int*, int);

/* swaps two integers in memory */
void swap(int*, int*);

int main() {
    int i;
    int arr_one[9] = {4, 3, 2, 7, 1, 9, 8, 5, 6};
    int* arr_one_pointer = arr_one;
    int* arr_two;
    int arr_two_size;
    node_t* head = NULL;
    
    head = create_linked_list_from_file();
    arr_two_size = size_of_list(head);
    arr_two = (int*) malloc(arr_two_size*sizeof(int));
    create_array_from_list(head, arr_two, arr_two_size);

    /* prints the first array before any sorting algorithm is applied */
    printf("Array one before any sorting algorithm has been applied: ");
    for (i = 0; i < (sizeof arr_one / sizeof arr_one[0]); i++) {
        if (i == (sizeof arr_one / sizeof arr_one[0]) - 1) {
            printf("%d\n", *(arr_one_pointer + i));
        }
        else {
            printf("%d ", *(arr_one_pointer + i));
        }
    }
    
    /* prints the second array before any sorting algorithm is applied */
    printf("Array two before any sorting algorithm has been applied: ");
    for (i = 0; i < arr_two_size; i++) {
        if (i == arr_two_size - 1) {
            printf("%d\n", *(arr_two + i));
        }
        else {
            printf("%d ", *(arr_two + i));
        }
    }

    /* applies sorting algorithms */
    /* selection sort */
    array_selection_sort(arr_one_pointer, sizeof arr_one / sizeof arr_one[0]);
    array_selection_sort(arr_two, arr_two_size);

    /* prints the first array after the selection sorting algorithm is applied */
    printf("Array one after selection sort: ");
    for (i = 0; i < (sizeof arr_one / sizeof arr_one[0]); i++) {
        if (i == (sizeof arr_one / sizeof arr_one[0]) - 1) {
            printf("%d\n", arr_one[i]);
        }
        else {
            printf("%d ", arr_one[i]);
        }
    }

    /* prints the second array after the selection sorting algorithm is applied */
    printf("Array two after selection sort: ");
    for (i = 0; i < arr_two_size; i++) {
        if (i == arr_two_size - 1) {
            printf("%d\n", arr_two[i]);
        }
        else {
            printf("%d ", arr_two[i]);
        }
    }

    /* frees the allocated memory */
    free(arr_two);
        
    return EXIT_SUCCESS; /* Same as return 0 */
}

/* returns the number of nodes within the linked list that has no sentinal nodes */
int size_of_list(node_t* head){
    node_t* current = head;
    int arr_two_size = 0;

    while (current != NULL) {
        arr_two_size++;
        current = current->next;
    }

    return arr_two_size;
}

/* creates an array from a singly linked list of nodes */
void create_array_from_list(node_t* head, int* arr_two, int arr_two_size) {
    node_t* current = head;
    int i;

    for (i = 0; i < arr_two_size; i++) {
        *(arr_two + i) = current->value;
        current = current->next;
    }
}

/* reads from a file of integers and creates an unsorted singly linked list of nodes */
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

/* performs a selection sort algorithm */
void array_selection_sort(int* arr, int n) {
    int i, j, min_idx;
 
    /* one by one move boundary of unsorted subarray */
    for (i = 0; i < n - 1; i++) {
        /* find the minimum element in unsorted array */
        min_idx = i;
        for (j = i + 1; j < n; j++) {
            if (*(arr + j) < *(arr + min_idx)) {
                min_idx = j;
            }
        }
 
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
