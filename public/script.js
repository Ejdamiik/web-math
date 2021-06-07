// handleSubmit je funkcia, ktorá sa spustí keď sa bude mať odoslať náš formulár
function handleSubmit(e) {
	e.preventDefault(); // zabrániť vstavenému odosielaniu v prehliadači

	// this reprezentuje ten formular, ktory odosielame
	const equation = this.querySelector("#equation_text").value; // Načítame text z textarea

	const url = this.action; // Nacitame povodnu URL zadanu vo formulari
	const method = this.method; // NAcitame povodnu metodu zadanu vo formulari
	fetch(url, {method: method, body: equation}) // Urobíme HTTP požiadavku na náš server POST /render a formularom v tele požiadavky 
		.then((res) => res.blob()) // Dostali sme binárne dáta (blob)
}


function pressed_x(){
	let val = document.querySelector("#equation_text").value;
	document.querySelector("#equation_text").value = val + "x";
}

function pressed_y(){
	let val = document.querySelector("#equation_text").value;
	document.querySelector("#equation_text").value = val + "y";
}

function pressed_z(){
	let val = document.querySelector("#equation_text").value;
	document.querySelector("#equation_text").value = val + "z";
}

function pressed_0(){
	let val = document.querySelector("#equation_text").value;
	document.querySelector("#equation_text").value = val + "0";
}

function pressed_1(){
	let val = document.querySelector("#equation_text").value;
	document.querySelector("#equation_text").value = val + "1";
}

function pressed_2(){
	let val = document.querySelector("#equation_text").value;
	document.querySelector("#equation_text").value = val + "2";
}

function pressed_3(){
	let val = document.querySelector("#equation_text").value;
	document.querySelector("#equation_text").value = val + "3";
}

function pressed_4(){
	let val = document.querySelector("#equation_text").value;
	document.querySelector("#equation_text").value = val + "4";
}

function pressed_5(){
	let val = document.querySelector("#equation_text").value;
	document.querySelector("#equation_text").value = val + "5";
}

function pressed_6(){
	let val = document.querySelector("#equation_text").value;
	document.querySelector("#equation_text").value = val + "6";
}

function pressed_7(){
	let val = document.querySelector("#equation_text").value;
	document.querySelector("#equation_text").value = val + "7";
}

function pressed_8(){
	let val = document.querySelector("#equation_text").value;
	document.querySelector("#equation_text").value = val + "8";
}

function pressed_9(){
	let val = document.querySelector("#equation_text").value;
	document.querySelector("#equation_text").value = val + "9";
}

function pressed_plus(){
	let val = document.querySelector("#equation_text").value;
	document.querySelector("#equation_text").value = val + "+";
}

function pressed_minus(){
	let val = document.querySelector("#equation_text").value;
	document.querySelector("#equation_text").value = val + "-";
}

function pressed_multiply(){
	let val = document.querySelector("#equation_text").value;
	document.querySelector("#equation_text").value = val + "*";
}

function pressed_divide(){
	let val = document.querySelector("#equation_text").value;
	document.querySelector("#equation_text").value = val + ":";
}

function pressed_equal(){
	let val = document.querySelector("#equation_text").value;
	document.querySelector("#equation_text").value = val + " = ";
}

function pressed_left(){
	let val = document.querySelector("#equation_text").value;
	document.querySelector("#equation_text").value = val + "(";
}

function pressed_right(){
	let val = document.querySelector("#equation_text").value;
	document.querySelector("#equation_text").value = val + ")";
}


document.querySelector("#x").addEventListener("click", pressed_x);
document.querySelector("#y").addEventListener("click", pressed_y);
document.querySelector("#z").addEventListener("click", pressed_z);

document.querySelector("#one").addEventListener("click", pressed_1);
document.querySelector("#two").addEventListener("click", pressed_2);
document.querySelector("#three").addEventListener("click", pressed_3);
document.querySelector("#four").addEventListener("click", pressed_4);
document.querySelector("#five").addEventListener("click", pressed_5);
document.querySelector("#six").addEventListener("click", pressed_6);
document.querySelector("#seven").addEventListener("click", pressed_7);
document.querySelector("#eight").addEventListener("click", pressed_8);
document.querySelector("#nine").addEventListener("click", pressed_9);
document.querySelector("#zero").addEventListener("click", pressed_0);

document.querySelector("#plus").addEventListener("click", pressed_plus);
document.querySelector("#minus").addEventListener("click", pressed_minus);
document.querySelector("#divide").addEventListener("click", pressed_divide);
document.querySelector("#multiply").addEventListener("click", pressed_multiply);

document.querySelector("#equal").addEventListener("click", pressed_equal);

document.querySelector("#lp").addEventListener("click", pressed_left);
document.querySelector("#rp").addEventListener("click", pressed_right);

document.querySelector("submit").addEventListener("submit", handleSubmit);
