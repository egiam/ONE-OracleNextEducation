const listaClientes = () =>
    fetch("http://localhost:3000/perfil").then((respuesta) => respuesta.json()); // Esto hace que se pueda exportar a otros archivos para poder usarlo(?)

const crearCliente = (nombre, email) => {
    return fetch("http://localhost:3000/perfil", {
        // Esto es para crear un nuevo cliente
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ nombre, email, id: uuid.v4() }), // JSON stringify convierte un objeto a un string
    });
};

const eliminarCliente = (id) => {
    return fetch(`http://localhost:3000/perfil/${id}`, {
        method: "DELETE",
    });
};

const detalleCliente = (id) => {
    return fetch(`http://localhost:3000/perfil/${id}`).then((respuesta) =>
        respuesta.json()
    );
};

const actualizarCliente = (nombre, email, id) => {
    return fetch(`http://localhost:3000/perfil/${id}`, {
            method: "PUT",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({ nombre, email }), // JSON stringify convierte un objeto a un string
        })
        .then((respuesta) => respuesta) // Esto es para devolver la respuesta
        .catch((err) => console.log(err)); // Esto es para que si hay un error, lo muestre en la consola
};

export const clientServices = {
    listaClientes,
    crearCliente,
    eliminarCliente,
    detalleCliente,
    actualizarCliente,
};