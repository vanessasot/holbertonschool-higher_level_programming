#!/usr/bin/node
// Prints the number of movies where the character Wedge Antilles is present

const request = require('request');
const requestURL = process.argv[2];
request(requestURL, function (error, response, body) {
  let n = 0;
  if (error) {
    console.log(error);
  }
  for (const movie of JSON.parse(body).results) {
    n += movie.characters.filter(each => each.search('/18/') > 0).length;
  }
  console.log(n);
});
