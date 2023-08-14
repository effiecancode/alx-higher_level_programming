#!/usr/bin/node

// Check if the number of occurrences argument is provided
if (process.argv.length < 3) {
  console.log('Missing number of occurrences');
} else {
  // Parse the argument as an integer
  const x = parseInt(process.argv[2]);

  // Check if the parsed value is a valid integer
  if (isNaN(x)) {
    console.log('Missing number of occurrences');
  } else {
    // Loop to print "C is fun" x times
    for (let i = 0; i < x; i++) {
      console.log('C is fun');
    }
  }
}
