fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => response.json())
    .then(data => {
        const characterDiv = document.getElementById('character');
        characterDiv.textContent = data.name;
})