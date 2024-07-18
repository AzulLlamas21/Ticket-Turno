/*BUSCAR FORMULARIO*/
function buscarFormulario() {
    const noTurno = document.getElementById('buscarNoTurno').value.trim();
    const curp = document.getElementById('buscarCurp').value.trim();

    if (noTurno === '' || curp === '') {
        Swal.fire({
            icon: 'error',
            title: 'Error',
            text: 'Por favor, escriba no_turno y CURP para poder buscar.',
        });
        return;
    }

    fetch(`/buscar_formulario?no_turno=${noTurno}&curp=${curp}`)
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                const formulario = data.formulario;
                document.getElementById('buscarNoTurno').disabled = true;
                document.getElementById('f_nc').value = formulario.nombre_completo;
                document.getElementById('f_curp').value = formulario.curp;
                document.getElementById('f_curp').disabled = true;
                document.getElementById('f_nombre').value = formulario.nombre;
                document.getElementById('f_paterno').value = formulario.paterno;
                document.getElementById('f_materno').value = formulario.materno;
                document.getElementById('f_telefono').value = formulario.telefono;
                document.getElementById('f_celular').value = formulario.celular;
                document.getElementById('f_correo').value = formulario.correo;
                document.getElementById('f_nivel').value = formulario.id_nivel;
                document.getElementById('f_municipio').value = formulario.id_mun;
                document.getElementById('f_municipio').disabled = true;
                document.getElementById('f_asunto').value = formulario.id_asunto;
                document.getElementById('update-delete-buttons').style.display = 'block';
                document.getElementById('btn_turno').style.display = "none";
            } else {
                Swal.fire({
                    icon: 'error',
                    title: 'Error',
                    text: 'No se encontró ningún formulario con el no_turno y CURP proporcionados.',
                });
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}

document.getElementById('buscarBtn').addEventListener('click', buscarFormulario);

/*ACTUALIZAR FORMULARIO*/
function actualizarFormulario(){
    const nombre_completo = document.getElementById('f_nc').value;
    const curp = document.getElementById('f_curp').value;
    const nombre = document.getElementById('f_nombre').value;
    const paterno = document.getElementById('f_paterno').value;
    const materno = document.getElementById('f_materno').value;
    const telefono = document.getElementById('f_telefono').value;
    const celular = document.getElementById('f_celular').value;
    const correo = document.getElementById('f_correo').value;
    const id_nivel = document.getElementById('f_nivel').value;
    const id_mun = document.getElementById('f_mun').value;
    const id_asunto = document.getElementById('f_asunto').value;
    const noTurno = document.getElementById('buscarNoTurno').value.trim();
    const data = {
        nombre_completo: nombre_completo,
        curp: curp,
        nombre: nombre,
        paterno: paterno,
        materno: materno,
        telefono: telefono,
        celular: celular,
        correo: correo,
        id_nivel: id_nivel,
        id_mun: id_mun,
        id_asunto: id_asunto,
        no_turno: noTurno
    };
    fetch('/actualizar_formulario', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        mensaje('success', '¡Actualizado!', 'El turno se ha actualizado correctamente');
    })
    .catch((error) => {
        console.error('Error:', error);
        mensaje('error', '¡Error!', 'El turno no se pudo actualizar');
    });
}

// Función para limpiar los campos del formulario
function limpiarCampos() {
    document.getElementById('buscarNoTurno').value = '';
    document.getElementById('buscarCurp').value = '';
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

// Función para mostrar mensajes utilizando SweetAlert2
function mensaje(icon, title, text) {
    Swal.fire({
        icon: icon,
        title: title,
        text: text,
    });
}
