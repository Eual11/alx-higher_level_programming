#!/usr/bin/node

if (process.argv.length <= 3) {
  console.log(0);
} else {
  const args = process.argv.map(Number).slice(2, process.argv.length).sort((a, b) => a - b);
  const sl = args[(args.length-2)];
  console.log(sl) 
}
