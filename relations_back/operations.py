from typing import Set, Tuple

Base = Set[str]
Relation = Set[Tuple[str, str]]


# Closures

def transitive_closure(relation: Relation) -> Relation:

	new_relation = relation
	old_relation = set()

	while new_relation != old_relation:

		old_relation = new_relation.copy()

		for a, b1 in old_relation:

			for b2, c in old_relation:

				if (b1 == b2) and (a, c) not in old_relation:
					new_relation.add((a, c))

	return new_relation


def reflexive_closure(base_set: Base, relation: Relation) -> Relation:

	new = relation.copy()
	for e in base_set:
		new.add((e, e))

	return new


def symetric_closure(relation: Relation) -> Relation:

	new_relation = relation.copy()
	for a, b in relation:

		new_relation.add((b, a))

	return new_relation


# ------------------------------------------------------------------------------ #
def find_most_frequent(base_set: Base, relation: Relation) -> Tuple[str, int]:

	frequency = {}

	for element in base_set:

		for duo in relation:

			if element in duo:

				if element in frequency:
					frequency[element] += 1
				else:
					frequency[element] = 1

	most = max(frequency, key = frequency.get)
	return most, frequency[most]
# ------------------------------------------------------------------------------ # 

# Predicates

def is_reflexive(base_set: Base, relation: Relation) -> bool:

	for e in base_set:

		if (e, e) not in relation:
			return False

	return True


def is_ireflexive(base_set: Base, relation: Relation) -> bool:

	for e in base_set:

		if (e, e) in relation:

			return False

	return True


def is_symetric(relation: Relation) -> bool:

	for a, b in relation:

		if (b, a) not in relation:
			return False

	return True


def is_antisymetric(relation: Relation) -> bool:

	for a, b in relation:

		if (b, a) in relation:
			return False

	return True


def is_transitive(relation: Relation) -> bool:

	for a, b1 in relation:

		for b2, c in relation:

			if b1 == b2 and (a, c) not in relation:
				return False

	return True

