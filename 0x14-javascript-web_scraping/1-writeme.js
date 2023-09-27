#!/usr/bin/node
const fs = require('fs');

/**
 * process.argv[3] = content to be written in the file
 * process.argv[2] = filename to be read
 * process.argv[1] = the file path
 * process.argv[0] = the Node.js executable
*/
fs.writeFile(process.argv[2], process.argv[3], 'utf-8', (error, data) => {
  if (error) {
    console.error(error);
  }
});
