import relations_back.operations as o
import relations_back.parse_string as ps


def get_all(base_string, relation_string):

	base = ps.create_set(base_string)
	relation = ps.create_set(relation_string)


	results_properties = {
		"reflexive" : o.is_reflexive(base, relation),
		"ireflexive" : o.is_ireflexive(base, relation),
		"symetric" : o.is_symetric(relation),
		"antisymetric" : o.is_antisymetric(relation),
		"transitive" : o.is_transitive(relation)
	}

	closures = {
		"reflexive closure" : o.reflexive_closure(base, relation),
		"symetric closure" : o.symetric_closure(relation),
		"transitive closure" : o.transitive_closure(relation)
	}

		
	MARGIN = "\n" + ("-" * 40)  + "\n"

	out = MARGIN
	out += "Relation is:\n"

	positive = ""
	negative = ""
	for _property, result in results_properties.items():
		
		if result:

			positive += _property + ", "

		else:

			negative += _property + ", "


	closures_out = "Closures:\n"
	for _type, closure in closures.items():

		closures_out += f"{_type}: {closure}\n"


	out += positive[:-2]
	out += MARGIN
	out += MARGIN
	out += "Relation is not:\n"
	out += negative[:-2]
	out += MARGIN
	out += MARGIN
	out += closures_out[:-1]
	out += MARGIN

	return out
