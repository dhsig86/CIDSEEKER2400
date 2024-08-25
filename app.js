document.addEventListener('DOMContentLoaded', () => {
    const searchButton = document.getElementById('search-button');
    const cidSearch = document.getElementById('cid-search');
    const resultsContainer = document.getElementById('cid-resultados');
    const loadingIndicator = document.getElementById('loading');

    // Carrega o JSON local do CID-10 completo
    fetch('CID10_completo.json')  // Verifique o caminho correto para o JSON
        .then(response => response.json())
        .then(data => {
            const search = () => {
                const query = cidSearch.value.trim().toLowerCase();

                if (!query) {
                    resultsContainer.innerHTML = '<p>Digite algo para pesquisar.</p>';
                    return;
                }

                loadingIndicator.style.display = 'block'; // Exibe o indicador de carregamento
                resultsContainer.innerHTML = ''; // Limpa resultados anteriores

                // Filtro dos resultados da busca
                const results = data.filter(item => item.Descrição.toLowerCase().includes(query));
                
                setTimeout(() => {
                    loadingIndicator.style.display = 'none'; // Oculta o indicador de carregamento
                    displayCidResults(results);
                }, 1000);  // Simulação de atraso para efeito de feedback ao usuário
            };

            // Função para exibir resultados
            const displayCidResults = (results) => {
                resultsContainer.innerHTML = '';  // Limpa resultados anteriores
                
                if (results.length === 0) {
                    resultsContainer.innerHTML = '<p>Nenhum resultado encontrado.</p>';
                } else {
                    results.forEach(result => {
                        const div = document.createElement('div');
                        div.classList.add('result-item');  // Classe CSS para estilizar
                        div.innerHTML = `<strong>${result.Código}:</strong> ${result.Descrição}`;
                        resultsContainer.appendChild(div);
                    });
                }
            };

            // Evento de clique no botão de busca
            searchButton.addEventListener('click', search);

            // Ativar a busca ao pressionar Enter
            cidSearch.addEventListener('keydown', (e) => {
                if (e.key === 'Enter') {
                    search();
                }
            });
        })
        .catch(error => {
            console.error('Erro ao carregar o JSON:', error);
            resultsContainer.innerHTML = '<p>Erro ao carregar os dados do CID-10. Tente novamente mais tarde.</p>';
        });
});
