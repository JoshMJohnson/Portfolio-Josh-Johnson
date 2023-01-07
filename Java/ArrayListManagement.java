/*
 * ArrayList Management:
 *  - TO DO: Specifications
 *  - TO DO: Insertion
 *  - TO DO: Deletion
 *  - TO DO: Element Locating
 *  - TO DO: Element Manipulation
 *
 * Created By: Josh Johnson
 */

import java.util.ArrayList;
import java.util.Arrays;

public class ArrayListManagement {
    private ArrayList<Integer> array0 = new ArrayList<Integer>(); /* empty list */

    /* integers lists */
    private ArrayList<Integer> array1 = new ArrayList<Integer>(Arrays.asList(0)); 
    private ArrayList<Integer> array2 = new ArrayList<Integer>() {{add(4); add(1);}};
    private ArrayList<Integer> array3 = new ArrayList<Integer>(Arrays.asList(-4, 6, 2)); 
    private ArrayList<Integer> array4 = new ArrayList<Integer>(Arrays.asList(0, 84, -3, 40, -21, 21));
    private ArrayList<Integer> array5 = new ArrayList<Integer>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9)); 
    private ArrayList<Integer> array6 = new ArrayList<Integer>(Arrays.asList(2, 4, 3, 2, 4, 2, 2)); 


    /* doubles lists */
    private ArrayList<Double> array7 = new ArrayList<Double>(Arrays.asList(3.5));
    private ArrayList<Double> array8 = new ArrayList<Double>(Arrays.asList((double) 5, 3.6)); 
    private ArrayList<Double> array9 = new ArrayList<Double>(Arrays.asList(-1.7, (double) 0, (double) 6));
    private ArrayList<Double> array10 = new ArrayList<Double>(Arrays.asList(6.9, 7.1, (double) -5, 3.7, -9.8)); 
    
    /* string lists */
    private ArrayList<String> array11 = new ArrayList<String>(Arrays.asList("")); 
    private ArrayList<String> array12 = new ArrayList<String>(Arrays.asList("hello"));
    private ArrayList<String> array13 = new ArrayList<String>(Arrays.asList("Hello World"));
    private ArrayList<String> array14 = new ArrayList<String>(Arrays.asList("hello world")); 
    private ArrayList<String> array15 = new ArrayList<String>(Arrays.asList("HELLO WORLD"));
    private ArrayList<String> array16 = new ArrayList<String>(Arrays.asList("hello", "world"));
    private ArrayList<String> array17 = new ArrayList<String>(Arrays.asList("hello", "world", "of", "coding", "!"));
    private ArrayList<String> array18 = new ArrayList<String>(Arrays.asList("hello world of coding!"));
    private ArrayList<String> array19 = new ArrayList<String>(Arrays.asList("dog", "cat", "dog", "dog", "animal"));
    private ArrayList<String> array20 = new ArrayList<String>(Arrays.asList("Discraft", "Innova", "Prodigy", "Axiom", "MVP", "Dynamic", "Gateway", "Latitude 64"));
    private ArrayList<String> array21 = new ArrayList<String>(Arrays.asList("Vikings", "Packers", "Lions", "Bears"));

    public static void main(String[] args) {
        ArrayListManagement methods = new ArrayListManagement();

        methods.specifications();
        methods.insertion();
        methods.deletion();
        methods.element_locating();
        methods.element_manipulation();
    }

    private void specifications() {
        System.out.println("--- Array Specifications ---");

        System.out.println("List: " + array20.toString());
    }

    private void insertion() {
        System.out.println("--- Array Insertion ---");


    }

    private void deletion() {
        System.out.println("--- Array Deletion ---");

    }

    private void element_locating() {
        System.out.println("--- Element Locating ---");

    }

    private void element_manipulation() {
        System.out.println("--- Element Manipulation ---");

    }
}
