let minutes = 0;
let seconds = 0;
let milliseconds = 0;
let timerId = null;
let display = null;

function formatTime() {
  const m = String(minutes).padStart(2, '0');
  const s = String(seconds).padStart(2, '0');
  return `${m}:${s}`;
}

function updateDisplay() {
  display.textContent = formatTime();
}

function tick() {
  milliseconds += 10;

  if (milliseconds >= 1000) {
    milliseconds = 0;
    seconds++;

    if (seconds >= 60) {
      seconds = 0;
      minutes++;
    }
  }

  updateDisplay();
}

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

    display = document.getElementById('display');
    timerId = setInterval(tick, 10);
    var shulteTable =
      document.getElementsByClassName("shulte_table")[0];
    var numsArray = [];
    for (var i = 1; i < 26; i++){
      numsArray.push(i);
    }
    numsArray.sort(() => 0.5 - Math.random())

    for (var i = 0; i < 25; i++){
      var newElement = document.createElement("div");
      newElement.setAttribute("class", "number");
      newElement.setAttribute("id", numsArray[i]);
      newElement.innerText = numsArray[i];
      shulteTable.append(newElement);
      newElement.addEventListener("click", touchFunction);
    }


});

function touchFunction(e){
    console.log(e.target.innerText);
    if (button_to_press == e.target.id){
        e.target.style.backgroundColor = 'green';
        }
        if (e.target.id == 25){
            clearInterval(timerId);
        }



}

function player1(e){
    console.log(e);
    if (e.target.id == "button1"){
        let audio2 = new Audio('audio/Lyudvig_van_Betkhoven_-_Symphony_No_5_48271065.mp3');
        let audio1 = new Audio('audio/Anton_CHekhov_-_KHameleon_72057283.mp3');
    }
    audio1.play();
    audio2.play();

}

function player2(e){


}




