print ("Hello, world!");
x = 4
print (x);

# """Testing if statements"""
# test_input = int(input("How old are you?"))
# if test_input < 0 and test_input > -5:
# 	print("That is too young.")
# elif test_input >= 0:
# 	print("Success.")
# 	print("Second line.")

"""Testing lists"""
test_list = [1, 2, 3]
for element in test_list:
	print("List element: {:f}" .format(element))
#I'm really not liking this "simpler" way of creating lists. You seem to have a lot more control when actually writing the loops
second_list = [(x,y) for x in range(0, 10) if x % 4 == 0 for y in range(20)]
for squared_element in second_list:
	print("x = {:d}, y = {:d}" .format(squared_element[0], squared_element[1]))



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
