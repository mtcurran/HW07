#!/usr/bin/env python

# I want to be able to call cumulative_sum from main w/ various lists and 
# get returned a list of the cumulative sums.
# You are safe to expect only integers in a flat list.
# Ex. the cumulative sum of [1, 2, 3] is [1, 3, 6]
#  - in the above example I want returned the list [1, 3, 6]
# In your final submission: 
#  - Do not print anything extraneous!
#  - Do not put anything but pass in main()


def cumulative_sum(l):
	"""This function will return a list of cumulative sums"""
	b = []
	for i in range(0,len(l)):
		b.append(sum(l[:i+1]))
	return b

def main():
	pass


if __name__ == '__main__':
	main()