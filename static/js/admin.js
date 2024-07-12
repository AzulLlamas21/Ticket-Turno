function searchForm(id, id_mun) {
    window.location.href = `/search/${id}/${id_mun}`;
}

function updateForm(id, id_mun) {
    window.location.href = `/update/${id}/${id_mun}`;
}

function deleteForm(id, id_mun) {
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
            window.location.href = `/delete/${id}/${id_mun}`;
        }
    });
}

