#!/usr/bin/node

if (isNaN(process.argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    const str = 'X';
    console.log(str.repeat(process.argv[2]));
  }
}
