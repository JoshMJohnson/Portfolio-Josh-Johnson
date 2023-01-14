/*
 * ArrayList Management:
 *  - Specifications
 *  - Insertion
 *  - Deletion
 *  - Element Locating
 *  - Element Manipulation
 * 
 * Created By: Josh Johnson
 */

import java.util.ArrayList;
import java.util.Arrays;

public class ArrayListManagement {
    private ArrayList<Integer> list0 = new ArrayList<>(); /* empty list */

    /* integer lists */
    private ArrayList<Integer> list1 = new ArrayList<Integer>(Arrays.asList(0)); 
    private ArrayList<Integer> list2 = new ArrayList<>() {{add(4); add(1);}};
    private ArrayList<Integer> list3 = new ArrayList<>(Arrays.asList(-4, 6, 2)); 
    private ArrayList<Integer> list4 = new ArrayList<>(Arrays.asList(0, 84, -3, 40, -21, 21));
    private ArrayList<Integer> list5 = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9)); 
    private ArrayList<Integer> list6 = new ArrayList<>(Arrays.asList(2, 4, 3, 2, 4, 2, 2)); 
    private ArrayList<Integer> list7 = new ArrayList<>(Arrays.asList(1, (int) 2.0, 3, 4, (int) 5.2, 6, 7, (int) 8.5, 9, (int) 10.9, 11)); 

    /* double lists */
    private ArrayList<Double> list8 = new ArrayList<Double>(Arrays.asList(3.5));
    private ArrayList<Double> list9 = new ArrayList<>(Arrays.asList((double) 5, 3.6)); 
    private ArrayList<Double> list10 = new ArrayList<>(Arrays.asList(-1.7, (double) 0, (double) 6));
    private ArrayList<Double> list11 = new ArrayList<>(Arrays.asList(6.9, 7.1, (double) -5, 3.7, -9.8)); 

    /* number lists */
    private ArrayList<Number> list12 = new ArrayList<Number>(Arrays.asList(1, 2.0, 3, 4, 5.5, 6.6, 7, 8, 9.9));

    /* character lists */
    private ArrayList<Character> list13 = new ArrayList<Character>(Arrays.asList('a', 'b', 'c'));

    /* string lists */
    private ArrayList<String> list14 = new ArrayList<String>(Arrays.asList("")); 
    private ArrayList<String> list15 = new ArrayList<>(Arrays.asList("hello"));
    private ArrayList<String> list16 = new ArrayList<>(Arrays.asList("Hello World"));
    private ArrayList<String> list17 = new ArrayList<>(Arrays.asList("hello world")); 
    private ArrayList<String> list18 = new ArrayList<>(Arrays.asList("HELLO WORLD"));
    private ArrayList<String> list19 = new ArrayList<>(Arrays.asList("hello", "world"));
    private ArrayList<String> list20 = new ArrayList<>(Arrays.asList("hello", "world", "of", "coding", "!"));
    private ArrayList<String> list21 = new ArrayList<>(Arrays.asList("hello world of coding!"));
    private ArrayList<String> list22 = new ArrayList<>(Arrays.asList("cat", "dog", "cat", "dog", "dog", "animal"));
    private ArrayList<String> list23 = new ArrayList<>(Arrays.asList("Discraft", "Innova", "Prodigy", "Axiom", "MVP", "Dynamic", "Gateway", "Latitude 64"));
    private ArrayList<String> list24 = new ArrayList<>(Arrays.asList("Vikings", "Packers", "Lions", "Bears"));

    /* object lists */
    private ArrayList<Object> list25 = new ArrayList<Object>(Arrays.asList(1, 2, 3.0, 4, "JJ", 6, "Air Plane"));

    /* boolean lists */
    private ArrayList<Boolean> list26 = new ArrayList<Boolean>(Arrays.asList(true, false));

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
        System.out.println("toString: " + list26.toString()); /* converts list into a string */

        Object[] array = list3.toArray(); /* converts an arraylist to an array */
        System.out.println("toArray: " + Arrays.toString(array));

        System.out.println("size: " + list5.size()); /* shows number of elements within the list */

        System.out.println("isEmpty: " + list15.isEmpty()); /* tells if arraylist is empty or not */       

        System.out.println();
    }

    /** list insertion */
    private void insertion() {
        System.out.println("--- Array Insertion ---");

        /* arraylist methods */
        ArrayList<Integer> cloneListInt = new ArrayList<>(list5);
        cloneListInt.add(21); /* appends the specified element to the end of the list */
        System.out.println("add: " + cloneListInt.toString());

        ArrayList<Number> cloneListNumber = new ArrayList<>(list12);
        cloneListNumber.add(6, 5); /* enters a value at a given index; pushing all values previously at and after given index */
        System.out.println("add; index: " + cloneListNumber.toString());

        System.out.println("addAll: ");

        System.out.println("addAll: ");

        System.out.println();
    }

    /** list deletion */
    private void deletion() {
        System.out.println("--- Array Deletion ---");

        /* arraylist methods */
        ArrayList<String> tempArrayString = new ArrayList<>(list21);
        tempArrayString.clear(); /* removes all of the elements from the list given */
        System.out.println("clear: " + tempArrayString.toString());

        System.out.println("remove: ");

        System.out.println("removeAll: ");

        System.out.println("removeIf: ");

        System.out.println("removeRange: ");

        System.out.println("retainAll: ");

        System.out.println();
    }

    /** element location */
    private void element_locating() {
        System.out.println("--- Element Locating ---");

        /* arraylist methods */
        System.out.println("contains: " + list19.contains("hello")); /* returns true if list contains the specified element */

        System.out.println("get: " + list4.get(1)); /* returns the element at the specified position in list */

        System.out.println("indexOf: " + list22.indexOf("dog")); /* returns index o first occurrence of specified element in the list; else -1 if not found */

        System.out.println();
    }

    /** element manipulation */
    private void element_manipulation() {
        System.out.println("--- Element Manipulation ---");

        /* arraylist methods */
        ArrayList<Character> tempArrayCharacter = new ArrayList<>(list13);
        tempArrayCharacter.set(2, 'e'); /* replaces value at given index with given value  */
        System.out.println("set: " + tempArrayCharacter.toString());

        System.out.println("forEach: ");

        System.out.println("replaceAll: ");

        System.out.println("sort: ");

        System.out.println("subList: ");
    }
}
