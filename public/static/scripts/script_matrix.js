

function handleSubmit(e) {

	e.preventDefault();

	const formular = new URLSearchParams();

	const url = this.action; // Nacitame povodnu URL zadanu vo formulari
	const method = this.method; // NAcitame povodnu metodu zadanu vo formulari

	fetch(url, {method: method, body: formular}) // Urobíme HTTP požiadavku na náš server POST /render a formularom v tele požiadavky 
		.then((res) => res.json())
		.then((data) => {
			document.querySelector("#m1").innerHTML = data["m1"]
			document.querySelector("#m2").innerHTML = data["m2"]
		})
}


document.querySelector("#get_matrix_form").addEventListener("submit", handleSubmit);