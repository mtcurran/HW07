#!/usr/bin/env python

# I want to be able to call capitalize_nested from main w/ various lists 
# and get returned a new nested list with all strings capitalized.
# Ex. ['apple', ['bear'], 'cat']
# Result ex. ['Apple', ['Bear'], 'Cat']
# Verify you've tested w/ various nestings.
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()

def capitalize_nested(l):
	"""This function will capitalize the first letter in a list even if it is a list of lists"""
	for i in range(0,len(l)):
		if type(l[i]) == type([]):
			capitalize_nested(l[i])
		else:
			l[i] = l[i].capitalize()
	return l

def main():
	pass

if __name__ == '__main__':
	main()