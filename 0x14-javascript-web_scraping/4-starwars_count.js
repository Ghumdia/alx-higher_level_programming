#!/usr/bin/node
// Searchs for the number of times a character appears in a movie

const request = require('request');
const ag = process.argv;

request(ag[2], (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const films = JSON.parse(body).results;
  const numFilmsWithWedge = films.filter(film => film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')).length;

  console.log(numFilmsWithWedge);
});
