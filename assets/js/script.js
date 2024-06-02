document.addEventListener('DOMContentLoaded', function () {
        const searchInput = document.querySelector('#search-input');
        const resultsContainer = document.querySelector('#results-container');

        function performSearch(searchTerm) {
            fetch(`/search?searchTerm=${searchTerm}`)
                .then(response => {
                    if (!response.ok) {
                        throw new Error('Erreur lors de la récupération des données. Veuillez réessayer plus tard.');
                    }
                    return response.json();
                })
                .then(results => {
                    displayResults(results);
                })
                .catch(error => console.error('Error:', error));
        }

        function displayResults(results) {
            results.forEach(result => {
                const resultElement = document.createElement('div');
                resultElement.textContent = `
                <p>Nom: ${result.nom}</p>
                <p>Prénom: ${result.prenom}</p>
                <p>Email: ${result.email[0]}</p>
            `;
                resultsContainer.appendChild(resultElement);
            });
        }
    }
);
