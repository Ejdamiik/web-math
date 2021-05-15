from math import sqrt


def quadratic(a, b, c):
	if a == 0:
		return linear(b, c)

	D = b**2 - 4*a*c

	if D < 0:
		return None

	x1 = (b**2 + sqrt(D)) / (2 * a)
	x2 = (b**2 - sqrt(D)) / (2 * a)

	return x1, x2


def linear(a, b):
	if a == 0:
		return None

	return -b / a


def cubic(a, b, c, d):
	pass