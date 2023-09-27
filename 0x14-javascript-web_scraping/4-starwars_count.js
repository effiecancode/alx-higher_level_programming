#!/usr/bin/node
const request = require('request');

const baseUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(baseUrl, (error, response, body) => {
  if (!error) {
    const titles = JSON.parse(body).results;
    let foundtitles = 0;

    for (const movie of titles) {
      if (movie.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
        foundtitles++;
      }
    }
    console.log(foundtitles);
  }
});
