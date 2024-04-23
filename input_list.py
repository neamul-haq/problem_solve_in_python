num_elements = int(input())

# Get the list elements as a string separated by spaces
input_string = input()

# Split the string into a list of integers
my_list = list(map(int, input_string.split()))

# Check if the number of elements matches the length of the list
if len(my_list) != num_elements:
    print("Error: The number of elements entered does not match the specified length.")
else:
    # Now you have the list `my_list` containing the elements
    print(my_list)