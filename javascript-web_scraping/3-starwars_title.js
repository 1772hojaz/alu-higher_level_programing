#!/usr/bin/node
// importing the request module
const req = require('request');

// taking input from the command line
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

req.get(url, (err, res) => {
  err ? console.log(err) : console.log(JSON.parse(res.body).title);
});
