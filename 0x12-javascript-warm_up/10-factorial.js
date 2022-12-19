#!/usr/bin/node

function factorial (num) {
  const n = parseInt(num);

  if (n === 0) {
    return 1;
  } else if (isNaN(n)) {
    return 1;
  } else {
    return n * factorial((n - 1));
  }
}

console.log(factorial(process.argv[2]));
