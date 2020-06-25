function trimString(str, maxlength){
   if(str.length > maxlength){
       let newMessage = str.substring(0, maxlength) + "...";
       alart(newMessage)
       // let ends = str.replace(str.substring(str.length - 3, str.length), "...")	
       // alert(str.length + " " + ends)
   }else{
       alert(str)
   }
}
let a = prompt("Enter your sentence:", "")
let b = +prompt("Enter available length:", "")
trimString(a, b)


// 2
function randomDigit(){
   let a = Math.floor(Math.random() * 100) + 1;
   if (a%2 == 0){
       alert(`Digit ${a} is even`)
   }else{
       alert(`digit ${a} is odd`)
   }
}

randomDigit()


// 3
function strToArray(){
    let a = prompt("input the numbers:", "")
    let b = prompt("input your favorite number:", "")
    let c = a.split(",");
    if (c.includes(b) || c.includes(" "+b)){
        alert("your number is here")
    }else{
        alert("your number is not here")
    }
}
strToArray()

// or 3
function strToArrayByFind(){
    let a = prompt("input the numbers:", "")
    let b = prompt("input your favorite number:", "")
    let c = a.split(",");
    let isTrue = c.find(function(el){
    	return el ===b 
    })
}
strToArrayByFind()
