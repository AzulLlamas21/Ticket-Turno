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
                document.getElementById('update-delete-buttons').style.display = 'block';
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
