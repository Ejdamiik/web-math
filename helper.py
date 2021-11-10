from typing import List, Tuple, Callable
from flask import send_file
from io import BytesIO


def hex2dec(hex_num: str) -> int:
	"""
	Function resposible for converting hexadecimal number to decimal number

	hex_num - string with hexadecimal number
	"""

	hex_num = hex_num.replace("\n","")
	convertion = {
	  "a": 10, "b": 11, "c": 12, 
	  "d": 13, "e": 14, "f": 15
	  }
	decimal = 0

	for index in range(len(hex_num)):

		if hex_num[index].lower() in convertion:
			decimal += (16**(len(hex_num) - index - 1)) * convertion[hex_num[index].lower()]
		else:
			decimal += (16**(len(hex_num) - index - 1)) * int(hex_num[index].lower())

	return decimal


def hexColor(color: str) -> Tuple:
	"""
	Function responsible for converting color hexcode to rgb tuple

	color - string with color hexcode
	"""
	color = color.replace("\n", "")
	r = hex2dec(color[1:3])
	g = hex2dec(color[3:5])
	b = hex2dec(color[5:])

	return (r, g, b)

def serve_img(img):
    """
    Allows to save PIL image object to a
    virtual file in memory and then return
    it as a HTTP response
    """

    img_io = BytesIO()
    img.savefig(img_io)
    img_io.seek(0)
    return send_file(img_io, mimetype='image/png')