fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
        const list = document.getElementById('list_movies');
        const films = data.results;

        films.forEach(film => {
            const li = document.createElement('li');
            li.textContent = film.title;
            list.appendChild(li);
        });
    });