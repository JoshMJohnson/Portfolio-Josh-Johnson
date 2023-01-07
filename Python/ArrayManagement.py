# Array Management:
#   - Specifications
#   - Insertion
#   - Deletion
#   - Element Locating
#   - Element Manipulation
#
# Created By: Josh Johnson

array0 = [] # empty array

# integers arrays
array1 = [0] 
array2 = [4, 1] 
array3 = [-4, 6, 2] 
array4 = [0, 84, -3, 40, -21, 21] 
array5 = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
array6 = [2, 4, 3, 2, 4, 2, 2] 

# doubles arrays
array7 = [3.5]
array8 = [5, 3.6] 
array9 = [-1.7, 0, 6]
array10 = [6.9, 7.1, -5, 3.7, -9.8] 

# string arrays
array11 = [''] 
array12 = ['hello']
array13 = ['Hello World'] 
array14 = ['hello world'] 
array15 = ['HELLO WORLD'] 
array16 = ['hello', 'world'] 
array17 = ['hello', 'world', 'of', 'coding', '!']
array18 = ['hello world of coding!']
array19 = ['dog', 'cat', 'dog', 'dog', 'animal']
array20 = ['Discraft', 'Innova', 'Prodigy', 'Axiom', 'MVP', 'Dynamic', 'Gateway', 'Latitude 64']
array21 = ['Vikings', 'Packers', 'Lions', 'Bears']

# array specifications
def specifications():
    print("--- Array Specifications ---")

    # list functions
    size_array = len(array17) # returns size of array
    print("len: " + str(size_array), end="\n\n")

# insertion
def insertion():
    print("--- Array Element Insertion ---")

    # list functions
    temp_array = array5.copy()
    temp_array.append(10) # inserts element to the end of the array
    print("Append; Number: " + str(temp_array))

    temp_array = array16.copy()
    temp_array.append("!") # inserts element to the end of the array
    print("Append; String: " + str(temp_array))

    temp_array = array17.copy()
    temp_array.insert(1, "amazing") # inserts element at index given; pushes all elements previously at index given and after
    print("Insert: " + str(temp_array))

    temp_array1 = array20.copy()
    temp_array2 = array21.copy()
    temp_array1.extend(temp_array2) # adds all elements from parameter array to the end of working array in order
    print("extend: " + str(temp_array1), end="\n\n")

# deletion
def deletion():
    print("--- Array Element Deletion ---")

    # list functions
    temp_array = array20.copy()
    temp_array.clear() # removes all elements from the array
    print("Clear: " + str(temp_array))

    temp_array = array5.copy()
    temp_array.pop() # removes last element
    print("Pop; No Parameter Given: " + str(temp_array))

    temp_array = array5.copy()
    temp_array.pop(1) # removes at index given and pulls all elements with a higher index than given parameter index
    print("Pop; With Parameter Given: " + str(temp_array))

    temp_array = array19.copy()
    temp_array.remove('dog') # removes first occurrence of parameter
    print("Remove: " + str(temp_array), end="\n\n")

# element locating
def locating():
    print("--- Array Element Locating ---")

    # list functions
    index_array = array5.index(3) # returns index value of first occurrence of number parameber
    print("Index; Number: " + str(index_array))

    index_array = array19.index('dog') # returns index value of first occurrence of string parameter
    print("Index; String: " + str(index_array))

    count_array = array6.count(2) # returns number of occurrences
    print("Count; Occurrences of a Number: " + str(count_array))

    count_array = array19.count("dog") # returns number of occurrences
    print("Count; Occurrences of a String: " + str(count_array), end="\n\n")

# element manipulation
def manipulation():
    print("--- Array Element Manipulation ---")

    # list functions
    temp_array = array5.copy()
    temp_array.reverse() # reverses the array elements
    print("Reverse: " + str(temp_array))

    temp_array = array10.copy()
    temp_array.sort() # sorts array in ascending order
    print("Sort; Ascending: " + str(temp_array))

    temp_array = array4.copy()
    temp_array.sort(reverse=True) # sorts array in descending order
    print("Sort; Descending: " + str(temp_array))

    temp_array = array20.copy()
    temp_array.sort() # alphabetically sorts the array
    print("Sort; Alphabetically: " + str(temp_array))

    temp_array = array20.copy()
    def orderByLength(param):
        return len(param)
    temp_array.sort(key=orderByLength) # sort by string length in ascending length
    print("Sort; String Length Increasing: " + str(temp_array))

specifications()
insertion()
deletion()
locating()
manipulation()