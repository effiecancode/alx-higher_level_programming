#!/usr/bin/node
const request = require('request');

// retrieve url from command line arguments
const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    const completed = {};
    const tasks = JSON.parse(body);

    for (const i in tasks) {
      const task = tasks[i];

      if (task.completed === true) {
        if (completed[task.userId] === undefined) {
          completed[task.userId] = 1;
        } else {
          completed[task.userId]++;
        }
      }
    }
    console.log(completed);
  } else {
    console.log('An error occured. Status code: ' + response.statusCode);
  }
});

/**
 * [algo]
 * request to url + callback function to handle HTTP response
 * create empty object to store count
 * parse the response body to js object
 * iterate through each item in tasks object
 * [i] rep the current task being processes during iteration
 * Checks if the completed property of the current task is true
 * [nested if-else]
 * Checks if the user's ID is not already in the completed object.
 * If the user's ID is not in the completed object, it initializes the
 * count for that user to 1
 * else increament count
 * error handling during requests
 */
