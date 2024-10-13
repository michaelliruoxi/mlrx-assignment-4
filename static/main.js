document.getElementById('search-form').addEventListener('submit', function (event) {
    event.preventDefault();
    
    let query = document.getElementById('query').value;
    let resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = '';

    fetch('/search', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: new URLSearchParams({
            'query': query
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        displayResults(data);
        displayChart(data);
    });
});

function displayResults(data) {
    let resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = '<h2>Results</h2>';
    for (let i = 0; i < data.documents.length; i++) {
        let docDiv = document.createElement('div');
        docDiv.innerHTML = `<strong>Document ${data.indices[i]}</strong><p>${data.documents[i]}</p><br><strong>Similarity: ${data.similarities[i]}</strong>`;
        resultsDiv.appendChild(docDiv);
    }
}

function displayChart(data) {
    const similarityChart = document.getElementById('similarity-chart');

    const trace = {
        x: data.indices.map(i => `Doc ${i}`),
        y: data.similarities,
        type: 'bar',
        text: data.similarities.map(sim => sim.toFixed(3)),
        hovertext: data.indices.map((i, idx) => `Doc ${i}<br>Cosine Similarity: ${data.similarities[idx].toFixed(3)}`),
        hoverinfo: 'text',  // This ensures that the hovertext shows
        textposition: 'auto',
        marker: {
            color: 'rgba(55, 128, 191, 0.6)',
            line: {
                color: 'rgba(55, 128, 191, 1.0)',
                width: 2
            }
        }
    };

    const layout = {
        title: 'Cosine Similarity of Top Documents',
        xaxis: { title: 'Document' },
        yaxis: { title: 'Cosine Similarity', range: [0, 1] }
    };

    // Use Plotly to plot the data on the div
    Plotly.newPlot(similarityChart, [trace], layout);
}