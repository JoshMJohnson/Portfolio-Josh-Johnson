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
    private ArrayList<Integer> list0 = new ArrayList<Integer>(); /* empty list */

    /* integers lists */
    private ArrayList<Integer> list1 = new ArrayList<Integer>(Arrays.asList(0)); 
    private ArrayList<Integer> list2 = new ArrayList<Integer>() {{add(4); add(1);}};
    private ArrayList<Integer> list3 = new ArrayList<Integer>(Arrays.asList(-4, 6, 2)); 
    private ArrayList<Integer> list4 = new ArrayList<Integer>(Arrays.asList(0, 84, -3, 40, -21, 21));
    private ArrayList<Integer> list5 = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9)); 
    private ArrayList<Integer> list6 = new ArrayList<>(Arrays.asList(2, 4, 3, 2, 4, 2, 2)); 
    private ArrayList<Integer> list7 = new ArrayList<>(Arrays.asList(1, (int) 2.0, 3, 4, (int) 5.2, 6, 7, (int) 8.5, 9, (int) 10.9, 11)); 

    /* doubles lists */
    private ArrayList<Double> list8 = new ArrayList<Double>(Arrays.asList(3.5));
    private ArrayList<Double> list9 = new ArrayList<Double>(Arrays.asList((double) 5, 3.6)); 
    private ArrayList<Double> list10 = new ArrayList<>(Arrays.asList(-1.7, (double) 0, (double) 6));
    private ArrayList<Double> list11 = new ArrayList<>(Arrays.asList(6.9, 7.1, (double) -5, 3.7, -9.8)); 

    /* number lists */
    private ArrayList<Number> list12 = new ArrayList<Number>(Arrays.asList(1, 2.0, 3, 4, 5.5, 6.6, 7, 8, 9.9));

    /* string lists */
    private ArrayList<String> list13 = new ArrayList<String>(Arrays.asList("")); 
    private ArrayList<String> list14 = new ArrayList<String>(Arrays.asList("hello"));
    private ArrayList<String> list15 = new ArrayList<String>(Arrays.asList("Hello World"));
    private ArrayList<String> list16 = new ArrayList<String>(Arrays.asList("hello world")); 
    private ArrayList<String> list17 = new ArrayList<String>(Arrays.asList("HELLO WORLD"));
    private ArrayList<String> list18 = new ArrayList<>(Arrays.asList("hello", "world"));
    private ArrayList<String> list19 = new ArrayList<>(Arrays.asList("hello", "world", "of", "coding", "!"));
    private ArrayList<String> list20 = new ArrayList<>(Arrays.asList("hello world of coding!"));
    private ArrayList<String> list21 = new ArrayList<>(Arrays.asList("dog", "cat", "dog", "dog", "animal"));
    private ArrayList<String> list22 = new ArrayList<>(Arrays.asList("Discraft", "Innova", "Prodigy", "Axiom", "MVP", "Dynamic", "Gateway", "Latitude 64"));
    private ArrayList<String> list23 = new ArrayList<>(Arrays.asList("Vikings", "Packers", "Lions", "Bears"));

    /* object lists */
    private ArrayList<Object> list24 = new ArrayList<Object>(Arrays.asList(1, 2, 3.0, 4, "JJ", 6, "Air Plane"));

    public static void main(String[] args) {
        ArrayListManagement methods = new ArrayListManagement();

        /* categorized arraylist methods */
        methods.specifications();
        methods.insertion();
        methods.deletion();
        methods.element_locating();
        methods.element_manipulation();
    }

    /** list specifications */
    private void specifications() {
        System.out.println("--- Array Specifications ---");

        /* arraylist methods */
        System.out.println("List: " + list24.toString()); /* prints contents of list to stdout */
        System.out.println("Size: " + list5.size());
        System.out.println();
    }

    /** list insertion */
    private void insertion() {
        System.out.println("--- Array Insertion ---");

        /* arraylist methods */
        ArrayList<Integer> tempList = new ArrayList<>(list5);
        tempList.add(21);
        System.out.println("Add: " + tempList.toString());

        System.out.println();
    }

    /** list deletion */
    private void deletion() {
        System.out.println("--- Array Deletion ---");

        /* arraylist methods */

        System.out.println();
    }

    /** element location */
    private void element_locating() {
        System.out.println("--- Element Locating ---");

        /* arraylist methods */

        System.out.println();
    }

    /** element manipulation */
    private void element_manipulation() {
        System.out.println("--- Element Manipulation ---");

        /* arraylist methods */

        System.out.println();
    }
}
