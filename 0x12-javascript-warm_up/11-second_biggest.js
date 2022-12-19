#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const sl = process.argv.map(Number).slice(2, process.argv.length).sort().reverse()[1];
  console.log(sl);
}
