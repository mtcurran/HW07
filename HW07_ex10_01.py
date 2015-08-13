#!/usr/bin/env python

# I want to be able to call nested_sum from main w/ various nested lists
# and I greatly desire that the function returns the sum.
# Ex. [1, 2, [3]]
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def nested_sum(l, result=0):
	"""This function will calculate the sum of a list, even if it is a list of nested lists of
	nested lists etc."""
	for item in l:
		if type(item) == type([]):
			result = nested_sum(item, result)
		else:
			result += item
	return result

def main():
	pass


if __name__ == '__main__':
	main()