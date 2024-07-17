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

document.getElementById("buscarBtn").addEventListener("click", function() {
    let searchInput = document.getElementById("buscar").value.trim();
    if (searchInput === "") {
        mensaje('error', 'Campo de Búsqueda Vacío', 'Ingrese un nombre completo o CURP para buscar.', '');
    } else {
        buscarFormulario(searchInput);
    }
});

function buscarFormulario(buscarTerm) {
    fetch(`/buscar_formulario?term=${buscarTerm}`)
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const formData = data.formulario;
                document.getElementById("f_nc").value = formData.nombre_completo;
                document.getElementById("f_curp").value = formData.curp;
                document.getElementById("f_nombre").value = formData.nombre;
                document.getElementById("f_paterno").value = formData.paterno;
                document.getElementById("f_materno").value = formData.materno;
                document.getElementById("f_telefono").value = formData.telefono;
                document.getElementById("f_celular").value = formData.celular;
                document.getElementById("f_correo").value = formData.correo;
                document.getElementById("f_nivel").value = formData.id_nivel;
                document.getElementById("f_mun").value = formData.id_mun;
                document.getElementById("f_asunto").value = formData.id_asunto;

                document.getElementById("update-delete-buttons").style.display = "block";
            } else {
                mensaje('error', 'No Encontrado', 'No se encontró ningún formulario con los datos ingresados.', '');
            }
        })
        .catch(error => console.error('Error:', error));
}


// Función para buscar un formulario por CURP o no_turno
function buscarFormulario() {
    const query = document.getElementById('buscar').value.trim();
    if (query !== '') {
        fetch(`/buscar_formulario?query=${query}`)
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Mostrar los datos del formulario en los campos correspondientes
                    const formulario = data.formulario;
                    document.getElementById('f_nc').value = formulario.nombre_completo;
                    document.getElementById('f_curp').value = formulario.curp;
                    document.getElementById('f_nombre').value = formulario.nombre;
                    document.getElementById('f_paterno').value = formulario.paterno;
                    document.getElementById('f_materno').value = formulario.materno;
                    document.getElementById('f_telefono').value = formulario.telefono;
                    document.getElementById('f_celular').value = formulario.celular;
                    document.getElementById('f_correo').value = formulario.correo;
                    document.getElementById('f_nivel').value = formulario.id_nivel;
                    document.getElementById('f_mun').value = formulario.id_mun;
                    document.getElementById('f_asunto').value = formulario.id_asunto;

                    // Mostrar botones de actualizar y eliminar
                    document.getElementById('update-delete-buttons').style.display = 'block';
                } else {
                    // Mostrar mensaje de error si no se encuentra el formulario
                    Swal.fire({
                        icon: 'error',
                        title: 'Error',
                        text: 'No se encontró ningún formulario con el CURP o no_turno proporcionado.',
                    });
                }
            })
            .catch(error => {
                console.error('Error:', error);
            });
    } else {
        // Mostrar mensaje de error si el campo de búsqueda está vacío
        Swal.fire({
            icon: 'error',
            title: 'Error',
            text: 'Por favor, ingrese un CURP o no_turno para buscar.',
        });
    }
}

// Función para actualizar un formulario
function actualizarFormulario() {
    const formData = {
        f_curp: document.getElementById('f_curp').value.trim(),
        f_nombre: document.getElementById('f_nombre').value.trim(),
        f_paterno: document.getElementById('f_paterno').value.trim(),
        f_materno: document.getElementById('f_materno').value.trim(),
        f_telefono: document.getElementById('f_telefono').value.trim(),
        f_celular: document.getElementById('f_celular').value.trim(),
        f_correo: document.getElementById('f_correo').value.trim(),
        f_nivel: document.getElementById('f_nivel').value,
        f_mun: document.getElementById('f_mun').value,
        f_asunto: document.getElementById('f_asunto').value,
    };

    fetch('/actualizar_formulario', {
        method: 'PUT',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    })
    .then(response => response.json())
    .then(data => {
        if (data.success) {
            // Mostrar mensaje de éxito y limpiar los campos
            Swal.fire({
                icon: 'success',
                title: 'Éxito',
                text: 'El formulario se actualizó correctamente.',
            });
            limpiarCampos();
        } else {
            // Mostrar mensaje de error si no se pudo actualizar el formulario
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'No se pudo actualizar el formulario.',
            });
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

// Función para limpiar los campos del formulario
function limpiarCampos() {
    document.getElementById('f_nc').value = '';
    document.getElementById('f_curp').value = '';
    document.getElementById('f_nombre').value = '';
    document.getElementById('f_paterno').value = '';
    document.getElementById('f_materno').value = '';
    document.getElementById('f_telefono').value = '';
    document.getElementById('f_celular').value = '';
    document.getElementById('f_correo').value = '';
    document.getElementById('f_nivel').value = '0';
    document.getElementById('f_mun').value = '0';
    document.getElementById('f_asunto').value = '0';
    document.getElementById('update-delete-buttons').style.display = 'none';
}

// Event listener para el botón de buscar
document.getElementById('buscarBtn').addEventListener('click', buscarFormulario);

// Event listener para el botón de actualizar
document.getElementById('btn_actualizar').addEventListener('click', actualizarFormulario);
