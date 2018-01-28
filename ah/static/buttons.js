function buttonPresser(url){
	var request = new XMLHttpRequest();
	request.open("GET", url, true);
	request.send();
	console.log(url);
}