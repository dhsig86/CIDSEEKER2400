document.addEventListener('DOMContentLoaded', () => {
    const searchButton = document.getElementById('search-button');
    const cidSearch = document.getElementById('cid-search');
    const resultsContainer = document.getElementById('cid-resultados');

    // Carrega o JSON local do CID-10
    fetch('CID10_categorias.json')  // Verifique se o caminho está correto no GitHub Pages ou no servidor local
        .then(response => {
            if (!response.ok) {
                throw new Error('Erro ao carregar o arquivo JSON');
            }
            return response.json();
        })
        .then(data => {
            // Ação ao clicar no botão de busca
            searchButton.addEventListener('click', () => {
                const query = cidSearch.value.trim().toLowerCase();
                
                // Exibe resultados da busca
                const results = data.filter(item => item.DESCRICAO.toLowerCase().includes(query));
                displayCidResults(results);
            });

            // Função para exibir resultados na página
            const displayCidResults = (results) => {
                resultsContainer.innerHTML = '';  // Limpa resultados anteriores
                
                if (results.length === 0) {
                    resultsContainer.innerHTML = '<p>Nenhum resultado encontrado.</p>';
                } else {
                    results.forEach(result => {
                        const div = document.createElement('div');
                        div.classList.add('result-item');  // Classe CSS para estilizar
                        div.innerHTML = `<strong>${result.CAT}:</strong> ${result.DESCRICAO}`;
                        resultsContainer.appendChild(div);
                    });
                }
            };
        })
        .catch(error => {
            console.error('Erro ao carregar o JSON:', error);
            resultsContainer.innerHTML = '<p>Erro ao carregar os dados do CID-10. Tente novamente mais tarde.</p>';
        });
});
