document.addEventListener("DOMContentLoaded", function() {
    document.getElementById("btnGenerarPDF").addEventListener("click", function() {
        // Obtener los datos del DOM
        let nombreCompleto = document.getElementById("nombre_completo").innerText;
        let curp = document.getElementById("curp").innerText;
        let nombre = document.getElementById("nombre").innerText;
        let paterno = document.getElementById("paterno").innerText;
        let materno = document.getElementById("materno").innerText;
        let telefono = document.getElementById("telefono").innerText;
        let celular = document.getElementById("celular").innerText;
        let correo = document.getElementById("correo").innerText;
        let nivel = document.getElementById("nivel").innerText;
        let municipio = document.getElementById("municipio").innerText;
        let asunto = document.getElementById("asunto").innerText;
        let noTurno = document.getElementById("no_turno").innerText;

        // Crear objeto con los datos
        let datos = {
            nombre_completo: nombreCompleto,
            curp: curp,
            nombre: nombre,
            paterno: paterno,
            materno: materno,
            telefono: telefono,
            celular: celular,
            correo: correo,
            nivel: nivel,
            municipio: municipio,
            asunto: asunto,
            no_turno: noTurno
        };

        // Realizar la solicitud POST al servidor Flask
        fetch("/generar_pdf", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(datos)
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Abrir el PDF en una nueva pestaña
                window.open(data.pdf_url, '_blank');
                // Mostrar mensaje de éxito
                Swal.fire({
                    icon: 'success',
                    title: 'PDF Generado',
                    text: 'Se ha generado el PDF correctamente.',
                    footer: '<a href="">Necesitas ayuda?</a>'
                });
            } else {
                // Mostrar mensaje de error si no se puede generar el PDF
                Swal.fire({
                    icon: 'error',
                    title: 'Error',
                    text: 'No se pudo generar el PDF.',
                    footer: '<a href="">Necesitas ayuda?</a>'
                });
            }
        })
        .catch(error => {
            // Mostrar mensaje de error en caso de fallo en la solicitud
            console.error('Error al generar el PDF:', error);
            Swal.fire({
                icon: 'error',
                title: 'Error',
                text: 'Ocurrió un error al generar el PDF.',
                footer: '<a href="">Necesitas ayuda?</a>'
            });
        });
    });
});
