const button = document.getElementById("button");
const answer = document.getElementById("answer");

button.addEventListener("click", () => {
    button.style.color = "darkblue";
    button.style.textShadow = "0px 1px black";
    button.style.transitionDuration = "1s";
});

button.addEventListener("dblclick", () => {
    answer.style.transform = "translateX(0px)";
    answer.style.transitionDuration = "1s";
});