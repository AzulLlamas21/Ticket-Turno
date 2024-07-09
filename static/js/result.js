document.addEventListener("DOMContentLoaded", function() {
    let params = new URLSearchParams(window.location.search);
    let resultDiv = document.getElementById("result");

    const nivelTextos = {
        "1": "Nivel 1",
        "2": "Nivel 2",
        "3": "Nivel 3",
        "4": "Nivel 4",
        "5": "Nivel 5",
        "6": "Nivel 6",
        "7": "Nivel 7",
        "8": "Nivel 8",
        "9": "Nivel 9"
    };

    const munTextos = {
        "1": "Saltillo",
        "2": "Arteaga",
        "3": "Ramos Arizpe",
        "4": "Monclova",
        "5": "Torreón",
        "6": "Acuña",
        "7": "Ocampo",
        "8": "Piedras Negras"
    };

    const asuntoTextos = {
        "1": "Ingreso",
        "2": "Egreso",
        "3": "Pago de Inscripción",
        "4": "Selección de Horario",
        "5": "Recoger papelería"
    };

    let nivel = params.get("nivel");
    let mun = params.get("mun");
    let asunto = params.get("asunto");

    let nivelTexto = nivelTextos[nivel] || "No seleccionado";
    let munTexto = munTextos[mun] || "No seleccionado";
    let asuntoTexto = asuntoTextos[asunto] || "No seleccionado";

    let data = `
        <p><strong>Nombre Completo:</strong> ${params.get("nc")}</p>
        <p><strong>CURP:</strong> ${params.get("curp")}</p>
        <p><strong>Nombre:</strong> ${params.get("nombre")}</p>
        <p><strong>Apellido Paterno:</strong> ${params.get("paterno")}</p>
        <p><strong>Apellido Materno:</strong> ${params.get("materno")}</p>
        <p><strong>Teléfono:</strong> ${params.get("telefono")}</p>
        <p><strong>Celular:</strong> ${params.get("celular")}</p>
        <p><strong>Correo:</strong> ${params.get("correo")}</p>
        <p><strong>Nivel:</strong> ${nivelTexto}</p>
        <p><strong>Municipio:</strong> ${munTexto}</p>
        <p><strong>Asunto:</strong> ${asuntoTexto}</p>
    `;

    resultDiv.innerHTML = data;
});
