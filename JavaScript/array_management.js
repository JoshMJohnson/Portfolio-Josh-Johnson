/**
 * Array Management JavaScript:
 *  - Specifications
 *  - List Conditions
 *  - Iteration
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
const list4 = [-4.1, 6.9, 2.4];
const list5 = [0, 84, -3, 40, -21, 21];
const list6 = [1, 2, 3, 4, 5, 6, 7, 8, 9]; 
const list7 = [9, 8, 7, 6, 5, 4, 3, 2, 1]; 
const list8 = [-4, -3, -2, -1, 0, 1, 2, 3, 4];
const list9 = [2, 4, 3, 2, 4, 2, 2]; 
const list10 = [1, 2.0, 3, 4, 5.2, 6, 7, 8.5, 9, 10.9, 11]; 
const list11 = [123456789];

// * double lists 
const list12 = [3.5];
const list13 = [5, 3.6, 1.2]; 
const list14 = [-1.7, 0, 6];
const list15 = [6.9, 7.1, -5, 3.7, -9.8]; 

// * number lists
const list16 = [1, 2.0, 3, 4, 5.5, 6.6, 7, 8, 9.9];

// * character lists 
const list17 = ['a', 'b', 'c'];

// * string lists 
const list18 = [""]; 
const list19 = ["hello"];
const list20 = ["Hello World"];
const list21 = ["hello world"]; 
const list22 = ["HELLO WORLD"];
const list23 = ["hello", "world"];
const list24 = ["hello", "world", "of", "coding", "!"];
const list25 = ["hello world of coding!"];
const list26 = ["cat", "dog", "cat", "dog", "dog", "guinea pig", "fish"];
const list27 = ["Discraft", "Innova", "Prodigy", "Axiom", "MVP", "Dynamic", "Gateway", "Latitude 64"];
const list28 = ["Vikings", "Packers", "Lions", "Bears"];
const list29 = ["Chiefs", "Chargers", "Raiders", "Broncos"];
const list30 = ["Buccaneers", "Panthers", "Saints", "Falcons"];
const list31 = ["Commander Cody", "Captain Rex", "Echo", "Commander Fox"];
const list32 = ["Anakin Skywalker", "Yoda", "Obi-Wan Kenobi", "Mace Windu", "Plo koon"];
const list33 = ["Anakin Skywalker", "Yoda", "Obi-Wan Kenobi", "Darth Sidious"];

// * object lists 
const list34 = [1, 2, 3.0, 4, "JJ", 6, "Air Plane"];

// * boolean lists 
const list35 = [true, false];

// * fake lists
const list36 = "Commander Cody";

main();

/* main function */
function main() {
    // * specifications 
    console.log("\t\t\t\tSpecs");
    console.log("--------------------------------------"); 
    length();
    console.log("--------------------------------------");    
    create_copy();
    console.log("--------------------------------------"); 
    toString();
    console.log("--------------------------------------"); 
    valueOf();
    console.log("--------------------------------------"); 
    slice();
    console.log("--------------------------------------"); 
    filter();
    console.log("--------------------------------------"); 
    reduce();
    console.log("--------------------------------------"); 
    reduceRight();
        
    console.log("\n\n**************************************");
    console.log("**************************************");
    console.log("**************************************\n\n");

    // * list conditions
    console.log("\t\t\tList Conditions");
    console.log("--------------------------------------"); 
    every();
    console.log("--------------------------------------"); 
    some();
    console.log("--------------------------------------"); 
    isArray();
    console.log("--------------------------------------");
    includes();

    console.log("\n\n**************************************");
    console.log("**************************************");
    console.log("**************************************\n\n");

    // * iteration
    console.log("\t\t\tIteration");
    console.log("--------------------------------------");
    entries();  
    console.log("--------------------------------------");
    keys();
    
    console.log("\n\n**************************************");
    console.log("**************************************");
    console.log("**************************************\n\n");

    // * list manipulation
    console.log("\t\tList Manipulation");
    console.log("--------------------------------------");
    join();    
    console.log("--------------------------------------");
    forEach();
    console.log("--------------------------------------");
    reverse();
    console.log("--------------------------------------");
    sort();
    console.log("--------------------------------------");
    prototype();
    
    console.log("\n\n**************************************");
    console.log("**************************************");
    console.log("**************************************\n\n");

    // * insertion 
    console.log("\t\t\t   Insertion");
    console.log("--------------------------------------");
    concat();
    console.log("--------------------------------------");
    push();
    console.log("--------------------------------------");
    unshift();
    console.log("--------------------------------------");
    splice();
    
    console.log("\n\n**************************************");
    console.log("**************************************");
    console.log("**************************************\n\n");

    // * deletion 
    console.log("\t\t\t   Deletion");
    console.log("--------------------------------------");
    pop();
    console.log("--------------------------------------");
    shift();
    console.log("--------------------------------------");
    splice();

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
    lastIndexOf();
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
    console.log("--------------------------------------");
    map();
}

/**
 * creating a copy of an array 
 */
