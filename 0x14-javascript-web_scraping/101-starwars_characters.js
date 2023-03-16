const request = require('request');
const ag = process.argv;

request('https://swapi-api.alx-tools.com/api/films/' + ag[2], (error, response, body) => {
  if (error) {
    console.error(error);
  }
  const data = JSON.parse(body);
  console.log(data.title);
});
