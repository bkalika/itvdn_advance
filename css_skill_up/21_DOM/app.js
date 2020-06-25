// console.log(document.body.parentElement)
// console.log(document.body.firstElementChild)
// console.log(last.previousElementSibling)
// console.log(document.body.lastElementChild)
// console.log(document.body.nextElementSibling)
// console.log(document.body.previousElementSibling)

// my version:
const last = document.body.lastElementChild
const ul = last.previousElementSibling
const li = ul.lastElementChild
const css = li.previousElementSibling
console.log(css)

// teacher version:
let ul2 = document.body.children[2].children[1];
console.log(ul2)

//student version:
console.log(document.body.lastElementChild.previousElementSibling.firstElementChild.nextElementSibling)


// 2
let li2 = document.getElementsByTagName("li");
console.log(li2)

console.log(document.getElementsByClassName("test"))

console.log(document.getElementById("text-id"))

console.log(document.querySelectorAll("ol li"))
console.log(document.querySelector("ol li"))

//3
document.querySelector("ol li").innerHTML = "change HTML"  
document.querySelector("ol li").textContent = "change HTML 2"  


let liFirst = document.querySelector("ol li");
console.log(liFirst);

console.log(liFirst.getAttribute("class"));
console.log(liFirst.hasAttribute("class"));

liFirst.setAttribute("class", "mul");
liFirst.removeAttribute("class");
console.log(liFirst);


// 4
let textId = document.querySelector("#text-id");

textId.onclick = function(){
	alert("Hello World!!!")
}
textId.onclick = function(){
	alert("Bye-Bye World!!!")
}



textId.addEventListener("click", function(){
	alert("Hello World!!!")
})

textId.addEventListener("click", function(){
	alert("Bye-Bye World!!!")
})

function hi(){
	alert("hello w 2")
}

textId.addEventListener("click", hi)

console.log(textId)


