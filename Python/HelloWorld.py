# hello world part one
print("Hello World! - Part One")

# hello world part two function
def hello_world_two():
    print("Hello World! - Part Two")

# hello world part three function
def hello_world_three(hello, world, part):
    print(hello + " " + world + " - " + part)

# function calls
hello_world_two() # first function call
hello_world_three("Hello", "World!", "Part Three") # second function call

print("Hello", "World", "!", sep=" ")
print("Hellooo", end=" ")
print("Worlddd", end=" ")
print("!!!")