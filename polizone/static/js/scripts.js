function loadContent(url) {
    fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error('Error al cargar el contenido: ' + response.status);
            }
            return response.text();
        })
        .then(data => {
            const contentDiv = document.getElementById('content');
            contentDiv.innerHTML = data; 
            contentDiv.style.display = 'block'; 
        })
        .catch(error => {
            console.error(error);
            alert('No se pudo cargar el contenido.');
        });
}
