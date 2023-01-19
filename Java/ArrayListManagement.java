/**
 * ArrayList Management:
 *  - Specifications
 *  - Iteration
 *  - Insertion
 *  - Deletion
 *  - Element Locating
 *  - Element Manipulation
 *  
 * Created By: Josh Johnson
 */

 /**
  * Using the Better Comments extension 
  * 
  * TODO: A to do comment for future editing
  * * This is an important comment which highlights the line
  * ? Question/Double-check comment
  * ! Incorrect comment
  */

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Iterator;
import java.util.ListIterator;
import java.util.List;
import java.util.Collections;

public class ArraylistManagement {
    private ArrayList<Integer> list0 = new ArrayList<>(); /* empty list */

    // * integer lists 
    private ArrayList<Integer> list1 = new ArrayList<Integer>(Arrays.asList(0)); 
    private ArrayList<Integer> list2 = new ArrayList<>() {{add(4); add(1);}};
    private ArrayList<Integer> list3 = new ArrayList<>(Arrays.asList(-4, 6, 2)); 
    private ArrayList<Integer> list4 = new ArrayList<>(Arrays.asList(0, 84, -3, 40, -21, 21));
    private ArrayList<Integer> list5 = new ArrayList<>(Arrays.asList(1, 2, 3, 4, 5, 6, 7, 8, 9)); 
    private ArrayList<Integer> list6 = new ArrayList<>(Arrays.asList(2, 4, 3, 2, 4, 2, 2)); 
    private ArrayList<Integer> list7 = new ArrayList<>(Arrays.asList(1, (int) 2.0, 3, 4, (int) 5.2, 6, 7, (int) 8.5, 9, (int) 10.9, 11)); 

    // * double lists 
    private ArrayList<Double> list8 = new ArrayList<Double>(Arrays.asList(3.5));
    private ArrayList<Double> list9 = new ArrayList<>(Arrays.asList((double) 5, 3.6)); 
    private ArrayList<Double> list10 = new ArrayList<>(Arrays.asList(-1.7, (double) 0, (double) 6));
    private ArrayList<Double> list11 = new ArrayList<>(Arrays.asList(6.9, 7.1, (double) -5, 3.7, -9.8)); 

    // * number lists
    private ArrayList<Number> list12 = new ArrayList<Number>(Arrays.asList(1, 2.0, 3, 4, 5.5, 6.6, 7, 8, 9.9));

    // * character lists 
    private ArrayList<Character> list13 = new ArrayList<Character>(Arrays.asList('a', 'b', 'c'));

    // * string lists 
    private ArrayList<String> list14 = new ArrayList<String>(Arrays.asList("")); 
    private ArrayList<String> list15 = new ArrayList<>(Arrays.asList("hello"));
    private ArrayList<String> list16 = new ArrayList<>(Arrays.asList("Hello World"));
    private ArrayList<String> list17 = new ArrayList<>(Arrays.asList("hello world")); 
    private ArrayList<String> list18 = new ArrayList<>(Arrays.asList("HELLO WORLD"));
    private ArrayList<String> list19 = new ArrayList<>(Arrays.asList("hello", "world"));
    private ArrayList<String> list20 = new ArrayList<>(Arrays.asList("hello", "world", "of", "coding", "!"));
    private ArrayList<String> list21 = new ArrayList<>(Arrays.asList("hello world of coding!"));
    private ArrayList<String> list22 = new ArrayList<>(Arrays.asList("cat", "dog", "cat", "dog", "dog", "guinea pig", "fish"));
    private ArrayList<String> list23 = new ArrayList<>(Arrays.asList("Discraft", "Innova", "Prodigy", "Axiom", "MVP", "Dynamic", "Gateway", "Latitude 64"));
    private ArrayList<String> list24 = new ArrayList<>(Arrays.asList("Vikings", "Packers", "Lions", "Bears"));
    private ArrayList<String> list27 = new ArrayList<>(Arrays.asList("Commander Cody", "Captain Rex", "Echo", "Commander Fox"));
    private ArrayList<String> list28 = new ArrayList<>(Arrays.asList("Anakin Skywalker", "Yoda", "Obi-Wan Kenobi", "Mace Windu", "Plo koon"));
    private ArrayList<String> list29 = new ArrayList<>(Arrays.asList("Anakin Skywalker", "Yoda", "Obi-Wan Kenobi", "Darth Sidious"));

    // * object lists 
    private ArrayList<Object> list25 = new ArrayList<Object>(Arrays.asList(1, 2, 3.0, 4, "JJ", 6, "Air Plane"));

    // * boolean lists 
    private ArrayList<Boolean> list26 = new ArrayList<Boolean>(Arrays.asList(true, false));

