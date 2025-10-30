const rollBtn = document.getElementById("rollDice");
const dice = document.getElementById("dice");
const diceHistoryEl = document.getElementById("rollHistory");


let diceHistory = [];

function rollDice() {
    let rollRes = Math.floor(Math.random() * 6) + 1;
    let face = changeDiceFace(rollRes)

    dice.innerHTML = face;

    diceHistory.push(rollRes);

    updateHistroy();
}

function updateHistroy(){
    diceHistoryEl.innerHTML = "";

    for(let i = 0; i < diceHistory.length; i++){
        const listEl = document.createElement("li");
        listEl.innerHTML = `Roll ${i + 1}: <span>${changeDiceFace(diceHistory[i])}</span>`;
        diceHistoryEl.appendChild(listEl);
    }
}

function changeDiceFace(rollRes){
    switch(rollRes){
        case 1:
            return "&#9856;";
        case 2:
            return "&#9857;";
        case 3:
            return "&#9858;";
        case 4:
            return "&#9859";
        case 5:
            return "&#9860;";
        case 6:
            return "&#9861;";
        default:
            return "";
    }
}

rollBtn.addEventListener("click", ()=> {
    dice.classList.add("rollAnimation");

    setTimeout(() => {
        dice.classList.remove("rollAnimation");
        rollDice();
    }, 1000);


})