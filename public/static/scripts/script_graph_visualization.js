function add_spaces(formula) {
	let formatted = "";

	for (let i = 0; i < formula.length; i++) {

		formatted = formatted + formula.charAt(i);
		formatted = formatted + " "
	}

	return formatted.slice(0, -1)
}


// handleSubmit je funkcia, ktorá sa spustí keď sa bude mať odoslať náš formulár
function get_graph(e) {
	e.preventDefault(); // zabrániť vstavenému odosielaniu v prehliadači

	let selected = null;

	unformatted = this.querySelector("#formula_entry").value;

	const color = this.querySelector("#plot_color").value;
	const formula = add_spaces(unformatted);

	const formular = new URLSearchParams(); // Vytvoríme štruktúru, ktorá bude reprezentovať formulár
	formular.append('formula', formula); // Pridáme tam naše hodnoty
	formular.append('color', color);

	const url = this.action; // Nacitame povodnu URL zadanu vo formulari
	const method = this.method; // NAcitame povodnu metodu zadanu vo formulari
	fetch(url, {method: method, body: formular}) // Urobíme HTTP požiadavku na náš server POST /render a formularom v tele požiadavky 
		.then((res) => res.blob()) // Dostali sme binárne dáta (blob)
		.then((image) => {
			document.querySelector("#output-plot").src = URL.createObjectURL(image); // Nastavíme src našeho <img> na načítaný obrázok
		})
	/*setTimeout(function(){
		scroll("output")
	}, 3000);*/
}

document.querySelector("#option_panel").addEventListener("submit", get_graph);
