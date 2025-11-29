


document.addEventListener("DOMContentLoaded", function(e) {
let button1 = document.getElementById("button1");
    let button2 = document.getElementById("button2");
    let button3 = document.getElementById("button3");
    let button4 = document.getElementById("button4");
    let button5 = document.getElementById("button5");
    let button6 = document.getElementById("button6");
    button1.addEventListener("click", player1);
    button2.addEventListener("click", player1);
    button3.addEventListener("click", player1);
    button4.addEventListener("click", player2);
    button5.addEventListener("click", player2);
    button6.addEventListener("click", player2);

});


function player1(e){
    console.log(e);
    if (e.target.id == "button1"){
        audio2 = new Audio('audio/Бетховен. Музыка.mp3');
        audio1 = new Audio('audio/Хамелеон 1.mp3');
        audio1.play();
        audio2.play();

    }

    if (e.target.id == "button2"){

    audio1 = new Audio('audio/Хамелеон 2.mp3')
    audio2 = new Audio('audio/Бах. Музыка.mp3')
    audio3 = new Audio ('audio/Азбука морзе 2.mp3')
    audio1.play();
    audio2.play();
    audio3.play();
    }

    if (e.target.id == "button3"){
     audio2 = new Audio('audio/Чайковский. Музыка.mp3')
    audio1 = new Audio('audio/Хамелеон 3.mp3')
    audio3 = new Audio ('audio/Азбука морзе 3.mp3')
    audio1.play();
    audio2.play();
    audio3.play();
    }
}

function player2(e){
    if (e.target.id == "button4"){
        audio1.pause();
        audio2.pause();
    }

    if(e.target.id == "button5"){
        audio1.pause();
        audio2.pause();
        audio3.pause();
    }

    if(e.target.id == "button6"){
        audio1.pause();
        audio2.pause();
        audio3.pause();
    }
}