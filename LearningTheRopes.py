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

class income_tax_calculator:

	# TOP_BRACKET = 1000000
	# TOP_BRACKET_TAX_RATE = 0.133
	# TOP_BRACKET_CONSTANT = 1098840
	# SECOND_BRACKET = 508500
	# SECOND_BRACKET_TAX_RATE = 0.123
	# SECOND_BRACKET_CONSTANT = 26445.3
	# THIRD_BRACKET = 305100
	# THIRD_BRACKET_TAX_RATE = 0.113
	# THIRD_BRACKET_CONSTANT = 26445.3
	# FOURTH_BRACKET = 254250
	# FOURTH_BRACKET_TAX_RATE = 0.103
	# FOURTH_BRACKET_CONSTANT = 21207.75
	# FIFTH_BRACKET = 49774
	# FIFTH_BRACKET_TAX_RATE = 0.093
	# FIFTH_BRACKET_CONSTANT = 2191.48
	# SIXTH_BRACKET = 39384
	# SIXTH_BRACKET_TAX_RATE = 0.08
	# SIXTH_BRACKET_CONSTANT = 1360.28
	# SEVENTH_BRACKET = 28371
	# SEVENTH_BRACKET_TAX_RATE = 0.06
	# SEVENTH_BRACKET_CONSTANT = 699.50
	# EIGTH_BRACKET = 17976
	# EIGTH_BRACKET_TAX_RATE = 0.04
	# EIGTH_BRACKET_CONSTANT = 283.7
	# NINTH_BRACKET = 7982
	# NINTH_BRACKET_TAX_RATE = 0.02
	# NINTH_BRACKET_CONSTANT = 75.82
	# TENTH_BRACKET = 0
	# TENTH_BRACKET_TAX_RATE = 0.01
	# TENTH_BRACKET_CONSTANT = 0

	def __init__ (self, _taxable_income):
		self.taxable_income = _taxable_income
	

	def calculate_tax_rate_2014(self):
		
		TOP_BRACKET = 1000000
		TOP_BRACKET_TAX_RATE = 0.133
		TOP_BRACKET_CONSTANT = 1098840
		SECOND_BRACKET = 508500
		SECOND_BRACKET_TAX_RATE = 0.123
		SECOND_BRACKET_CONSTANT = 26445.3
		THIRD_BRACKET = 305100
		THIRD_BRACKET_TAX_RATE = 0.113
		THIRD_BRACKET_CONSTANT = 26445.3
		FOURTH_BRACKET = 254250
		FOURTH_BRACKET_TAX_RATE = 0.103
		FOURTH_BRACKET_CONSTANT = 21207.75
		FIFTH_BRACKET = 49774
		FIFTH_BRACKET_TAX_RATE = 0.093
		FIFTH_BRACKET_CONSTANT = 2191.48
		SIXTH_BRACKET = 39384
		SIXTH_BRACKET_TAX_RATE = 0.08
		SIXTH_BRACKET_CONSTANT = 1360.28
		SEVENTH_BRACKET = 28371
		SEVENTH_BRACKET_TAX_RATE = 0.06
		SEVENTH_BRACKET_CONSTANT = 699.50
		EIGTH_BRACKET = 17976
		EIGTH_BRACKET_TAX_RATE = 0.04
		EIGTH_BRACKET_CONSTANT = 283.7
		NINTH_BRACKET = 7982
		NINTH_BRACKET_TAX_RATE = 0.02
		NINTH_BRACKET_CONSTANT = 75.82
		TENTH_BRACKET = 0
		TENTH_BRACKET_TAX_RATE = 0.01
		TENTH_BRACKET_CONSTANT = 0
		state_income_tax = 0
		taxable_income = self.taxable_income
		if taxable_income > TOP_BRACKET:
			state_income_tax += (taxable_income - TOP_BRACKET) * TOP_BRACKET_TAX_RATE + TOP_BRACKET_CONSTANT
			taxable_income = TOP_BRACKET
		if taxable_income > SECOND_BRACKET:
			state_income_tax += (taxable_income - SECOND_BRACKET) * SECOND_BRACKET_TAX_RATE + SECOND_BRACKET_CONSTANT
			taxable_income = SECOND_BRACKET
		if taxable_income > THIRD_BRACKET:
			state_income_tax += (taxable_income - THIRD_BRACKET) * THIRD_BRACKET_TAX_RATE + THIRD_BRACKET_CONSTANT
			taxable_income = THIRD_BRACKET
		if taxable_income > FOURTH_BRACKET:
			state_income_tax += (taxable_income - FOURTH_BRACKET) * FOURTH_BRACKET_TAX_RATE + FOURTH_BRACKET_CONSTANT
			taxable_income = FOURTH_BRACKET
		if taxable_income > FIFTH_BRACKET:
			state_income_tax += (taxable_income - FIFTH_BRACKET) * FIFTH_BRACKET_TAX_RATE + FIFTH_BRACKET_CONSTANT
			taxable_income = FIFTH_BRACKET
		if taxable_income > SIXTH_BRACKET:
			state_income_tax += (taxable_income - SIXTH_BRACKET) * SIXTH_BRACKET_TAX_RATE + SIXTH_BRACKET_CONSTANT
			taxable_income = SIXTH_BRACKET
		if taxable_income > SEVENTH_BRACKET:
			state_income_tax += (taxable_income - SEVENTH_BRACKET) * SEVENTH_BRACKET_TAX_RATE + SEVENTH_BRACKET_CONSTANT
			taxable_income = SEVENTH_BRACKET
		if taxable_income > EIGTH_BRACKET:
			state_income_tax += (taxable_income - EIGTH_BRACKET) * EIGTH_BRACKET_TAX_RATE + EIGTH_BRACKET_CONSTANT
			taxable_income = EIGTH_BRACKET
		if taxable_income > NINTH_BRACKET:
			state_income_tax += (taxable_income - NINTH_BRACKET) * NINTH_BRACKET_TAX_RATE + NINTH_BRACKET_CONSTANT
			taxable_income = NINTH_BRACKET
		if taxable_income > TENTH_BRACKET:
			state_income_tax += (taxable_income - TENTH_BRACKET) * TENTH_BRACKET_TAX_RATE + TENTH_BRACKET_CONSTANT
			taxable_income = TENTH_BRACKET
		return state_income_tax

test_income_tax = income_tax_calculator(75000)
print (test_income_tax.calculate_tax_rate_2014())
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