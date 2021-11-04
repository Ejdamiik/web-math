
function replaceLineBreaksWithHTML(string) {
 return string !== undefined ? string.replace(/\n/g, '<br/>') : "";
}


// handleSubmit je funkcia, ktorá sa spustí keď sa bude mať odoslať náš formulár
function handleSubmit(e) {

	e.preventDefault(); // zabrániť vstavenému odosielaniu v prehliadači

	// this reprezentuje ten formular, ktory odosielame
	const base = this.querySelector("#base_entry").value;
	const relation = this.querySelector("#relation_entry").value;

	const formular = new URLSearchParams();


	formular.append('base', base);
	formular.append('relation', relation);

	const url = this.action; // Nacitame povodnu URL zadanu vo formulari
	const method = this.method; // NAcitame povodnu metodu zadanu vo formulari

	fetch(url, {method: method, body: formular}) // Urobíme HTTP požiadavku na náš server POST /render a formularom v tele požiadavky 
		.then((res) => res.blob())
		.then((solution) => {
			prom = solution.text()

			prom.then(
				function(result){

					const converted = replaceLineBreaksWithHTML(result);
					document.querySelector("#output").innerHTML = converted;
			})
		})
}


document.querySelector("#relations_form").addEventListener("submit", handleSubmit);