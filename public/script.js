// handleSubmit je funkcia, ktorá sa spustí keď sa bude mať odoslať náš formulár
function handleSubmit(e) {
	e.preventDefault(); // zabrániť vstavenému odosielaniu v prehliadači

	// this reprezentuje ten formular, ktory odosielame
	const x1 = this.querySelector("#x1").value;
	const y1 = this.querySelector("#y1").value;
	const z1 = this.querySelector("#z1").value;
	const r1 = this.querySelector("#r1").value;

	const x2 = this.querySelector("#x2").value;
	const y2 = this.querySelector("#y2").value;
	const z2 = this.querySelector("#z2").value;
	const r2 = this.querySelector("#r2").value;

	const x3 = this.querySelector("#x3").value;
	const y3 = this.querySelector("#y3").value;
	const z3 = this.querySelector("#z3").value;
	const r3 = this.querySelector("#r3").value;

	const formular = new URLSearchParams();

	formular.append('x1', x1);
	formular.append('y1', y1);
	formular.append('z1', z1);
	formular.append('r1', r1);

	formular.append('x2', x2);
	formular.append('y2', y2);
	formular.append('z2', z2);
	formular.append('r2', r2);

	formular.append('x3', x3);
	formular.append('y3', y3);
	formular.append('z3', z3);
	formular.append('r3', r3);

	const url = this.action; // Nacitame povodnu URL zadanu vo formulari
	const method = this.method; // NAcitame povodnu metodu zadanu vo formulari
	fetch(url, {method: method, body: formular}) // Urobíme HTTP požiadavku na náš server POST /render a formularom v tele požiadavky 
		.then((res) => res.blob())
		.then((solution) => {
			prom = solution.text()

			prom.then(
				function(result){
					document.querySelector("#output").textContent = result;
			})
		})
}


document.querySelector("#eq_system").addEventListener("submit", handleSubmit);