function create_copy() {
    // method one; part A
    let temp = list6.slice(); 
    process.stdout.write("List Copy 1; part A: ");
    console.log(temp);

    // method one; part B
    console.log(`List Copy 1; part B: ${temp}`);

    // method two
    temp = list6.map((x) => x); 
    process.stdout.write("List Copy 2: ");
    console.log(temp);
}

/** 
 * joins arrays and returns an array with the joined arrays
 */
function concat() { 
    // method one; 2 lists
    let temp1 = list28.slice();
    let temp2 = list29.slice();
    let combinedTemps = temp1.concat(temp2);

    process.stdout.write("concat; 2 lists: ");
    console.log(combinedTemps);

    // method two; 3 lists
    temp1 = list28.slice();
    temp2 = list29.slice();
    let temp3 = list30.slice();
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
    let temp = list6.slice();
    temp.copyWithin(2,0);
    process.stdout.write("copyWithin; 2 parameters: ");
    console.log(temp);

    // method 2
    temp = list6.slice();
    temp.copyWithin(2, 0, 2);
    process.stdout.write("copyWithin; 3 parameters: ");
    console.log(temp);
}

/** 
 * returns a key/value pair Array Iteration Object
 */
function entries() {
    const temp = list31.slice();
    const c = temp.entries();

    console.log("entries: ");
    for (let x of c) {
        console.log("\t" + x.toString());
    }
}

/** 
 * fill the elements in an array with a static value
 */
function fill() { 
    // method 1; fill all elements with a value
    let temp = list33.slice();
    temp.fill("Final 4");
    process.stdout.write("fill; change all elements: ");
    console.log(temp);

    // method 2; change range of elements    
    temp = list33.slice();
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
    list28.forEach(printPrefix);
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
    let temp = list19.slice();
    let result = Array.from(temp.toString());
    
    process.stdout.write("from; 1 parameter: ");
    console.log(result);

    // method 2
    temp = list11.slice();
    result = Array.from(temp.toString(), x => x + x);
    
    process.stdout.write("from; 2 parameters: ");
    console.log(result);

    // method 3
    temp = list6.slice();
    result = Array.from(temp, x => x + x);
    
    process.stdout.write("from; 2 parameters: ");
    console.log(result);
}

/** 
 * check if an array contains the specified element
 */
function includes() { 
    // method 1; 1 parameter
    let temp = list29.slice();
    let result = temp.includes("Chargers");
    console.log(`includes; 1 parameter: ${result}`);

    // method 2; 2 parameters - start the search at position given
    temp = list29.slice();
    result = temp.includes("Chargers", 2);
    console.log(`includes; 2 parameters: ${result}`);
}

/**
 * search the array for an element and returns its position
 */
function indexOf() {
    // method 1; find first index
    let result = list26.indexOf("dog");
    console.log(`indexOf; find first index: ${result}`);

    // method 2; start at index given
    result = list26.indexOf("dog", 3);
    console.log(`indexOf; start at index given: ${result}`);
}

/**
 * checks whether an object is an array
 */
function isArray() {
    // example 1
    let result = Array.isArray(list1);
    console.log(`isArray: ${result}`);

    // example 2
    result = Array.isArray(list36);
    console.log(`isArray: ${result}`);
}

/**
 * joins all elements of an array into a string
 */
function join() {
    let temp = list6.map((x) => x);
    console.log(`join: ${temp.join(" * ")}`);
}

/**
 * returns a Array Iteration Object, containing the keys of the original array
 */
function keys() {
    // example 1; create an Array Iterator object, containing the keys of the array
    let temp = list24.slice();
    let keys = temp.keys();

    console.log("keys; array iterator: ");
    for (let x of keys) {
        console.log(`\t${x}`);
    }

    // example 2; using the built in Object.keys() method
    temp = list24.slice();
    keys = Object.keys(temp);

    console.log("keys; object.keys: ");
    for (let x of keys) {
        console.log(`\t${x}`);
    }
}

/**
 * search the array for an element, starting at the end, and returns its position
 */
function lastIndexOf() {
    let result = list26.lastIndexOf("dog");
    console.log(`lastIndexOf: ${result}`);
}

/**
 * sets or returns the number of elements in an array
 */
function length() { 
    console.log(`length: ${list6.length}`);
}

/**
 * creates a new array with the result of calling a function for each array element
 */
function map() {
    // example 1
    let result = list6.map(Math.sqrt);
    process.stdout.write("map; example 1: ");
    console.log(result);

    // example 2
    result = list6.map(multTen);
    function multTen(num) {
        return num * 10;
    }

    process.stdout.write("map; example 2: ");
    console.log(result);

    // example 3
    result = list6.map(function (num) {
        return num % 2;
    });

    process.stdout.write("map; example 3: ");
    console.log(result);
}

/**
 * allows you to add properties and methods to an Array object
 */
