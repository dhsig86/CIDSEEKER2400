document.addEventListener("DOMContentLoaded", function () {
    const searchInput = document.getElementById("searchInput");
    const searchButton = document.getElementById("searchButton");
    const autoSearchToggle = document.getElementById("autoSearchToggle");
    const resultTable = document.getElementById("resultTable");
    const errorMessage = document.getElementById("errorMessage");

    let cidData = [];

    // Load CID10 data
    fetch("CID10_completo.json")
        .then(response => {
            if (!response.ok) {
                throw new Error("Failed to load CID-10 data");
            }
            return response.json();
        })
        .then(data => {
            cidData = data;
            // Enable search on button click
            searchButton.addEventListener("click", () => {
                performSearch(cidData, searchInput.value);
            });

            // Enable live search during typing if toggle is enabled
            searchInput.addEventListener("input", () => {
                if (autoSearchToggle.checked) {
                    performSearch(cidData, searchInput.value);
                }
            });
        })
        .catch(error => {
            errorMessage.textContent = "Erro ao carregar os dados do CID-10. Tente novamente mais tarde.";
            console.error("Error loading CID-10 data:", error);
        });

    // Function to perform the search
    function performSearch(data, searchTerm) {
        // Clear previous results
        resultTable.innerHTML = "";

        const searchTermLower = searchTerm.toLowerCase();
        const filteredResults = data.filter(entry =>
            entry.Código.toLowerCase().includes(searchTermLower) ||
            entry.Descrição.toLowerCase().includes(searchTermLower)
        );

        if (filteredResults.length > 0) {
            // Display results in the table
            filteredResults.forEach(result => {
                const row = document.createElement("tr");

                const codeCell = document.createElement("td");
                codeCell.textContent = result.Código;

                const descriptionCell = document.createElement("td");
                descriptionCell.textContent = result.Descrição;

                row.appendChild(codeCell);
                row.appendChild(descriptionCell);
                resultTable.appendChild(row);
            });
        } else {
            const noResultsRow = document.createElement("tr");
            const noResultsCell = document.createElement("td");
            noResultsCell.textContent = "Nenhum resultado encontrado";
            noResultsCell.setAttribute("colspan", 2);
            noResultsRow.appendChild(noResultsCell);
            resultTable.appendChild(noResultsRow);
        }
    }
});
