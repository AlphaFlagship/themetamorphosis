let compScore =0;
let yourScore =0;
function yourChoice(value){
    let input = document.getElementById("input");
    let text = "You chose : ";
    if(value==1) text += "ROCK";
    if(value==2) text += "PAPER";
    if(value==3) text += "SCISSORS";
    var enter = value;
    input.innerHTML = text;

    let comp = document.getElementById("comp");
    let text1 = "Computer chose : ";
    var num = Math.floor(Math.random()*3+1);
    if(num==1) text1 += "ROCK";
    if(num==2) text1 += "PAPER";
    if(num==3) text1 += "SCISSORS";
    comp.innerHTML = text1;

    let out = document.getElementById("result");
    let text2 = "";
    if (enter==num) {
        text2 = "Both TIED";
    }
    else if (enter == 1 && num == 2) {
        text2 = "Computer WON";
        compScore++;
    }
    else if (enter == 1 && num ==3) {
        text2 = "You WIN. Yaayyyyyy!!";
        yourScore++;
    }
    else if (enter == 2 && num == 3) {
        text2 = "Computer WON";
        compScore++;
    }
    else if (enter == 2 && num ==1) {
        text2 = "You WIN. Yaayyyyyy!!";
        yourScore++;
    }
    else if (enter == 3 && num == 1) {
        text2 = "Computer WON";
        compScore++;
    }
    else if (enter == 3 && num ==2) {
        text2 = "You WIN. Yaayyyyyy!!";
        yourScore++;
    }
    out.innerHTML = text2;
    let abc = document.getElementById("myScore");
    let mytext = "PC Score ";
    abc.innerHTML = `PC Score `+ compScore;
    let xyz = document.getElementById("yourScore");
    let yourtext = "Your Score ";
    xyz.innerHTML = `Your Score `+ yourScore;

    if (compScore == 5) {
        alert("Computer WON a set. Game will now Reset");
        compScore =0;
        yourScore =0;
    }
    if (yourScore==5){
        alert("You WON a set. Game will now Reset");
        yourScore = 0;
        compScore =0;
    }
}