/*
 * This C program reads from a text file, character by character, and 
 * prints the file contents to stdout, character by character
 * 
 * Created By: Josh Johnson
 */

#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE* file;
    char c;

    /* tries to open file */
    if ((file = fopen("../Test_Files/Basic_Text.txt", "r")) == NULL) {
        printf("Could not open the file");

        exit(EXIT_FAILURE); /* same as exit(1) */
    }

    /* prints file content character by character to output stream */
    do {
        c = fgetc(file);

        if (!feof(file)) {
            printf("%c", c);
        }
    } while (!feof(file));

    fclose(file);
    return EXIT_SUCCESS; /* Same as return 0 */
}
