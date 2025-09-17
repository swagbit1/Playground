
const buttonsEl = document.querySelectorAll("button");
const inputFieldEl = document.querySelector(".result")

for (let i = 0; i < buttonsEl.length; i++) {

    buttonsEl[i].addEventListener("click", ()=>{
        const buttonElValues = buttonsEl[i].innerText

        if (buttonElValues === "C") {
            clearResult();
        } else if (buttonElValues === "="){
            calculate()
        } else if (buttonElValues === "X"){
            takeback()
        } else {
            appendValue(buttonElValues)
        }
    })
    
}

function clearResult(){
    const result = document.querySelector(".result")
    result.value = "";
}

function calculate() {
    inputFieldEl.value = eval(inputFieldEl.value)
}

function appendValue(value){
    inputFieldEl.value += value
}

function takeback(value){
    inputFieldEl.value = inputFieldEl.value.slice(0,-1)
}