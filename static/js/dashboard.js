function loadCircularChart() {
    fetch(`/dashboard/circular`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('circular-chart').src = data.image;
        });
}

function loadBarChart() {
    var municipio = $('#municipio-input').val();
    $.getJSON('/dashboard/bar', { municipio: municipio }, function(data) {
        if (data.image) {
            $('#bar-chart-img').attr('src', data.image);
        } else {
            console.error('Error al cargar el gráfico de barras:', data.error);
        }
    });
}

window.onload = () => {
    loadCircularChart();
    loadBarChart();
};