    public static void main(String[] args) {
        ArraylistManagement methods = new ArraylistManagement();

        /* categorized arraylist methods */
        methods.specifications();
        methods.iteration();
        methods.insertion();
        methods.deletion();
        methods.element_locating();
        methods.element_manipulation();
    }

    /* arraylist specifications  */
    private void specifications() {
        System.out.println("--- Specifications ---");

        /* converts list into a string */
        System.out.println("toString: " + list26.toString()); 

        /* converts an arraylist to an array */
        Object[] array = list3.toArray(); 
        System.out.println("toArray: " + Arrays.toString(array));

        /* shows number of elements within the list */
        System.out.println("size: " + list5.size()); 

        /* tells if arraylist is empty or not */  
        System.out.println("isEmpty: " + list15.isEmpty());    

        System.out.println();
    }

    /* arraylist insertion */
    private void insertion() {
        System.out.println("--- Insertion ---");

        /* appends the specified element to the end of the list */
        ArrayList<Integer> cloneListInt = new ArrayList<>(list5);
        cloneListInt.add(21); 
        System.out.println("add: " + cloneListInt.toString());

        /* enters a value at a given index; pushing all values previously at and after given index */
        ArrayList<Number> cloneListNumber = new ArrayList<>(list12);
        cloneListNumber.add(6, 5); 
        System.out.println("add; index: " + cloneListNumber.toString());

        /* appends all of the elements to the end of this list */
        ArrayList<String> temp1 = new ArrayList<>(list27);
        ArrayList<String> temp2 = new ArrayList<>(list28);
        temp1.addAll(temp2); 
        System.out.println("addAll: " + temp1.toString()); 

        /* inserts all of the elements into this list, starting at the specified position */
        temp1 = new ArrayList<>(list27);
        temp2 = new ArrayList<>(list28);
        temp1.addAll(1, temp2); 
        System.out.println("addAll; index: " + temp1.toString()); 

        System.out.println();
    }

    /* arraylist deletion */
    private void deletion() {
        System.out.println("--- Deletion ---");

        /* removes all of the elements from the list given */
        ArrayList<String> tempArrayString = new ArrayList<>(list21);
        tempArrayString.clear(); 
        System.out.println("clear: " + tempArrayString.toString());

        /* removes the element at the specified position in this list */
        ArrayList<Integer> temp1 = new ArrayList<>(list5);
        temp1.remove(2);
        System.out.println("remove; index: " + temp1.toString()); 

        /* removes the first occurrence of the specified element from this list, if it is present */
        ArrayList<String> temp2 = new ArrayList<>(list24);
        temp2.remove("Lions");
        System.out.println("remove; value: " + temp2.toString());  

        /* removes all of the elements of this collection that satisfy the given predicate */
        ArrayList<Integer> temp5 = new ArrayList<>(list5);
        temp5.removeIf(x -> (x % 2 == 0));
        System.out.println("removeIf: " + temp5.toString()); 

        ArrayList<String> temp6 = new ArrayList<>(list23);
        temp6.removeIf(x -> (x.charAt(0) == 'D'));
        System.out.println("removeIf: " + temp6.toString()); 

        /* removes from this list all of its elements that are contained in the specified collection */
        ArrayList<String> temp3 = new ArrayList<>(list29);
        ArrayList<String> temp4 = new ArrayList<>(list28);
        temp3.removeAll(temp4);
        System.out.println("removeAll: " + temp3.toString());

        /* returns a view of the portion of this list between the specified fromIndex, inclusive, and toIndex, exclusive */
        ArrayList<Integer> temp7 = new ArrayList<>(list5);
        List<Integer> temp8 = temp7.subList(3, 6);
        System.out.println("subList: " + temp8.toString()); 

        /* retains only the elements in this list that are contained in the specified collection */
        ArrayList<String> temp9 = new ArrayList<>(list28);
        ArrayList<String> temp10 = new ArrayList<>(list29);
        temp9.retainAll(temp10);
        System.out.println("retainAll: " + temp9.toString());

        System.out.println();
    }

    /* element location */
    private void element_locating() {
        System.out.println("--- Element Locating ---");

        /* returns true if list contains the specified element */
        System.out.println("contains: " + list19.contains("hello")); 

        /* returns the element at the specified position in list */
        System.out.println("get: " + list4.get(1)); 

        /* returns index o first occurrence of specified element in the list; else -1 if not found */
        System.out.println("indexOf: " + list22.indexOf("dog")); 

        /* returns the index of the last occurrence of the specified element in this list, or -1 if this list does not contain the element */
        System.out.println("lastIndexOf: " + list22.lastIndexOf("dog")); 

        System.out.println();
    }

