/*
 * This C program sorts an unsorted array of integers given by
 * the program itself, as well as given through text files
 * using multiple different sorting algorithms 
 *
 * Sorting algorithms implemented
 * - Selection Sort
 * - Insertion Sort
 * - Bubble Sort
 * - TO DO: Quick Sort
 * - TO DO: Merge Sort
 * Created By: Josh Johnson
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

/* singly linked list of nodes struct */
typedef struct node {
    int value;
    struct node* next;
} node_t;

/* reads from a file of integers and creates an unsorted singly linked list of nodes */
node_t* create_linked_list_from_file(char*);

/* returns the number of nodes within the linked list that has no sentinal nodes */
int size_of_list(node_t*);

/* creates an array from a singly linked list of nodes */
void create_array_from_list(node_t*, int*, int);

/* performs a selection sort algorithm */
void array_selection_sort(int*, int);

/* performs an insertion sort algorithm */
void array_insertion_sort(int*, int);

/* performs a bubble sort algorithm */
void array_bubble_sort(int*, int);

/* prints an array of integers to stdout */
void print_array(int*, int, int, char*, bool);

/* swaps two integers in memory */
void swap(int*, int*);

/* fills in an initialized array with random values */
void fill_array(int*, int);

int main() {
    node_t *head = NULL;
    int i, id = 0;
    int array_one_size, array_two_size, array_three_size; 
    int *array_one_pointer, *array_two_pointer, *array_three_pointer;
    int array_one[9] = {4, 3, 2, 7, 1, 9, 8, 5, 6}; 
    char *file_name;

    /* applies sorting algorithms */
    /* selection sort - array size and values are given by program */
    array_one_size = sizeof array_one / sizeof array_one[0];
    array_one_pointer = array_one;

    id++;
    print_array(array_one_pointer, array_one_size, id, "Selection", false);
    array_selection_sort(array_one_pointer, array_one_size);
    print_array(array_one_pointer, array_one_size, id, "Selection", true);

    /* insertion sort - array size and values are given by program */
    array_two_size = 20;
    array_two_pointer = (int*) malloc(array_two_size * sizeof(int));
    fill_array(array_two_pointer, array_two_size);
    
    id++;
    print_array(array_two_pointer, array_two_size, id, "Insertion", false);
    array_insertion_sort(array_two_pointer, array_two_size);
    print_array(array_two_pointer, array_two_size, id, "Insertion", true);

    /* bubble sort - array size and values are discovered by reading a file */
    file_name = "../Test_Files/Random_Integers_No_Duplicates.txt";
    head = create_linked_list_from_file(file_name);
    array_three_size = size_of_list(head);
    array_three_pointer = (int*) malloc(array_three_size * sizeof(int));
    create_array_from_list(head, array_three_pointer, array_three_size);
    
    id++;
    print_array(array_three_pointer, array_three_size, id, "Bubble", false);
    array_bubble_sort(array_three_pointer, array_three_size);
    print_array(array_three_pointer, array_three_size, id, "Bubble", true);   

    
    /* frees allocated memory */
    free(array_two_pointer);
    free(array_three_pointer);
        
    return EXIT_SUCCESS; /* Same as return 0 */
}

/* reads from a file of integers and creates an unsorted singly linked list of nodes */
node_t* create_linked_list_from_file(char *file_name) {
    FILE *file;
    node_t *head = NULL, *current = NULL;

    /* tries to open file */
    if ((file = fopen(file_name, "r")) == NULL) {
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

/* returns the number of nodes within the linked list that has no sentinal nodes */
int size_of_list(node_t *head){
    node_t *current = head;
    int arr_two_size = 0;

    while (current != NULL) {
        arr_two_size++;
        current = current->next;
    }

    return arr_two_size;
}

/* creates an array from a singly linked list of nodes */
void create_array_from_list(node_t *head, int *arr_two, int arr_two_size) {
    node_t *current = head;
    int i;

    for (i = 0; i < arr_two_size; i++) {
        *(arr_two + i) = current->value;
        current = current->next;
    }
}

/* performs a selection sort algorithm */
void array_selection_sort(int *arr, int arr_size) {
    int i, j, min_idx;
 
    /* one by one move boundary of unsorted sub-array */
    for (i = 0; i < arr_size - 1; i++) {
        min_idx = i;

        /* find the minimum element in unsorted array */
        for (j = i + 1; j < arr_size; j++) {
            if (*(arr + j) < *(arr + min_idx)) {
                min_idx = j;
            }
        }
 
        /* swap the found minimum element with the first element */
        swap((arr + min_idx), (arr + i));
    }
}

/* performs an insertion sort algorithm */
void array_insertion_sort(int *arr, int arr_size) {
    int i, j, key;
    
    for (i = 1; i < arr_size; i++) {
        key = arr[i];
        j = i - 1;
 
        while (j >= 0 && arr[j] > key) {
            arr[j + 1] = arr[j];
            j--;
        }

        arr[j + 1] = key;
    }
}

/* performs a bubble sort algorithm */
void array_bubble_sort(int *arr, int arr_size) {
    int i, j;
    
    for (i = 0; i < arr_size - 1; i++) {
        for (j = 0; j < arr_size - i - 1; j++) {
            if (*(arr + j) > *(arr + j + 1)) {
                swap((arr + j), (arr + j + 1));
            }
        }
    }
}

/* prints an array of integers to stdout */
void print_array(int *array_pointer, int array_size, int array_id, char *algorithm, bool algorithm_applied) {
    int i;
    
    if (algorithm_applied) {
        printf("Array %d after %s Sort algorithm is applied: ", array_id, algorithm);
    } else {
        printf("Array %d before %s Sort algorithm is applied: ", array_id, algorithm);
    }

    /* prints the contents of the array into stdout */
    for (i = 0; i < array_size; i++) {
        if (i == array_size - 1) {
            printf("%d\n", *(array_pointer + i));
        }
        else {
            printf("%d ", *(array_pointer + i));
        }
    }
}

/* swaps two integers in memory */
void swap(int *p1, int *p2) {
    int temp = *p1;
    *p1 = *p2;
    *p2 = temp;
}

/* fills in an initialized array with random values */
void fill_array(int* array_pointer, int array_size) {
    int i, random_value;

    srand(time(NULL)); // seeding: prevents same random values every test case

    for (i = 0; i < array_size; i++) {
        random_value = (rand() % 100) + 1; // random value between 1-100
        *(array_pointer + i) = random_value;
    }
}