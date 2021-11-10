import relations_back.operations as o
import relations_back.parse_string as ps
from typing import List

def get_all(base_string: str,
			relation_string: str,
			closure_wanted: List[str]) -> str:

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
		"reflexive" : o.reflexive_closure,
		"symetric" : o.symetric_closure,
		"transitive" : o.transitive_closure
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


	closure_out = "Closure:\n"

	res = relation

	print(closure_wanted)
	for closure in closure_wanted:

		if closure == "reflexive":
			res = closures[closure](base, res)

		else:
			res = closures[closure](res)

	closure_out += str(res)

	out += positive[:-2]
	out += MARGIN
	out += MARGIN
	out += "Relation is not:\n"
	out += negative[:-2]
	out += MARGIN
	out += MARGIN
	out += closure_out[:-1]
	out += MARGIN

	return out
