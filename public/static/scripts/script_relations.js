
function replaceLineBreaksWithHTML(string) {
 return string !== undefined ? string.replace(/\n/g, '<br/>') : "";
}


function handleSubmit(e) {

	e.preventDefault();

	let error_msg = "";

	const base = this.querySelector("#base_entry").value;
	const relation = this.querySelector("#relation_entry").value;

	if (base == ""){
		error_msg = "Please enter a base-set!";
	}

	if (relation == ""){
		error_msg = "Please enter a relation!";
	}

	let closures = [];


	if (this.querySelector("#reflexive_closure").checked) {
		closures.push("reflexive");
	}
	
	else if (this.querySelector("#symetric_closure").checked) {
		closures.push("symetric");
	}

	else if (this.querySelector("#transitive_closure").checked) {
		closures.push("transitive");
	}

	else {
		error_msg = "Pick at least one closure please!";
	}

	if (error_msg != ""){
		document.querySelector("#output-relations").innerHTML = error_msg;
		return null;
	}

	const formular = new URLSearchParams();


	formular.append('base', base);
	formular.append('relation', relation);
	formular.append('closures', closures);

	const url = this.action; // Nacitame povodnu URL zadanu vo formulari
	const method = this.method; // NAcitame povodnu metodu zadanu vo formulari

	fetch(url, {method: method, body: formular}) // Urobíme HTTP požiadavku na náš server POST /render a formularom v tele požiadavky 
		.then((res) => res.blob())
		.then((solution) => {
			prom = solution.text()

			prom.then(
				function(result){

					const converted = replaceLineBreaksWithHTML(result);
					document.querySelector("#output-relations").innerHTML = converted;
			})
		})
}


document.querySelector("#relations_form").addEventListener("submit", handleSubmit);