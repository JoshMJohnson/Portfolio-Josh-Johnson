/**
 * Array Management JavaScript:
 *  - Specifications
 *  - List Manipulation
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

const list0 = []; // * empty list 

// * integer lists 
const list1 = [0]; 
const list2 = [4, 1];
const list3 = [-4, 6, 2]; 
const list4 = [0, 84, -3, 40, -21, 21];
const list5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]; 
const list6 = [2, 4, 3, 2, 4, 2, 2]; 
const list7 = [1, 2.0, 3, 4, 5.2, 6, 7, 8.5, 9, 10.9, 11]; 

// * double lists 
const list8 = [3.5];
const list9 = [5, 3.6]; 
const list10 = [-1.7, 0, 6];
const list11 = [6.9, 7.1, -5, 3.7, -9.8]; 

// * number lists
const list12 = [1, 2.0, 3, 4, 5.5, 6.6, 7, 8, 9.9];

// * character lists 
const list13 = ['a', 'b', 'c'];

// * string lists 
const list14 = [""]; 
const list15 = ["hello"];
const list16 = ["Hello World"];
const list17 = ["hello world"]; 
const list18 = ["HELLO WORLD"];
const list19 = ["hello", "world"];
const list20 = ["hello", "world", "of", "coding", "!"];
const list21 = ["hello world of coding!"];
const list22 = ["cat", "dog", "cat", "dog", "dog", "guinea pig", "fish"];
const list23 = ["Discraft", "Innova", "Prodigy", "Axiom", "MVP", "Dynamic", "Gateway", "Latitude 64"];
const list24 = ["Vikings", "Packers", "Lions", "Bears"];
const list25 = ["Commander Cody", "Captain Rex", "Echo", "Commander Fox"];
const list26 = ["Anakin Skywalker", "Yoda", "Obi-Wan Kenobi", "Mace Windu", "Plo koon"];
const list27 = ["Anakin Skywalker", "Yoda", "Obi-Wan Kenobi", "Darth Sidious"];

// * object lists 
const list28 = [1, 2, 3.0, 4, "JJ", 6, "Air Plane"];

// * boolean lists 
const list29 = [true, false];

main();

/* main function */
function main() {
    /* specifications */
    console.log("\t\t\t\tSpecs");
    console.log("--------------------------------------");    

    console.log("\n\n**************************************");
    console.log("**************************************");
    console.log("**************************************\n\n");

    /* list manipulation */
    console.log("\t\t\tList Manipulation");
    console.log("--------------------------------------");
    create_copy();
    console.log("--------------------------------------");
    join();

    console.log("\n\n**************************************");
    console.log("**************************************");
    console.log("**************************************\n\n");

    /* insertion */
    console.log("\t\t\t   Insertion");
    console.log("--------------------------------------");

    console.log("\n\n**************************************");
    console.log("**************************************");
    console.log("**************************************\n\n");

    /* deletion */
    console.log("\t\t\t   Deletion");
    console.log("--------------------------------------");
    pop();

    console.log("\n\n**************************************");
    console.log("**************************************");
    console.log("**************************************\n\n");

    /* element locating */
    console.log("\t\t\tElement Locating");
    console.log("--------------------------------------");

    console.log("\n\n**************************************");
    console.log("**************************************");
    console.log("**************************************\n\n");

    /* element manipulation */
    console.log("\t\t  Element Manipulation");
    console.log("--------------------------------------");
}

/* creating a copy of an array */
function create_copy() {
    // method one
    let temp = list5.slice(); // makes a copy of list
    process.stdout.write("List Copy: ");
    console.log(temp);

    console.log(`List Copy: ${temp}`);

    // method two
    temp = list5.map((x) => x); // makes a copy of list
    process.stdout.write("List Copy 2: ");
    console.log(temp);
}

/** 
 * joins arrays and returns an array with the joined arrays
 */
function concat() { // TODO 
    
}

/**
 * copies array elements within the array, to and from specified positions 
 */
function copyWithin() { // TODO

}

/** 
 * returns a key/value pair Array Iteration Object
 */
function entries() { // TODO

}

/**
 * checks if every element in an array pass a test
 */
function every() { // TODO

}

/** 
 * fill the elements in an array with a static value
 */
function fill() { // TODO

}

/**
 * creates a new array with every element in an array that pass a test
 */
function filter() { // TODO

}

/**
 * returns the value of the first element in an array that pass a test
 */
function find() { // TODO

}

/**
 * returns the index of the first element in an array that pass a test
 */
function findIndex() { // TODO 

}

/**
 * calls a function for each array element
 */
function forEach() { // TODO

}

/**
 * creates an array from an object
 */
function from() { // TODO

}

/** 
 * check if an array contains the specified element
 */
function includes() { // TODO 

}

/**
 * search the array for an element and returns its position
 */
function indexOf() { // TODO

}

/**
 * checks whether an object is an array
 */
function isArray() { // TODO

}

/**
 * joins all elements of an array into a string
 */
function join() {
    let temp = list5.map((x) => x);
    console.log(`join: ${temp.join(" * ")}`);
}

/**
 * returns a Array Iteration Object, containing the keys of the original array
 */
function keys() { // TODO

}

/**
 * search the array for an element, starting at the end, and returns its position
 */
function lastIndexOf() { // TODO

}

/**
 * sets or returns the number of elements in an array
 */
function length() { // TODO

}

/**
 * creates a new array with the result of calling a function for each array element
 */
function map() { // TODO

}

/**
 * allows you to add properties and methods to an Array object
 */
function prototype() { // TODO

}

/**
 * removes the last element of an array, and returns that element
 */
function pop() {
    let temp = list5.slice();
    let popped_value = temp.pop();
    process.stdout.write("pop; remove last element: ");
    console.log(temp);
    console.log(`Popped value from above: ${popped_value}`);
}

/**
 * adds new elements to the end of an array, and returns the new length
 */
function push() { // TODO

}

/**
 * reduce the values of an array to a single value (going left-to-right)
 */
function reduce() { // TODO

}

/**
 * reduce the values of an array to a single value (going right-to-left)
 */
function reduceRight() { // TODO

}

/**
 * reverses the order of the elements in an array
 */
function reverse() { // TODO

}

/**
 * removes the first element of an array, and returns that element
 */
function shift() { // TODO

}

/**
 * adds new elements to the beginning of an array, and returns the new length
 */
function unshift() { // TODO

}

/**
 * selects a part of an array, and returns the new array
 */
function slice() { // TODO

}

/**
 * checks if any of the elements in an array pass a test
 */
function some() { // TODO

}

/**
 * sorts the elements of an array
 */
function sort() { // TODO

}

/**
 * adds/removes elements from an array
 */
function splice() { // TODO

}

/**
 * converts an array to a string, and returns the result
 */
function toString() { // TODO

}

/**
 * returns the primitive value of an array
 */
function valueOf() { // TODO

}
