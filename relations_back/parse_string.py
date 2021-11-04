from typing import Tuple, Set


def extract_second(line: str) -> str:

	line = line.replace(" ", "")

	return line.split("=")[1]


def create_set(stringified: str) -> Set:

	# Only for tuples and strings

	res = set()

	stringified = stringified.replace(" ", "").replace("{", "").replace("}", "")

	elems = []

	e = ""
	in_tuple = False
	for char in stringified:

		if char == ",":
			if not in_tuple:
				elems.append(e)
				e = ""


		if char == "(":
			in_tuple = True

		if char == ")":
			in_tuple = False

		if char == ",":
			if in_tuple:
				e += char
		else:
			e += char

	if e != "":
		elems.append(e)


	for elem in elems:
		
		if elem[0] != "(":
			res.add(elem)
		else:
			res.add(create_tuple(elem))

	return res



def create_tuple(stringified: str) -> Tuple:

	stringified = stringified.replace(" ", "").replace("(", "").replace(")", "")
	elems = stringified.split(",")

	return tuple(elems)


def parse(path: str) -> Tuple[Set, Set[Tuple]]:

	with open(path, "r") as f:
		content = f.read()

	base_line, relation_line = content.split("\n")

	base_str = extract_second(base_line)
	relation_str = extract_second(relation_line)

	base = create_set(base_str)
	relation = create_set(relation_str)

	return base, relation