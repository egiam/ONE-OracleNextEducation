const deleteIcon = () => {
    const i = document.createElement("i"); // create an icon
    i.classList.add("fas", "fa-trash-alt", "trashIcon", "icon"); // Agrega clases a i
    i.addEventListener("click", deleteTask); // Agrega un evento a i
    return i;
};

const deleteTask = (event) => {
    const parent = event.target.parentElement; // parent is the li
    parent.remove(); // remove the li
};

export default deleteIcon; // export the function