const pattern_curp = /^[A-Z]{4}[0-9]{6}[A-Z]{6}[A-Z0-9]{2}?$/;
const pattern_tel = /^[0-9]{10}?$/;
const pattern_correo = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}?$/;

function generarNombreCompleto(nombre, paterno, materno) {
    if (!materno) {
        return `${nombre} ${paterno}`;
    }
    let materno_completo = materno.trim().toLowerCase();
    if (materno_completo === 'X' || materno_completo === 'x' || materno_completo === 'none' || materno_completo === '') {
        return `${nombre} ${paterno}`;
    }
    return `${nombre} ${paterno} ${materno}`;
}

function valida_forma() {
    let js_nc = getTextInputById("f_nc");
    let js_curp = getTextInputById("f_curp");
    let js_nombre = getTextInputById("f_nombre");
    let js_paterno = getTextInputById("f_paterno");
    let js_materno = getTextInputById("f_materno");
    let js_tel = getTextInputById("f_telefono");
    let js_cel = getTextInputById("f_celular");
    let js_correo = getTextInputById("f_correo");
    let js_nivel = document.getElementById("f_nivel").value;
    let js_mun = document.getElementById("f_mun").value;
    let js_asunto = document.getElementById("f_asunto").value;

    // Generar nombre completo usando la lógica de Python
    let generated_nc = generarNombreCompleto(js_nombre, js_paterno, js_materno);

    if (js_nc.length <= 0) {
        mensaje('warning', 'NOMBRE', 'El dato Nombre no puede ir vacío!', '<a href="">Necesitas ayuda?</a>');
        return false;
    } else if (js_nc.length < 6) {
        mensaje('error', 'ERROR: NOMBRE', 'El dato Nombre debe tener al menos 6 caracteres. Ejemplo: Sue Kim', '<a href="">Necesitas ayuda?</a>');
        return false;
    } 
    
    else if (js_curp.length <= 0) {
        mensaje('warning', 'CURP', 'Olvido escribir el CURP!', '<a href="">Necesitas ayuda?</a>');
        return false;
    } else if (!pattern_curp.test(js_curp)) {
        mensaje('error', 'ERROR: CURP', 'El dato CURP no cumple con los requisitos! Ejemplo: LATA011228MCLLRZA2', '<a href="">Necesitas ayuda?</a>');
        return false;
    } 
    
    if (js_nombre.length <= 0) {
        mensaje('warning', 'NOMBRE', 'Olvido escribir el nombre!', '<a href="">Necesitas ayuda?</a>');
        return false;
    } else if (js_nombre.length < 3) {
        mensaje('error', 'ERROR: NOMBRE', 'El nombre debe tener al menos 3 caracteres!', '<a href="">Necesitas ayuda?</a>');
        return false;
    } 
    
    if (js_paterno.length <= 0) {
        mensaje('warning', 'APELLIDO PATERNO', 'Olvido escribir el Apellido Paterno!', '<a href="">Necesitas ayuda?</a>');
        return false;
    } else if (js_paterno.length < 3) {
        mensaje('error', 'ERROR: APELLIDO PATERNO', 'El Apellido Paterno debe tener al menos 3 caracteres!', '<a href="">Necesitas ayuda?</a>');
        return false;
    } 
    
    if (js_materno.length <= 0) {
        mensaje('warning', 'APELLIDO MATERNO', 'Olvido escribir el Apellido Materno!', '<a href="">Necesitas ayuda?</a>');
        return false;
    } else if (js_materno.length <1) {
        mensaje('error', 'ERROR: APELLIDO MATERNO', 'El Apellido Materno debe tener al menos 3 caracteres! Error: en caso de no tener apellido materno escribir X', '<a href="">Necesitas ayuda?</a>');
        return false;
    } 

    else if (js_nc !== generated_nc) {
        mensaje('error', 'ERROR: NOMBRE COMPLETO', 'El Nombre Completo no coincide con los campos Nombre, Apellido Paterno y Apellido Materno!', '<a href="">Necesitas ayuda?</a>');
        return false;
    }
    
    if (js_tel.length <= 0) {
        mensaje('warning', 'TELÉFONO', 'Olvido escribir el Teléfono!', '<a href="">Necesitas ayuda?</a>');
        return false;
    } else if (!pattern_tel.test(js_tel)) {
        mensaje('error', 'ERROR: TELÉFONO', 'El Teléfono debe tener 10 dígitos numéricos!', '<a href="">Necesitas ayuda?</a>');
        return false;
    } 
    
    if (js_cel.length <= 0) {
        mensaje('warning', 'CELULAR', 'Olvido escribir el Celular!', '<a href="">Necesitas ayuda?</a>');
        return false;
    } else if (!pattern_tel.test(js_cel)) {
        mensaje('error', 'ERROR: CELULAR', 'El Celular debe tener 10 dígitos numéricos!', '<a href="">Necesitas ayuda?</a>');
        return false;
    } 
    
    if (js_correo.length <= 0) {
        mensaje('warning', 'CORREO', 'Olvido escribir el Correo!', '<a href="">Necesitas ayuda?</a>');
        return false;
    } else if (!pattern_correo.test(js_correo)) {
        mensaje('error', 'ERROR: CORREO', 'El Correo debe tener un formato válido! Ejemplo: azul@gmail.com', '<a href="">Necesitas ayuda?</a>');
        return false;
    } 
    
    if (js_nivel == "0") {
        mensaje('warning', 'NIVEL DEL CURSO', 'Olvido seleccionar el Nivel del Curso!', '<a href="">Necesitas ayuda?</a>');
        return false;
    } 
    
    if (js_mun == "0") {
        mensaje('warning', 'MUNICIPIO', 'Olvido seleccionar el Municipio!', '<a href="">Necesitas ayuda?</a>');
        return false;
    } 
    
    if (js_asunto == "0") {
        mensaje('warning', 'ASUNTO', 'Olvido seleccionar el Asunto!', '<a href="">Necesitas ayuda?</a>');
        return false;
    }
    
}

function getTextInputById(id) {
    return document.getElementById(id).value.trim();
}

function mensaje(tipo, titulo, texto, footer) {
    Swal.fire({
        icon: tipo,
        title: titulo,
        text: texto,
        footer: footer
    });
}
