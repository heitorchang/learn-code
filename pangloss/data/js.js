var data = [

  // TODO
  //
  // Data structures: queue, stack, set
  // regex
  // for...in
  // yield
  
  { // begin new topic
    topic: 'Strings',
    title: 'Substrings',
    reference: '',
    description: 'substring and substr do different things',
    code: `
var a = "abcdefgh";

a.substr(2, 4);  // cdef
a.substring(2, 4);  // cd

// substring can go backwards
a.substring(4, 2);
// cd
    `
  },

  { // begin new topic
    topic: 'Arrays',
    title: 'Slicing',
    reference: '',
    description: '',
    code: `
var a = [0, 10, 20, 30, 40, 50];

a.slice(1);  // begins at 1, goes until end
// [10, 20, 30, 40, 50]

a.slice(2, 4);  // begins at 2, but does not include 4
// [20, 30]

a.slice(1, -1);  // -1 counts backwards from the end
// [10, 20, 30, 40]
    `
  },


  { // begin new topic
    topic: 'Variables',
    title: 'let variables are block-limited',
    reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/let',
    description: 'The let statement declares a block scope local variable. var declares them to function or global scope.',
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'Default parameters',
    reference: 'https://www.tutorialspoint.com/es6/es6_functions.htm',
    description: '',
    code: `
function add(a, b=10) {
  return a + b;
}
    `
  },

  { // begin new topic
    topic: 'Sorting',
    title: 'Sort integers',
    reference: 'https://stackoverflow.com/questions/1063007/how-to-sort-an-array-of-integers-correctly',
    description: 'By default, .sort() will sort lexicographically. Pass a simple comparison function to sort by numeric value. .sort() changes the array in-place.',
    code: `
var a = [1, 3, 2, 10, 100];
a.sort();  // [1, 10, 100, 2, 3]

a.sort((a, b) => a - b);  // [1, 2, 3, 10, 100]
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'Rest parameters',
    reference: 'https://www.tutorialspoint.com/es6/es6_functions.htm',
    description: 'The last parameter in a function definition may be a "rest parameter". It collects a variable number of arguments into the variable named after the ellipsis.',
    code: `
function scalar(s, ...vals) {
  for (let v of vals) {
    console.log(s * v);
  }
}
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'Iterate over elements of an array',
    reference: 'https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for...of',
    description: 'The keyword for retrieving elements is "of" (Python uses "in"). Using "in" results in iterating over the enumerable properties of an object (in the case of an array, its valid indices). However, correct order is not guaranteed.',
    code: `
var nums = [1, 3, 5];
    
for (let num of nums) {
  console.log(num);
}
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'Arrow functions',
    reference: '',
    description: 'A shorthand for defining functions.',
    code: `
var square = (x) => x * x;
var hello = () => "Hello";
var add = (a, b) => a + b;
    `
  },

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: '',
    code: `
    
    `
  },

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: '',
    code: `
    
    `
  },

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: '',
    code: `
    
    `
  },

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: '',
    code: `
    
    `
  },

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: '',
    code: `
    
    `
  },

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: '',
    code: `
    
    `
  },


];

