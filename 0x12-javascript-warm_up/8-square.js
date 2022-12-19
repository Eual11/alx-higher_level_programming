#!/usr/bin/node

const size = process.argv[2];
const c = 'X';

if (parseInt(size)) {
  let i = 0;
  while (i < size) {
    console.log(c.repeat(size));
    i++;
  }
} else {
  console.log('Missing size');
}
