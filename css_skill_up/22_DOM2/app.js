let div = document.querySelectorAll("div");
console.log(div)

for(let i = 0; i < div.length; i++){
	div[i].addEventListener("click", function(){
		div[i].style.backgroundColor = "blue"
	})
}
