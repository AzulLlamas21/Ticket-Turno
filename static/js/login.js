document.getElementById('login').addEventListener('submit', function(event) {
    let usuario = document.getElementById('f_user').value.trim();
    let contrasena = document.getElementById('f_pwd').value.trim();

    if (usuario.length <= 0) {
        mensaje('warning', 'Usuario', 'El campo de usuario no puede estar vacío.', '<a href="">Necesitas ayuda?</a>');
        event.preventDefault();
        return false;
    }

    if (contrasena.length <= 0) {
        mensaje('warning', 'Contraseña', 'El campo de contraseña no puede estar vacío.', '<a href="">Necesitas ayuda?</a>');
        event.preventDefault();
        return false;
    }
    
    // Validación básica del formulario
    if (usuario.length <= 0 || contrasena.length <= 0) {
        mensaje('warning', 'Campos vacíos', 'Por favor, complete todos los campos.', '<a href="">Necesitas ayuda?</a>');
        return false;
    }

    // Realiza la solicitud POST al servidor Flask para verificar las credenciales
    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({f_user: usuario, f_pwd: contrasena})
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Error en la solicitud');
        }
        return response.json();
    })
    .then(data => {
        if (data.redirect) {
            window.location.href = data.redirect;  // Redirige si las credenciales son correctas
        } else {
            mensaje('error', 'Error de inicio de sesión', data.message, '');  // Muestra mensaje de error si las credenciales son incorrectas
        }
    })
    .catch(error => {
        console.error('Error:', error);
        mensaje('error', 'Error de conexión', 'Hubo un problema al intentar iniciar sesión.', '');
    });       
    
    return true;
});

function mensaje(tipo, titulo, texto, liga) {
    Swal.fire({
        icon: tipo,
        title: titulo,
        text: texto,
        footer: liga
    });
}
