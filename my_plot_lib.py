from PIL import Image
from typing import Tuple, Callable

def draw_plot(picture, function: Callable, color: Tuple) -> None:
	"""
	Function draws plot of function with color to a picture xd
	"""

	width, height = picture.size
	middle = (width // 2, height // 2)

	points = []
	for x in range(0,width + 1):
		xx = (x - middle[0])

	y = function(xx)

	if y != None: # ouf of Domain
	  points.append((xx, y))

	for i in range(1, len(points)):
		A = points[i - 1]
		B = points[i]

		A = (A[0] * 10, A[1])
		B = (B[0] * 10, B[1])

		A = (A[0] + middle[0], height - (A[1] + middle[1]))
		B = (B[0] + middle[0], height - (B[1] + middle[1]))

	line(picture, A, B, color)


def create_cartesian(picture) -> None:
	"""
	Function creates cartesian system to a picture
	"""
	color = (255, 0, 0)
	width, height = picture.size

	line(picture, (0, height // 2), (width, height // 2), color)
	line(picture, (width // 2, 0), (width // 2, height), color)

"""Functions"""

from math import sin, pi, log10, cos
from typing import Union

def quadratic(x: int) -> int:
  return x**2

def n_quadratic(x: int) -> int:
  return -x**2

def cubic(x: int) -> int:
  return x**3

def n_cubic(x: int) -> int:
  return -x**3

def absolute(x: int) -> int:
  return abs(x)

def linear(x: int) -> int:
  return 10 * x


def line(picture, A: Tuple, B: Tuple, color: Tuple) -> None:

  width, height = picture.size

  if A[0] == B[0]:
    if A[1] > B[1]:
        A,B=B,A
    for y in range(A[1], B[1] + 1):
      if y > 0 and y < height:
        if A[0] > 0 and A[0] < width: 
          picture.putpixel((A[0], y), color)

  elif A[1] == B[1]:
    if A[0] > B[0]:
        A,B=B,A
    for x in range(A[0], B[0] + 1):
      if x > 0 and x < width:
        if A[1] > 0 and A[1] < height:
          picture.putpixel((x, A[1]), color)

  else:
    if A[0] > B[0]:
        A,B=B,A
    dx = B[0] - A[0]
    dy = B[1] - A[1]
    if abs(dy/dx) > 1:
      for y in range(min(A[1], B[1]), max(A[1], B[1]) + 1):
        if y >= 0 and y < height:
          x = int((y - A[1] + (dy/dx) * A[0]) * (dx/dy))
          if x >= 0 and x < width:
            picture.putpixel((x, y), color)
    else:
      for x in range(min(A[0], B[0]), max(A[0], B[0]) + 1):
        if x >= 0 and x < width:
          y = int((B[1] - A[1])/(B[0] - A[0]) * (x - A[0]) + A[1])
          if y >= 0 and y < height:
            picture.putpixel((x, y), color)