    /* element manipulation */
    private void element_manipulation() {
        System.out.println("--- Element Manipulation ---");

        /* replaces value at given index with given value  */
        ArrayList<Character> tempArrayCharacter = new ArrayList<>(list13);
        tempArrayCharacter.set(2, 'e'); 
        System.out.println("set: " + tempArrayCharacter.toString());

        /* performs the given action for each element of the Iterable until all elements have been processed or the action throws an exception */
        ArrayList<Integer> temp1 = new ArrayList<>(list5);
        System.out.print("forEach: "); 
        temp1.forEach((n) -> System.out.print(n + " ... "));
        System.out.println();
        
        ArrayList<Integer> temp2 = new ArrayList<>(list5);
        System.out.print("forEach: "); 
        temp1.forEach((n) -> System.out.print(n*10 + " "));
        System.out.println();

        /* replaces each element of this list with the result of applying the operator to that element */
        ArrayList<String> temp3 = new ArrayList<>(list22);
        temp3.replaceAll(n -> n.toUpperCase());
        System.out.println("replaceAll: " + temp3.toString()); 

        ArrayList<String> temp4 = new ArrayList<>(list22);
        Collections.replaceAll(temp4, "dog", "best friend");
        System.out.println("replaceAll: " + temp4.toString()); 

        /* sorts this list according to the order induced by the specified Comparator */
        ArrayList<String> temp5 = new ArrayList<>(list23);
        Collections.sort(temp5);
        System.out.println("sort: " + temp5.toString()); 

        ArrayList<Integer> temp6 = new ArrayList<>(list4);
        Collections.sort(temp6);
        System.out.println("sort: " + temp6.toString()); 

        ArrayList<Integer> temp7 = new ArrayList<>(list4);
        Collections.sort(temp7, Collections.reverseOrder());
        System.out.println("sort: " + temp7.toString()); 

        System.out.println();
    }

    /* iterations of arraylists */
    private void iteration() {
        System.out.println("--- Iteration ---");

        /** 
         * returns an iterator over the elements in this list in proper sequence
         * * iterator can traverse list in a forward direction
         */
        ArrayList<Number> temp1 = new ArrayList<>(list5);
        Iterator<Number> iter = temp1.iterator();
        System.out.print("iterator: "); 
        while (iter.hasNext()) {
            System.out.print(iter.next() + " ");
        }

        System.out.println();

        /**
         *  returns a list iterator over the elements in this list (in proper sequence) 
         * * listIterator can traverse list in both forward and backward direction
         */
        System.out.print("listIterator: "); 
        ArrayList<Number> temp2 = new ArrayList<>(list5);
        ListIterator<Number> iter2 = temp2.listIterator();
        while (iter2.hasNext()) {
            System.out.print(iter2.next() + " ");
        }
        
        System.out.println();

        /**
         *  returns a list iterator over the elements in this list (in proper sequence) in reverse order
         * * listIterator can traverse list in both forward and backward direction
         */
        System.out.print("listIterator; reverse: "); 
        ArrayList<Number> temp3 = new ArrayList<>(list5);
        ListIterator<Number> iter3 = temp3.listIterator(list5.size());
        while (iter3.hasPrevious()) {
            System.out.print(iter3.previous() + " ");
        }
        
        System.out.println();

        /** 
         * returns a list iterator over the elements in this list (in proper sequence), starting at the specified position in the list
         *  * listIterator can traverse list in both forward and backward direction
         */
        System.out.print("listIterator; index: "); 

        ArrayList<Number> temp4 = new ArrayList<>(list5);
        ListIterator<Number> iter4 = temp4.listIterator(3);
        while (iter4.hasNext()) {
            System.out.print(iter4.next() + " ");
        }

        System.out.println();

        /**
         * returns a list iterator over the elements in this list (in proper sequence), starting at the specified position in the list; reverse 
         *  * listIterator can traverse list in both forward and backward direction
         */
        System.out.print("listIterator; index - reverse: "); 
        ArrayList<Number> temp5 = new ArrayList<>(list5);
        ListIterator<Number> iter5 = temp5.listIterator(3);
        while (iter5.hasPrevious()) {
            System.out.print(iter5.previous() + " ");
        }

        System.out.println();

        /** 
         * returns a list iterator over the elements in this list (in proper sequence), starting at the specified position in the list and stops at another index
         *  * listIterator can traverse list in both forward and backward direction
         */
        System.out.print("listIterator; start index - end index: "); 

        ArrayList<Number> temp6 = new ArrayList<>(list5);
        ListIterator<Number> iter6 = temp6.listIterator(4);
        int counterTemp = 0;
        while (iter6.hasNext() && counterTemp < 3) {
            System.out.print(iter6.next() + " ");
            counterTemp++;
        }

        System.out.println("\n");
    }
}
