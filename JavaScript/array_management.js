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


// TODO: reorder lists to increasing order
const list0 = []; // * empty list 

// * integer lists 
const list1 = [0]; 
const list2 = [4, 1];
const list3 = [-4, 6, 2]; 
const list4 = [0, 84, -3, 40, -21, 21];
const list5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]; 
const list32 = [-4, -3, -2, -1, 0, 1, 2, 3, 4];
const list6 = [2, 4, 3, 2, 4, 2, 2]; 
const list7 = [1, 2.0, 3, 4, 5.2, 6, 7, 8.5, 9, 10.9, 11]; 
const list33 = [123456789];

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
const list30 = ["Chiefs", "Chargers", "Raiders", "Broncos"];
const list31 = ["Buccaneers", "Panthers", "Saints", "Falcons"];
const list25 = ["Commander Cody", "Captain Rex", "Echo", "Commander Fox"];
const list26 = ["Anakin Skywalker", "Yoda", "Obi-Wan Kenobi", "Mace Windu", "Plo koon"];
const list27 = ["Anakin Skywalker", "Yoda", "Obi-Wan Kenobi", "Darth Sidious"];

// * object lists 
const list28 = [1, 2, 3.0, 4, "JJ", 6, "Air Plane"];

// * boolean lists 
const list29 = [true, false];

// * fake lists
const list99 = "Commander Cody";

main();

/* main function */
function main() {
    // * specifications 
    console.log("\t\t\t\tSpecs");
    console.log("--------------------------------------");    
    create_copy();
    console.log("--------------------------------------"); 
    length();
    console.log("--------------------------------------"); 
    every();
    console.log("--------------------------------------"); 
    filter();
    console.log("--------------------------------------"); 
    isArray();
        
    console.log("\n\n**************************************");
    console.log("**************************************");
    console.log("**************************************\n\n");

    // * list manipulation
    console.log("\t\t\tList Manipulation");
    console.log("--------------------------------------");
    join();
    console.log("--------------------------------------");
    entries();
    console.log("--------------------------------------");
    forEach();
    

    console.log("\n\n**************************************");
    console.log("**************************************");
    console.log("**************************************\n\n");

    // * insertion 
    console.log("\t\t\t   Insertion");
    console.log("--------------------------------------");
    concat();
    console.log("--------------------------------------");

    
    console.log("\n\n**************************************");
    console.log("**************************************");
    console.log("**************************************\n\n");

    // * deletion 
    console.log("\t\t\t   Deletion");
    console.log("--------------------------------------");
    pop();

    console.log("\n\n**************************************");
    console.log("**************************************");
    console.log("**************************************\n\n");

    // * element locating 
    console.log("\t\t\tElement Locating");
    console.log("--------------------------------------");
    find();
    console.log("--------------------------------------");
    findIndex();
    console.log("--------------------------------------");
    includes();
    console.log("--------------------------------------");
    indexOf();

    console.log("\n\n**************************************");
    console.log("**************************************");
    console.log("**************************************\n\n");

    // * element manipulation
    console.log("\t\t  Element Manipulation");
    console.log("--------------------------------------");
    copyWithin();
    console.log("--------------------------------------");
    fill();
    console.log("--------------------------------------");
    from();
}

/**
 * creating a copy of an array 
 */
function create_copy() {
    // method one; part A
    let temp = list5.slice(); 
    process.stdout.write("List Copy 1; part A: ");
    console.log(temp);

    // method one; part B
    console.log(`List Copy 1; part B: ${temp}`);

    // method two
    temp = list5.map((x) => x); 
    process.stdout.write("List Copy 2: ");
    console.log(temp);
}

/** 
 * joins arrays and returns an array with the joined arrays
 */
function concat() { 
    // method one; 2 lists
    let temp1 = list24.slice();
    let temp2 = list30.slice();
    let combinedTemps = temp1.concat(temp2);

    process.stdout.write("concat; 2 lists: ");
    console.log(combinedTemps);

    // method two; 3 lists
    temp1 = list24.slice();
    temp2 = list30.slice();
    let temp3 = list31.slice();
    combinedTemps = temp1.concat(temp2, temp3);

    process.stdout.write("concat; 3 lists: ");
    console.log(combinedTemps);
}

/**
 * copies array elements within the array, to and from specified positions 
 * 
 * syntax: array.copyWithin(target, start, end)
 */
function copyWithin() { 
    // method 1
    let temp = list5.slice();
    temp.copyWithin(2,0);
    process.stdout.write("copyWithin; 2 parameters: ");
    console.log(temp);

    // method 2
    temp = list5.slice();
    temp.copyWithin(2, 0, 2);
    process.stdout.write("copyWithin; 3 parameters: ");
    console.log(temp);
}

/** 
 * returns a key/value pair Array Iteration Object
 */
function entries() {
    const temp = list25.slice();
    const c = temp.entries();

    console.log("entries: ");
    for (let x of c) {
        console.log("\t" + x.toString());
    }
}

/**
 * checks if every element in an array pass a test
 */
function every() { 
    // method 1
    let temp = list32.slice();
    let result = temp.every(isPositive);
    function isPositive(num) {
        return num > 0;
    }

    console.log(`every: ${result}`);

    // method 2
    temp = list5.slice();
    result = temp.every((num) => {return num > 0;});
    console.log(`every: ${result}`);
}

