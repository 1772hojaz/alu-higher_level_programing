#!/usr/bin/node
// useing file system module
const fileSy = require('fs');
// the file path
const filePath = process.argv[2];
// the string on the command-line
const comStr = process.argv[3];

fileSy.writeFile(filePath, comStr, (eyo) => {
  if (eyo) {
    console.error(eyo);
  } else {
    return null;
  }
});
