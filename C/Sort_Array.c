/*
 * This C program sorts unsorted arrays of integers given by
 * the program itself, as well as given through text files
 * using multiple different sorting algorithms. 
 *
 * Sorting algorithms implemented
 * - Selection Sort
 * - Insertion Sort
 * - Quick Sort
 * - Bubble Sort
 * - Merge Sort
 *
 * Created By: Josh Johnson
 */

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include <time.h>

#define NUM_ALGORITHMS 5 /* number of algorithms implemented */

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

/* performs a quick sort algorithm */
void array_quick_sort(int*, int, int);

/* 
 * quick sort helper function
 *
 * takes the last element as pivot, places the pivot element at 
 * correct position in sorted array, and places all smaller elements
 * to the left of the pivot and all greater elements to right of pivot 
 */
int partition(int*, int, int);

/* performs a bubble sort algorithm */
void array_bubble_sort(int*, int);

/* performs a merge sort algorithm */
void array_merge_sort(int*, int, int);

/* takes an array, splits it in half, and merges into one sorted array */
void merge(int*, int, int, int);

/* prints an array of integers to stdout */
void print_array(int*, int, int, char*, bool);

/* swaps two integers in memory */
void swap(int*, int*);

/* fills in an initialized array with random values */
void fill_array(int*, int);