/** 
 * fill the elements in an array with a static value
 */
function fill() { 
    // method 1; fill all elements with a value
    let temp = list27.slice();
    temp.fill("Final 4");
    process.stdout.write("fill; change all elements: ");
    console.log(temp);

    // method 2; change range of elements    
    temp = list27.slice();
    temp.fill("Jedi", 1, 3);
    process.stdout.write("fill; change range of elements: ");
    console.log(temp);
}

/**
 * creates a new array with every element in an array that pass a test
 */
function filter() {
    const temp = list3.slice();
    const qualifiedElementsFromList = temp.filter(allPositive);
    function allPositive(num) {
        return num > 0;
    }

    process.stdout.write("filter: ");
    console.log(qualifiedElementsFromList);
}

/**
 * returns the value of the first element in an array that pass a test
 */
function find() { 
    const temp = list3.slice();
    let result = temp.find(firstPositive);
    function firstPositive(num) {
        return num > 0;
    }

    console.log("find: " + result);
}

/**
 * returns the index of the first element in an array that pass a test
 */
function findIndex() {  
    const temp = list3.slice();
    let result = temp.findIndex(firstPositive);
    function firstPositive(num) {
        return num > 0;
    }

    console.log("findIndex: " + result);
}

/**
 * calls a function for each array element
 */
function forEach() {
    console.log("forEach: ");
    list24.forEach(printPrefix);
    function printPrefix(element, index) {
        console.log(`\telement ${index} : ${element} `);
    }

    console.log("");
}

/**
 * creates an array from an object
 */
function from() { 
    // method 1
    let temp = list15.slice();
    let result = Array.from(temp.toString());
    
    process.stdout.write("from; 1 parameter: ");
    console.log(result);

    // method 2
    temp = list33.slice();
    result = Array.from(temp.toString(), x => x + x);
    
    process.stdout.write("from; 2 parameters: ");
    console.log(result);

    // method 3
    temp = list5.slice();
    result = Array.from(temp, x => x + x);
    
    process.stdout.write("from; 2 parameters: ");
    console.log(result);
}

/** 
 * check if an array contains the specified element
 */
function includes() { 
    // method 1; 1 parameter
    let temp = list30.slice();
    let result = temp.includes("Chargers");
    console.log(`includes; 1 parameter: ${result}`);

    // method 2; 2 parameters - start the search at position given
    temp = list30.slice();
    result = temp.includes("Chargers", 2);
    console.log(`includes; 2 parameters: ${result}`);
}

/**
 * search the array for an element and returns its position
 */
function indexOf() {
    // method 1; find first index
    let result = list22.indexOf("dog");
    console.log(`indexOf; find first index: ${result}`);

    // method 2; start at index given
    result = list22.indexOf("dog", 3);
    console.log(`indexOf; start at index given: ${result}`);
}

/**
 * checks whether an object is an array
 */
function isArray() {
    // returns true
    let result = Array.isArray(list1);
    console.log(`isArray: ${result}`);

    // returns false
    result = Array.isArray(list99);
    console.log(`isArray: ${result}`);
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
    console.log("keys: ");
}

/**
 * search the array for an element, starting at the end, and returns its position
 */
function lastIndexOf() { // TODO
    console.log("lastIndexOf: ");
}

/**
 * sets or returns the number of elements in an array
 */
function length() { 
    console.log(`length: ${list5.length}`);
}

/**
 * creates a new array with the result of calling a function for each array element
 */
function map() { // TODO
    console.log("map: ");
}

/**
 * allows you to add properties and methods to an Array object
 */
function prototype() { // TODO
    console.log("prototype: ");
}

/**
 * removes the last element of an array, and returns that element
 */
function pop() {
    let temp = list5.slice();
    let popped_value = temp.pop();

    // updated list after value is popped
    process.stdout.write("pop; remove last element: ");
    console.log(temp);

    // value of the element popped from the list
    console.log(`Popped value from above: ${popped_value}`);
}

/**
 * adds new elements to the end of an array, and returns the new length
 */
function push() { // TODO
    console.log("push: ");
}

/**
 * reduce the values of an array to a single value (going left-to-right)
 */
function reduce() { // TODO
    console.log("reduce: ");
}

/**
 * reduce the values of an array to a single value (going right-to-left)
 */
function reduceRight() { // TODO
    console.log("reduceRight: ");
}

/**
 * reverses the order of the elements in an array
 */
function reverse() { // TODO
    console.log("reverse: ");
}

/**
 * removes the first element of an array, and returns that element
 */
function shift() { // TODO
    console.log("shift: ");
}

/**
 * adds new elements to the beginning of an array, and returns the new length
 */
function unshift() { // TODO
    console.log("unshift: ");
}

/**
 * selects a part of an array, and returns the new array
 */
function slice() { // TODO
    console.log("slice: ");
}

/**
 * checks if any of the elements in an array pass a test
 */
function some() { // TODO
    console.log("some: ");
}

/**
 * sorts the elements of an array
 */
function sort() { // TODO
    console.log("sort: ");
}

/**
 * adds/removes elements from an array
 */
function splice() { // TODO
    console.log("splice: ");
}

/**
 * converts an array to a string, and returns the result
 */
function toString() { // TODO
    console.log("toString: ");
}

/**
 * returns the primitive value of an array
 */
function valueOf() { // TODO
    console.log("valueOf: ");
}
