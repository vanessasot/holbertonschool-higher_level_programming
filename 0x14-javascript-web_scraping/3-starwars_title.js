#!/usr/bin/node
// Prints the title of a Star Wars movie where the episode number matches a given integer

const request = require('request');
const requestURL = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
