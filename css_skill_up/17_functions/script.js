function calcAge(age){
    return 2020 - age
}

function yearsUntilRetirement(year, userName){
    let age = calcAge(year);
    let retirement = 60 - age;
    if (retirement>0){
        console.log(`${userName} will retire in ${retirement} years.`)
    } else{
        console.log(`${userName} already on the retirement.`)
    }
}
yearsUntilRetirement(1980, 'Ivan');
console.log(calcAge(1980))


let user = {
    name:"Vova",
    age:20,
    fullName:"Kozak",
    isChecked:true,
    hi:function(){
        console.log(this)
        console.log("Hi " + this.name)
    }
}

// user.hi()
let ivan = {
    name:"Vova",
}

ivan.hi = user.hi;
ivan.hi()

for (i=10; i>0;i--){
    console.log(i)
}