function prototype() {
    // method 1
    Array.prototype.myUcase = function() {
        for (let i = 0; i < this.length; i++) {
            this[i] = this[i].toUpperCase();
        }
    };

    let temp = list24.slice();
    temp.myUcase();
    process.stdout.write("prototype; method 1: ");
    console.log(temp);

    // method 2
    Array.prototype.squareValues = function() {
        for (let i = 0; i < this.length; i++) {
            this[i] = Math.pow(this[i], 2);
        }
    };

    temp = list6.slice();
    temp.squareValues();
    process.stdout.write("prototype; method 2: ");
    console.log(temp);
}

/**
 * reduce the values of an array to a single value (going left-to-right)
 */
function reduce() {
    // example 1
    let temp = list3.slice();
    let result = temp.reduce(subtractionFunction);
    function subtractionFunction(total, num) {
        return total - num;
    }

    console.log(`reduce; example 1: ${result}`);

    // example 2
    temp = list13.slice();
    result = temp.reduce(integerSum, 0);
    function integerSum(total, num) {
        return total + Math.floor(num);
    }

    console.log(`reduce; example 2: ${result}`);
}

/**
 * reduce the values of an array to a single value (going right-to-left)
 */
function reduceRight() {
    // example 1
    let temp = list3.slice();
    let result = temp.reduceRight(subtractionFunction);
    function subtractionFunction(total, num) {
        return total - num;
    }

    console.log(`reduceRight; example 1: ${result}`);

    // example 2
    temp = list13.slice();
    result = temp.reduceRight(integerSum, 0);
    function integerSum(total, num) {
        return total + Math.floor(num);
    }

    console.log(`reduceRight; example 2: ${result}`);
}

/**
 * reverses the order of the elements in an array
 */
function reverse() {
    let temp = list6.slice();
    temp.reverse();
    process.stdout.write("reverse: ");
    console.log(temp);
}

/**
 * sorts the elements of an array
 */
function sort() {
    let temp = list7.slice();
    temp.sort();
    process.stdout.write("sort: ");
    console.log(temp);
}

/**
 * removes the last element of an array, and returns that element
 */
function pop() {
    let temp = list6.slice();
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
function push() {
    let temp = list31.slice();
    temp.push("Commander Wolffe");
    process.stdout.write("push: ");
    console.log(temp);
}

/**
 * removes the first element of an array, and returns that element
 */
function shift() {
    let temp = list6.slice();
    let shiftedItem = temp.shift();
    process.stdout.write("shift: ");
    console.log(temp);
    console.log(`shifted item from above: ${shiftedItem}`);
}

/**
 * adds new elements to the beginning of an array, and returns the new length
 */
function unshift() {
    // example 1; adding 1 item
    let temp = list32.slice();
    temp.unshift("Kit Fisto");
    process.stdout.write("unshift; add 1 item: ");
    console.log(temp);

    // example 2; adding multiple items
    temp = list32.slice();
    temp.unshift("Kit Fisto", "Shaak Ti", "Qui-Gon Jinn");
    process.stdout.write("unshift; add multiple items: ");
    console.log(temp);
}

/**
 * selects a part of an array, and returns the new array
 */
function slice() {
    // example 1; copy list
    let temp = list6.slice();
    process.stdout.write("slice; copy list: ");
    console.log(temp);

    // example 2; copy range of elements using positive values
    temp = list6.slice(1, 4);
    process.stdout.write("slice; copy range of elements using positive values: ");
    console.log(temp);

    // example 3; copy range of elements using negative values
    temp = list6.slice(-3, -1);
    process.stdout.write("slice; copy range of elements using negative values: ");
    console.log(temp);
}

/**
 * adds/removes elements from an array
 */
function splice() {
    /**
     * method 1; add elements
     *  - parameters: (starting index, number of elements to remove after insertion, element values to be inserted)
     * 
     */
    let temp = list6.slice();
    temp.splice(2, 1, "Hi", "Hello");
    process.stdout.write("splice; adding elements: ");
    console.log(temp);

    /**
     *  method 2; remove elements
     *  - parameters: (starting index to be removed, number of elements to remove)
     * 
     */
    temp = list6.slice();
    temp.splice(2, 3);
    process.stdout.write("splice; removing elements: ");
    console.log(temp);
}

/**
 * checks if every element in an array pass a test
 */
function every() { 
    // method 1
    let temp = list8.slice();
    let result = temp.every(isPositive);
    function isPositive(num) {
        return num > 0;
    }

    console.log(`every: ${result}`);

    // method 2
    temp = list6.slice();
    result = temp.every((num) => {return num > 0;});
    console.log(`every: ${result}`);
}

/**
 * checks if any of the elements in an array pass a test
 */
function some() {
    // method 1
    let temp = list8.slice();
    let result = temp.some(isPositive);
    function isPositive(num) {
        return num > 0;
    }

    console.log(`some: ${result}`);

    // method 2
    temp = list6.slice();
    result = temp.some((num) => {return num > 0;});
    console.log(`some: ${result}`);
}

/**
 * converts an array to a string, and returns the result
 */
function toString() {
    let temp = list6.slice();
    temp.toString();
    console.log(`toString: ${temp}`);
}

/**
 * returns the primitive value of an array
 */
function valueOf() {
    process.stdout.write("valueOf: ");
    console.log(list6.valueOf());
}
