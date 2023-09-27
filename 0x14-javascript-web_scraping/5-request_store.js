#!/usr/bin/node
const request = require('request');
const fs = require('fs');
/**
 * takes 2 arguments
 * process.argv[2] = url to fetch from
 * process.argv[3] = file where the contents will be stored
 */
request(process.argv[2]).pipe(fs.createWriteStream(process.argv[3]));

/**
 * [one line algo]
 * request module sends a request to the URL
 * then the response is piped to a writable stream created
 * by fs.createWriteStream that takes file to store data as param
 */
