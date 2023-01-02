# Array Management:
#   - Specifications
#   - Insertion
#   - Deletion
#   - Element Locating
#   - Element Manipulation
#
# Created By: Josh Johnson

array0 = [] # empty array; size = 0

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

# characters arrays
array11 = [''] 
array12 = ['hello']
array13 = ['Hello World'] 
array14 = ['hello world'] 
array15 = ['HELLO WORLD'] 
array16 = ['hello', 'world'] 
array17 = ['hello', 'world', 'of', 'coding', '!']
array18 = ['hello world of coding!']
array19 = ['dog', 'cat', 'dog', 'dog', 'animal']
array20 = ['Discraft', 'Innova', 'Prodigy', 'Axiom', 'Dynamic', 'Gateway', 'Latitude 64']
array21 = ['Vikings', 'Packers', 'Lions', 'Bears']

# array specifications
print("Array Specifications:")

size_array = len(array17) # returns size of array
print("len: " + str(size_array))

count_array = array6.count(2) # returns number of occurences
print("Count Number: " + str(count_array))

count_array = array19.count("dog") # returns number of occurences
print("Count Text: " + str(count_array), end="\n\n")

# insertion
print("Element Insertion:")

temp_array = array5.copy()
temp_array.append(10) # inserts element to the end of the array
print("Append Number: " + str(temp_array))

temp_array = array16.copy()
temp_array.append("!") # inserts element to the end of the array
print("Append Text: " + str(temp_array))

temp_array = array17.copy()
temp_array.insert(1, "amazing") # inserts element at index given; pushes all elements previously at index given and after
print("Insert: " + str(temp_array))

temp_array1 = array20.copy()
temp_array2 = array21.copy()
temp_array1.extend(temp_array2) # adds all elements from parameter array to the end of working array in order
print("extend: " + str(temp_array1), end="\n\n")

# deletion
print("Element Deletion:")

temp_array = array20.copy()
temp_array.clear() # Removes all elements from the array
print("Clear: " + str(temp_array))

temp_array = array5.copy()
temp_array.pop() # removes last element
print("Pop No Parameter Given: " + str(temp_array))

temp_array = array5.copy()
temp_array.pop(1) # removes at index given and pulls all elements with a higher index than given parameter index
print("Pop With Parameter Given: " + str(temp_array))

temp_array = array19.copy()
temp_array.remove('dog') # removes first occurrence of parameter
print("Remove: " + str(temp_array), end="\n\n")

# element locating
print("Element Locating:")


# element manipulation
print("Element Manipulation:")
