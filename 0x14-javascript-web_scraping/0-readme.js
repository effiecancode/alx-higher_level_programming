#!/usr/bin/node
const fs = require('fs').promises;

async function readdata (filepath) {
  try {
    const data = await fs.readFile(filepath, 'utf8');
    console.log(`File contents are ; ${data}`);
  } catch (error) {
    console.error(`Attempt to readfile ${filepath} unsuccessful: ${error.message}`);
  }
}

// const filepath = 'path/to/my/file.txt';
// readdata(filepath);
