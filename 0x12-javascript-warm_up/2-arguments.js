#!/usr/bin/node

const argscount = process.argv.length - 2;

if (argscount === 0){
    console.log("No argument");
} else if (argscount === 1){
    console.log("Argument found");
} else {
    console.log("Arguments found")
}


// set argcount to length -2
// process.argv[0] contains the path to the Node.js executable.
// process.argv[1] contains the path to the script file being executed.
