#!/usr/bin/node

// include the request module
const rs = require('request');
// taking input from the comand-line
const input = process.argv[2];
rs(input, (erl, resPo) => {
  console.log('code:' + resPo.statusCode);
});
