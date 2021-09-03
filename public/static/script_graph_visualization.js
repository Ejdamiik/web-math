// handleSubmit je funkcia, ktorá sa spustí keď sa bude mať odoslať náš formulár
function get_graph(e) {
	e.preventDefault(); // zabrániť vstavenému odosielaniu v prehliadači

	let selected = null;
	if (document.querySelector("#linear").checked) {
		selected = document.querySelector("#linear").value;
	}

	if (document.querySelector("#quadratic").checked) {
	  selected = document.querySelector("#quadratic").value;
	}

	if (document.querySelector("#cubic").checked) {
	  selected = document.querySelector("#cubic").value;
	}

	const color = document.querySelector("#plot_color").value;

	const formular = new URLSearchParams(); // Vytvoríme štruktúru, ktorá bude reprezentovať formulár
	formular.append('selected', selected); // Pridáme tam naše hodnoty
	formular.append('color', color);

	const url = this.action; // Nacitame povodnu URL zadanu vo formulari
	const method = this.method; // NAcitame povodnu metodu zadanu vo formulari
	fetch(url, {method: method, body: formular}) // Urobíme HTTP požiadavku na náš server POST /render a formularom v tele požiadavky 
		.then((res) => res.blob()) // Dostali sme binárne dáta (blob)
		.then((image) => {
			document.querySelector("#output").src = URL.createObjectURL(image); // Nastavíme src našeho <img> na načítaný obrázok
		})
	/*setTimeout(function(){
		scroll("output")
	}, 3000);*/
}

document.querySelector("#option_panel").addEventListener("submit", get_graph);
