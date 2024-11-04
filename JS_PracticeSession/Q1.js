
let a = 1;
let b = 5;
let c = 2;

let og_a = a;
let og_b = b;

a += b; // a = a + b
b += c;

console.log(og_a, og_b, c);
console.log(a, b, c);