int main() {
    node_t *head = NULL;
    int i, id = 0;
    char *file_name;
    int array_sizes[NUM_ALGORITHMS];
    int *array_pointers[NUM_ALGORITHMS];

    srand(time(NULL)); // seeding: prevents same random values

    /* applies sorting algorithms */
    /* selection sort - array size and values are given by program */
    id++;
    int array_one[9] = {4, 3, 2, 7, 1, 9, 8, 5, 6}; 
    array_sizes[id - 1] = sizeof array_one / sizeof array_one[0];
    array_pointers[id - 1] = array_one;

    print_array(array_pointers[id - 1], array_sizes[id - 1], id, "Selection", false);
    array_selection_sort(array_pointers[id - 1], array_sizes[id - 1]);
    print_array(array_pointers[id - 1], array_sizes[id - 1], id, "Selection", true);

    /* insertion sort - array size and values are given by program */
    id++;
    array_sizes[id - 1] = 20;
    array_pointers[id - 1] = (int*) malloc(array_sizes[id - 1] * sizeof(int));
    fill_array(array_pointers[id - 1], array_sizes[id - 1]);
    
    print_array(array_pointers[id - 1], array_sizes[id - 1], id, "Insertion", false);
    array_insertion_sort(array_pointers[id - 1], array_sizes[id - 1]);
    print_array(array_pointers[id - 1], array_sizes[id - 1], id, "Insertion", true);

    /* quick sort - array size and values are given by program */
    id++;
    array_sizes[id - 1] = 16;
    int array_three[array_sizes[id - 1]];
    array_pointers[id - 1] = array_three;
    fill_array(array_pointers[id - 1], array_sizes[id - 1]);

    print_array(array_pointers[id - 1], array_sizes[id - 1], id, "Quick", false);
    array_quick_sort(array_pointers[id - 1], 0, array_sizes[id - 1] - 1);
    print_array(array_pointers[id - 1], array_sizes[id - 1], id, "Quick", true);

    /* bubble sort - array size and values are discovered by reading a file */
    id++;
    file_name = "../Test_Files/random_integers_no_duplicates.txt";
    head = create_linked_list_from_file(file_name);
    array_sizes[id - 1] = size_of_list(head);
    array_pointers[id - 1] = (int*) malloc(array_sizes[id - 1] * sizeof(int));
    create_array_from_list(head, array_pointers[id - 1], array_sizes[id - 1]);
    
    print_array(array_pointers[id - 1], array_sizes[id - 1], id, "Bubble", false);
    array_bubble_sort(array_pointers[id - 1], array_sizes[id - 1]);
    print_array(array_pointers[id - 1], array_sizes[id - 1], id, "Bubble", true);   

    /* merge sort - array size and values are discovered by reading a file */
    id++;
    file_name = "../Test_Files/random_integers_with_duplicates.txt";
    head = create_linked_list_from_file(file_name);
    array_sizes[id - 1] = size_of_list(head);
    array_pointers[id - 1] = (int*) malloc(array_sizes[id - 1] * sizeof(int));
    create_array_from_list(head, array_pointers[id - 1], array_sizes[id - 1]);

    print_array(array_pointers[id - 1], array_sizes[id - 1], id, "Merge", false);
    array_merge_sort(array_pointers[id - 1], 0, array_sizes[id - 1] - 1);
    print_array(array_pointers[id - 1], array_sizes[id - 1], id, "Merge", true);

    /* frees allocated memory */
    free(array_pointers[1]);
    free(array_pointers[3]);
    free(array_pointers[4]);
        
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

/* performs a quick sort algorithm */
void array_quick_sort(int *arr, int low, int high) {
    if (low < high) {
        int index = partition(arr, low, high);

        /* separately sort elements before and after partition */
        array_quick_sort(arr, low, index - 1);
        array_quick_sort(arr, index + 1, high);
    }
}

/* 
 * quick sort helper function
 *
 * takes the last element as pivot, places the pivot element at 
 * correct position in sorted array, and places all smaller elements
 * to the left of the pivot and all greater elements to right of pivot 
 */
int partition(int *arr, int low, int high) {
    int temp, j;
    int pivot = arr[high];
    int i = low - 1;

    for (j = low; j <= high - 1; j++) {
        if (arr[j] < pivot) {
            i++;
            swap((arr + i), (arr + j));
        }
    }

    swap((arr + i + 1), (arr + high));

    return i + 1;
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

/* performs a merge sort algorithm */
void array_merge_sort(int *arr, int left_index, int right_index) {
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
void merge(int *arr, int left_index, int middle_index, int right_index) {
    int i, j, k;
    int sub_arr_one_size, sub_arr_two_size;
    int *temp_arr_one, *temp_arr_two;

    sub_arr_one_size = middle_index - left_index + 1;
    sub_arr_two_size = right_index - middle_index;

    temp_arr_one = (int*) malloc(sub_arr_one_size * sizeof(int));
    temp_arr_two = (int*) malloc(sub_arr_two_size * sizeof(int)); 
 
    /* copy data to temp arrays*/
    for (i = 0; i < sub_arr_one_size; i++) {
        *(temp_arr_one + i) = *(arr + left_index + i);
    }
    for (i = 0; i < sub_arr_two_size; i++) {
        *(temp_arr_two + i) = *(arr + middle_index + i + 1);
    }
  
    i = 0, j = 0, k = left_index;
 
    /* merge two sorted sub-arrays into one sorted array */
    while (i < sub_arr_one_size && j < sub_arr_two_size) {
        if (*(temp_arr_one + i) <= *(temp_arr_two + j)) {
            *(arr + k) = *(temp_arr_one + i);
            i++;
        } else {
            *(arr + k) = *(temp_arr_two + j);
            j++;
        }

        k++;
    }
 
    /* copy remaining elements of temp_arr_one if any */
    while (i < sub_arr_one_size) {
        *(arr + k) = *(temp_arr_one + i);
        i++;
        k++;
    }
 
    /* copy remaining elements of temp_arr_two if any */
    while (j < sub_arr_two_size) {
        *(arr + k) = *(temp_arr_two + j);
        j++;
        k++;
    }

    /* frees allocated memory */
    free(temp_arr_one);
    free(temp_arr_two);
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
    int temp;

    temp = *p1;
    *p1 = *p2;
    *p2 = temp;
}

/* fills in an initialized array with random values */
void fill_array(int* array_pointer, int array_size) {
    int i, random_value;

    for (i = 0; i < array_size; i++) {
        random_value = (rand() % 100) + 1; // random value between 1-100
        *(array_pointer + i) = random_value;
    }
}