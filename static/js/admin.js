function searchForm() {
    const searchQuery = document.getElementById('buscar').value;
    window.location.href = `/admin?query=${searchQuery}`;
}

function updateForm(noTurno, idMun) {
    window.location.href = `/update/${noTurno}/${idMun}`;
}

function deleteForm(noTurno, idMun) {
    Swal.fire({
        icon: 'warning',
        title: '¿Estás seguro?',
        text: "¡No podrás revertir esto!",
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Sí, eliminarlo!'
    }).then((result) => {
        if (result.isConfirmed) {
            window.location.href = `/delete/${noTurno}/${idMun}`;
        }
    });
}
