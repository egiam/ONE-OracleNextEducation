import checkComplete from "./components/checkComplete.js";
import deleteIcon from "./components/deleteIcon.js";

const btn = document.querySelector("[data-form-btn]"); // Selecciona el elemento con el atributo data-form-btn

const createTask = (evento) => {
    evento.preventDefault(); // Evita que el formulario se envíe
    const input = document.querySelector("[data-form-input]"); // Selecciona el elemento con el atributo data-form-input
    const value = input.value; // Obtiene el valor del input
    const list = document.querySelector("[data-list]"); // Selecciona el elemento con el atributo data-list
    const task = document.createElement("li"); // Crea un elemento li
    task.classList.add("card"); // Agrega la clase card al elemento li
    input.value = "";
    //backticks
    const taskContent = document.createElement("div"); // Crea un elemento div

    const titleTask = document.createElement("span"); // Crea un elemento span
    titleTask.classList.add("task"); // Agrega la clase task al elemento span
    titleTask.innerText = value; // Agrega el valor del input al elemento span
    taskContent.appendChild(checkComplete()); // Agrega el elemento i al elemento div
    taskContent.appendChild(titleTask); // Agrega el elemento span al elemento div
    // task.innerHTML = content;

    task.appendChild(taskContent); // Agrega el elemento div al elemento li
    task.appendChild(deleteIcon()); // Agrega el elemento i al elemento li
    list.appendChild(task); // Agrega el elemento li al elemento ul
};

//Arrow functions o funciones anonimas
btn.addEventListener("click", createTask); // Agrega un evento al elemento btn