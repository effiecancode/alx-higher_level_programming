#!/usr/bin/node
const fs = require('fs');

/**
 * process.argv[2] = filename to be read
 * process.argv[1] = the file path
 * process.argv[0] = the Node.js executable
*/

fs.readFile(process.argv[2], 'utf-8', (error, data) => {
  if (error) {
    console.error(error);
    return;
  }
  console.log(data);
});

/** (error, data) are params for the arrow function
 * its a callback function to check for errors during file reading
*/
