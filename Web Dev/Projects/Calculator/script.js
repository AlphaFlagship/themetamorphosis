var placeMultiplier= 1;
var number1= 0;
let test=0;
let result;
let firstNumber;
let flag =0;
let flag1 =0; 
function allclear() {
    let step = document.getElementById("steps");
    step.innerHTML = `0`;
    number1 =0;
    test =0;
    firstNumber =0;
    flag =0;   
}
function input(value)
{
    let number= document.getElementById("steps")
    let enter = value ;
    number1 = enter + number1*10;
    console.log(number1);
    number.innerHTML += enter;
    if (test !=0) {
        flag =1;
    }
}
function add() {
    let step = document.getElementById("steps");
    if(test == 0){
        let step = document.getElementById("steps");
        test =1;
        step.innerHTML+= `+`;
        const temp1 = number1;
        firstNumber = temp1;
        console.log(number1);
        number1 = 0;
    }
    
    if (test != 0) {
        const temp1 = firstNumber;
        let x = document.getElementById("steps").textContent;
        var textString =  x;
        textString = textString.toString();
        let newtextString=textString.slice(0,-1);
        console.log(newtextString);
        steps.innerHTML = newtextString;
        test =1;
        step.innerHTML+= `+`;
        firstNumber = temp1;
        number1 = 0;
    }
    
}
function product() {
    let step = document.getElementById("steps");
    if(test == 0){
        let step = document.getElementById("steps");
        test =2;
        step.innerHTML+= `*`;
        const temp1 = number1;
        firstNumber = temp1;
        console.log(number1);
        number1 = 0;
    }
    
    if (test != 0) {
        const temp1 = firstNumber;
        let x = document.getElementById("steps").textContent;
        var textString =  x;
        textString = textString.toString();
        let newtextString=textString.slice(0,-1);
        console.log(newtextString);
        steps.innerHTML = newtextString;
        test =2;
        step.innerHTML+= `*`;
        firstNumber = temp1;
        number1 = 0;
    }
}
function divide() {let step = document.getElementById("steps");
if(test == 0){
    let step = document.getElementById("steps");
    test =3;
    step.innerHTML+= `/`;
    const temp1 = number1;
    firstNumber = temp1;
    console.log(number1);
    number1 = 0;
}

if (test != 0) {
    const temp1 = firstNumber;
    let x = document.getElementById("steps").textContent;
    var textString =  x;
    textString = textString.toString();
    let newtextString=textString.slice(0,-1);
    console.log(newtextString);
    steps.innerHTML = newtextString;
    test =3;
    step.innerHTML+= `/`;
    firstNumber = temp1;
    number1 = 0;
}
}
function substract() {let step = document.getElementById("steps");
if(test == 0){
    let step = document.getElementById("steps");
    test =4;
    step.innerHTML+= `-`;
    const temp1 = number1;
    firstNumber = temp1;
    console.log(number1);
    number1 = 0;
}

if (test != 0) {
    const temp1 = firstNumber;
    let x = document.getElementById("steps").textContent;
    var textString =  x;
    textString = textString.toString();
    let newtextString=textString.slice(0,-1);
    console.log(newtextString);
    steps.innerHTML = newtextString;
    test =4;
    step.innerHTML+= `-`;
    firstNumber = temp1;
    number1 = 0;
}
}
function negative() {
    let step = document.getElementById("steps")
    test =1;
    step.innerHTML+= `+`;
}
function calculate() {
    if (test ==1) {
        result=firstNumber+number1;
        let solved = document.getElementById("result");
        solved.innerHTML=result;
    }
    else if (test ==2) {
        result=firstNumber*number1;
        let solved = document.getElementById("result");
        solved.innerHTML=result;
    }
    else if (test ==3) {
        result=firstNumber/number1;
        let solved = document.getElementById("result");
        solved.innerHTML=result;
    }
    else if (test ==4) {
        result=firstNumber-number1;
        let solved = document.getElementById("result");
        solved.innerHTML=result;
    }
}
function clear() {
    if (test ==0 && flag ==0 ) {
        
    }
}
