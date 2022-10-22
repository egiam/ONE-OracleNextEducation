const checkComplete = () => {
    const i = document.createElement("i"); // create an icon
    i.classList.add("far", "fa-check-square", "icon"); // Agrega clases a i
    i.addEventListener("click", completeTask); // Agrega un evento a i
    return i;
};
// Immediately invoked function expression IIFE
const completeTask = (event) => {
    const element = event.target; // element is the icon
    element.classList.toggle("fas"); // toggle the class fas
    element.classList.toggle("completeIcon"); // toggle the class completeIcon
    element.classList.toggle("far"); // toggle the class far
};

export default checkComplete; // export the function