# List Management:
#   - Specifications
#   - Insertion
#   - Deletion
#   - Element Locating
#   - Element Manipulation
#
# Created By: Josh Johnson

#   Using the Better Comments extension:   
#   TODO: A to do comment for future editing
#   * This is an important comment which highlights the line
#   ? Question/Double-check comment
#   ! Incorrect comment

array0 = [] # * empty list

# * integer lists
array1 = [0] 
array2 = [4, 1] 
array3 = [-4, 6, 2] 
array4 = [0, 84, -3, 40, -21, 21] 
array5 = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
array6 = [2, 4, 3, 2, 4, 2, 2] 

# * double lists
array7 = [3.5]
array8 = [5, 3.6] 
array9 = [-1.7, 0, 6]
array10 = [6.9, 7.1, -5, 3.7, -9.8] 

# * string lists
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

# * object lists
array22 = [1, 2, 3.0, 4, 'JJ', 6, 'Air Plane']

# * boolean lists
array23 = [True, False]

# list specifications
def specifications():
    print("\t\t\tList Specs")

    # returns string value of the list
    print("--------------------------------------")
    print("List: " + str(array23))
    
    # returns size of array; number of elements
    print("--------------------------------------")
    size_array = len(array17) 
    print("len: " + str(size_array))

    # returns a value of element at given index
    print("--------------------------------------")
    index_value = array20[1]
    print("Index Value: " + str(index_value))

    # returns elements in list from specified indices
    print("--------------------------------------")
    range_array = array20[1:3]
    print("Array Range: " + str(range_array), end="\n\n")

    print("**************************************")
    print("**************************************")
    print("**************************************\n")

# list insertion
def insertion():
    print("\t\tList Element Insertion")

    # adds an element at the end of the list
    print("--------------------------------------")
    temp_array = array5.copy()
    temp_array.append(10)
    print("append; Number: " + str(temp_array))

    temp_array = array16.copy()
    temp_array.append("!")
    print("append; String: " + str(temp_array))

    # adds an element at the specified position
    print("--------------------------------------")
    temp_array = array17.copy()
    temp_array.insert(1, "amazing") 
    print("insert: " + str(temp_array))

    # add the elements of a list (or any iterable), to the end of the current list
    print("--------------------------------------")
    temp_array1 = array20.copy()
    temp_array2 = array21.copy()
    temp_array1.extend(temp_array2)
    print("extend: " + str(temp_array1), end="\n\n")

    print("**************************************")
    print("**************************************")
    print("**************************************\n")

# list deletion
def deletion():
    print("\t\tList Element Deletion")

    # removes all the elements from the list
    print("--------------------------------------")
    temp_array = array20.copy()
    temp_array.clear()
    print("clear: " + str(temp_array))

    # removes the element at the specified position
    print("--------------------------------------")
    temp_array = array5.copy()
    temp_array.pop() # removes last element
    print("pop; No Parameter Given: " + str(temp_array))

    temp_array = array5.copy()
    temp_array.pop(1) # removes at index given and pulls all elements with a higher index than given parameter index
    print("pop; With Parameter Given: " + str(temp_array))

    # removes the first occurrence with the specified value
    print("--------------------------------------")
    temp_array = array19.copy()
    temp_array.remove('dog') 
    print("remove: " + str(temp_array), end="\n\n")

    print("**************************************")
    print("**************************************")
    print("**************************************\n")

# element locating
def locating():
    print("\t\tList Element Locating")

    # returns the index of the first element with the specified value
    print("--------------------------------------")
    index_array = array5.index(3)
    print("index; Number: " + str(index_array))

    index_array = array19.index('dog')
    print("index; String: " + str(index_array))

    # returns the number of occurrences of the specified value
    print("--------------------------------------")
    count_array = array6.count(2) 
    print("count; Occurrences of a Number: " + str(count_array))

    count_array = array19.count("dog") 
    print("count; Occurrences of a String: " + str(count_array), end="\n\n")

    print("**************************************")
    print("**************************************")
    print("**************************************\n")

# element manipulation
def manipulation():
    print("\tList Element Manipulation")

    # reverses the order of the list
    print("--------------------------------------")
    temp_array = array5.copy()
    temp_array.reverse()
    print("reverse: " + str(temp_array))

    # sorts the list
    print("--------------------------------------")
    temp_array = array10.copy()
    temp_array.sort() # sorts array in ascending order
    print("sort; Ascending: " + str(temp_array))

    temp_array = array4.copy()
    temp_array.sort(reverse=True) # sorts array in descending order
    print("sort; Descending: " + str(temp_array))

    temp_array = array20.copy()
    temp_array.sort() # alphabetically sorts the array
    print("sort; Alphabetically: " + str(temp_array))

    temp_array = array20.copy()
    def orderByLength(param):
        return len(param)
    temp_array.sort(key=orderByLength) # sort by string length in ascending length
    print("sort; String Length Increasing: " + str(temp_array))

    # set an element value at given index
    print("--------------------------------------")
    temp_array = array21.copy()
    temp_array[3] = "Trash"
    print("Change Element Value: " + str(temp_array))    

# categorized list functions
specifications()
insertion()
deletion()
locating()
manipulation()