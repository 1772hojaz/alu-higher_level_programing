#!/usr/bin/node
const [,, theArg] = process.argv;
if (theArg === undefined) {
  console.log('No argument');
} else {
  console.log(theArg);
}
