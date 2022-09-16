/*
 * This C program reads from a text file, character by character, and 
 * writes the file contents to another file, character by character
 * 
 * Created By: Josh Johnson
 */

#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE* file_in;
    FILE* file_out;
    char c;

    /* tries to open existing file to read from */
    if ((file_in = fopen("../Test_Files/poem.txt", "r")) == NULL) {
        printf("Could not open the existing file to read from");
        exit(EXIT_FAILURE); /* same as exit(1) */
    }

    /* tries to open or create a file to write to */
    if ((file_out = fopen("../Test_Files/Output_Files/poem_dup_from_read_write_file_c.txt", "w")) == NULL) {
        printf("Could not create or open file");
        exit(EXIT_FAILURE);
    }

    /* prints file content character by character to output stream */
    do {
        char c;
    
        c = fgetc(file_in);
        if (!feof(file_in)) {
            fprintf(file_out, "%c", c);
        }
    } while (!feof(file_in));

    printf("Successfully wrote to the output file");
    fclose(file_in);
    fclose(file_out);
    
    return EXIT_SUCCESS; /* Same as return 0 */
}
