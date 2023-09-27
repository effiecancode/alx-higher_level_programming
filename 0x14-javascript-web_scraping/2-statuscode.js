#!/usr/bin/node
const request = require('request');

// process.argv[2] = url to request data from
request(process.argv[2], (error, response) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`code: ${response.statusCode}`);
  }
});
