// handleSubmit je funkcia, ktorá sa spustí keď sa bude mať odoslať náš formulár
function handleSubmit(e) {

	e.preventDefault(); // zabrániť vstavenému odosielaniu v prehliadači

	console.log("Sent");
}


document.querySelector("#Linear_system").addEventListener("submit", handleSubmit);