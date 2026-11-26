#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js Movie_ID');
  process.exit(1);
}

const url = 'https://swapi-api.hbtn.io/api/films/' + movieId + '/';

request.get(url, { json: true }, (error, response, body) => {
  if (error || !response || response.statusCode !== 200) {
    console.error('Unable to retrieve movie.');
    process.exitCode = 1;
    return;
  }

  if (!body || !Array.isArray(body.characters)) {
    console.error('Invalid movie data.');
    process.exitCode = 1;
    return;
  }

  function printCharacter(index) {
    if (index >= body.characters.length) {
      return;
    }

    request.get(
      body.characters[index],
      { json: true },
      (err, res, character) => {
        if (err || !res || res.statusCode !== 200 ||
            !character || !character.name) {
          console.error('Unable to retrieve character.');
          process.exitCode = 1;
          return;
        }

        console.log(character.name);
        printCharacter(index + 1);
      }
    );
  }

  printCharacter(0);
});
