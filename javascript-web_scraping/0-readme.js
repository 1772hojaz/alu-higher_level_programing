#!/usr/bin/node

// Using the file system module. It provides an API that allows me to interact with the file system.
const fileSy = require('fs');

// Getting the file name from the command-line
const fiLe = process.argv[2];

// Reading the file and erl is the an argument that calls the error  object 
fileSy.readFile(fiLe, 'utf8', (erl, data) => {
    if (erl) {
        console.error(erl);
    } else {
        console.log(data);
    }
});
//By HUMPHREY NYAHOAJA 
