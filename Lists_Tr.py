
num_strings = ['2','23','34','43'];
num_inits = [15, 100, 42, 66];
num_floats = [2.2, 6.3, 3.6323, 7,9334];
num_lists = [[1.2,3], [4,5,6], [7,8,9]];

#Summary of each list
print("\nThe variable num_strings is a " + str(type(num_strings)) + ".");
print("It contain the elements: " + str(num_strings));
print("The element " + num_strings[0] + " is a " + str(type(num_strings[0])) + ".");

print("\nThe variable num_inits is a " + str(type(num_inits)) + ".");
print("It contain the elements: " + str(num_inits));
print("The element " + str(num_inits[0]) + " is a " + str(type(num_inits[0])) + ".");

print("\nThe variable num_floats is a " + str(type(num_floats)) + ".");
print("It contain the elements: " + str(num_floats));
print("The element " + str(num_floats[0]) + " is a " + str(type(num_floats[0])) + ".");

print("\nThe variable num_lists is a " + str(type(num_lists)) + ".");
print("It contain the elements: " + str(num_lists));
print("The element " + str(num_lists[0]) + " is a " + str(type(num_lists[0])) + ".");

#Sorting the lists
num_strings.sort();
num_inits.sort();
num_lists.sort();
num_floats.sort();

