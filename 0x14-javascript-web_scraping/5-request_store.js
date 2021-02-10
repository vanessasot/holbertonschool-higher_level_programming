#!/usr/bin/node
// Prints the number of movies where the character Wedge Antilles is present

const request = require('request');
const fs = require('fs');
const requestURL = process.argv[2];
request(requestURL, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    fs.writeFile(process.argv[3], body, 'utf8', function (err) {
      if (err) {
        console.log(err);
      }
    });
  }
});
