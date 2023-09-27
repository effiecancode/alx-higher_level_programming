#!/usr/bin/node
const request = require('request');

const baseUrl = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(baseUrl, (error, response, body) => {
  if (!error) {
    const titles = JSON.parse(body).results;
    const foundtitles = 0;

    for (const movie of titles) {
      for (const char of movie.characters) {
        if (char.endsWith('/18/')) {
          foundtitles++;
          break;
        }
      }
    }
    console.log(foundtitles);
  }
});
