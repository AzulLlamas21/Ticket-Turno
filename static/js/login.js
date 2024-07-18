document.getElementById('login').addEventListener('submit', function(event) {
    event.preventDefault(); 

    let usuario = document.getElementById('f_user').value.trim();
    let contrasena = document.getElementById('f_pwd').value.trim();
    let hcaptchaResponse = document.querySelector('.h-captcha [name="h-captcha-response"]').value;

    if (usuario.length === 0 || contrasena.length === 0) {
        mensaje('warning', 'Campos Vacíos', 'Por favor complete todos los campos.', '<a href="">Necesitas ayuda?</a>');
        return false;
    }

    if (hcaptchaResponse.length === 0) {
        mensaje('warning', 'Captcha', 'Por favor complete el captcha.', '<a href="">Necesitas ayuda?</a>');
        return false;
    }

    fetch('/login', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({f_user: usuario, f_pwd: contrasena, 'h-captcha-response': hcaptchaResponse})
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.json();
    })
    .then(data => {
        if (data.redirect) {
            window.location.href = data.redirect;
        } else {
            mensaje('error', 'Error', data.message, '<a href="">Necesitas ayuda?</a>');
        }
    })
    .catch(error => {
        console.error('Error:', error);
        mensaje('error', 'Error de Conexión', 'Hubo un problema al intentar iniciar sesión.', '');
    });
});

function mensaje(tipo, titulo, texto, liga) {
    Swal.fire({
        icon: tipo,
        title: titulo,
        text: texto,
        footer: liga
    });
}
