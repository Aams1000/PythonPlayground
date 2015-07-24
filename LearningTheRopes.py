"""Testing classes"""
class test_class:
	
	def __init__ (self, _class_name, _num_students):
		self.name = _class_name
		self.num_students = _num_students
		self.additional_variables = {}

	def add_variables(self, **additional):
		if additional is not None:
			for note in additional.items():
				self.additional_variables.update({note[0] : note[1]})

	def print_class(self):
		print("Class name: {0} Number of students: {1}" .format(self.name, self.num_students))
		for i, additional in enumerate(self.additional_variables.items()):
			print("Additional note {0}: {1}" .format(i, additional))

math = test_class("Math", 10, )
additional_variables = {"Level" : "intermediate", "Schedule" : "M W F", "Professor" : "Oak", "Building" : "Kanto"}
math.add_variables(**additional_variables)
math.print_class()
"""Testing functions!"""
# def add_two (input_int):
# 	print("Inside function!")
# 	return x + 2


# def return_list_of_integers (input_list):
# 	for i, element in enumerate(input_list):
# 		print("Element {0}: {1}" .format(i, element))

# def test_kwargs (**kwargs):
# 	if kwargs != None:
# 		for element in kwargs.items():
# 			print(element)

# def test_args (*args):
# 	if args != None:
# 		for element in args:
# 			print(element)

# print ("Hello, world!");
# x = 4
# y = add_two(x)
# print ("Updated value: {:d}" .format(y))
# test_list = []
# for i in range(0, 5):
# 	test_list.append(i)

# test_dictionary = {'first': 1, "second": 2}
# test_kwargs(**test_dictionary)
# test_args(*test_list)

# return_list_of_integers(test_list)

# """Testing if statements"""
# test_input = int(input("How old are you?"))
# if test_input < 0 and test_input > -5:
# 	print("That is too young.")
# elif test_input >= 0:
# 	print("Success.")
# 	print("Second line.")

"""Testing lists"""
# test_list = [1, 2, 3]
# for element in test_list:
# 	print("List element: {:f}" .format(element))
#I'm really not liking this "simpler" way of creating lists. You seem to have a lot more control when actually writing the loops
# second_list = [(x,y) for x in range(0, 10) if x % 4 == 0 for y in range(20)]
# for squared_element in second_list:
# 	print("x = {:d}, y = {:d}" .format(squared_element[0], squared_element[1]))
# test_list = []
# for i in range(1, 15):
# 	for j in range(1, 15):
# 		if j % i != 0:
# 			test_list.append((i, j))

# #print list
# for pair in test_list:
# 	print("Tuple: ({:d},{:d})" .format(pair[0], pair[1]))

# #testing enumerators
# for i, pair in enumerate(test_list):
# 	print("Index: {:d} Pair: " .format(i), pair)

#testing sets
# test_set = set()
# for i in range(10):
# 	test_set.add(i)

# second_set = set()
# test_string = "Hello, world!"
# for character in test_string:
# 	if character != 'l':
# 		second_set.add(character)

# for i in range(0, 4):
# 	second_set.add(i)

# third_set = test_set.union(second_set)
# for element in third_set:
# 	print(element)

#test dictionaries
# test_dictionary = {}
# for i in range(0, 11):
# 	for char in "Hello, world!":
# 		test_dictionary.update({char : i})

# for entry in test_dictionary.items():
# 	print("Key value: {:s}, Item: {:d}" .format(entry[0], entry[1]))
# 	print(entry)

# """Testing while statements"""
# test_int = 0;
# while test_int < 10:
# 	print ('Test int : {:d}' .format(test_int))
# 	test_int += 1
# else:
# 	print("This else statement reminds me of a finally statement in Java.")

# """Testing for loops"""
# for i in range(0, 5):
# 	print("Current value: {:d}" .format(i))