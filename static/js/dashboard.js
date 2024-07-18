function loadCircularChart() {
    fetch(`/dashboard/circular`)
    .then(response => response.json())
    .then(data => {
        document.getElementById('circular-chart').src = data.image;
    });
}

function loadBarChart() {
    const searchParams = new URLSearchParams(window.location.search);
    const municipio = searchParams.get('municipio');
    const url = municipio ? `/dashboard/bar?municipio=${municipio}` : '/dashboard/bar';
    
    fetch(url)
    .then(response => response.json())
    .then(data => {
        document.getElementById('bar-chart').src = data.image;
    });
}

function searchMunicipio() {
    const searchQuery = document.getElementById('buscar').value;
    window.location.href = `/dashboard?municipio=${searchQuery}`;
}

window.onload = () => {
    loadCircularChart();
    loadBarChart();
};