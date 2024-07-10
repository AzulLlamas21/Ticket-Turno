const pattern_tel = /^[0-9]{10}?$/;

function valida_forma() {
    let js_nc = getTextInputById("f_nc");
    let js_curp = getTextInputById("f_curp");

    if (js_nc.length <= 0) {
        mensaje('warning', 'NOMBRE', 'El dato Nombre no puede ir vacío!', '<a href="">Necesitas ayuda?</a>');
        return false;
    } 
    
    else if (js_nc.length < 6) {
        mensaje('error', 'ERROR: NOMBRE', 'El dato Nombre debe tener al menos 6 caracteres. Ejemplo: Sue Kim', '<a href="">Necesitas ayuda?</a>');
        return false;
    } 
    
    if (js_curp.length <= 0) {
        mensaje('warning', 'CURP', 'Olvido escribir el CURP!', '<a href="">Necesitas ayuda?</a>');
        return false;
    } 
    
    else if (!pattern_curp.test(js_curp)) {
        mensaje('error', 'ERROR: CURP', 'El dato CURP no cumple con los requisitos! Ejemplo: LATA011228MCLLRZA2', '<a href="">Necesitas ayuda?</a>');
        return false;
    } 

    let data = {
        nc: js_nc,
        curp: js_curp
    };

    fetch('/generar_ticket', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data)
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Error en la solicitud');
        }
        return response.text(); // Cambia a text() porque estamos redirigiendo
    })
    .then(result => {
        console.log(result);
        // Redirecciona directamente a la página de ticket
        let url = new URL('/ticket', window.location.origin);
        Object.keys(data).forEach(key => url.searchParams.append(key, data[key]));
        window.location.href = url;
    })
    .catch(error => {
        console.error('Error:', error);
    });
    

    return false; 
}

let getTextInputById = (id) => {
    return document.getElementById(id).value.trim();
}

let mensaje = (tipo, titulo, texto, liga) => {
    Swal.fire({
        icon: tipo,
        title: titulo,
        text: texto,
        footer: liga
    });
}