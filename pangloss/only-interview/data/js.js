var data = [

  {
    topic: 'Objects',
    title: 'Initializing an object',
    reference: 'self',
    description: 'An object may be initialized with a literal',
    code: `
    var obj = {};
    `
  },

  {
    topic: 'Control flow',
    title: 'If statements',
    reference: 'self',
    description: 'The most basic conditional.',
    code: `
    if () {
      function () {

      }
    }
    `
  },

  { // begin new topic
    topic: 'Objects',
    title: 'Classic inheritance',
    reference: 'Crockford, http://www.crockford.com/javascript/inheritance.html',
    description: 'JavaScript is prototype-based',
    code: `
    function Animal() {

    }

    function Cat() {

    }

    Cat.prototype;
    `
  },

  { // begin new topic
    topic: 'Objects',
    title: 'Methods',
    reference: 'http://eloquentjavascript.net/06_object.html',
    description: '',
    code: `
    Rabbit.prototype.speak = function(line) {
      console.log("The " + this.type + " rabbit says '" +
                  line + "'");
    };
    blackRabbit.speak("Doom...");
    `
  },

  { // begin new topic
    topic: 'Strings',
    title: 'Substrings',
    reference: '',
    description: 'substring and substr do different things',
    code: `
    var a = "abcdefgh";

    a.substr(2, 4);
    // cdef
    
    a.substring(2, 4);
    // cd

    // substring can go backwards
    a.substring(4, 2);
    // cd
    `
  },

  { // begin new topic
    topic: 'Arrays',
    title: 'Initializing',
    reference: '',
    description: '',
    code: `
    var arr = [1, 2, 3];    
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
    topic: 'Arrays',
    title: 'Initializing',
    reference: '',
    description: '',
    code: `
    var arr = [100, 2, 3];    
    `
  },


  
  { // begin new topic
    topic: 'Rickroll',
    title: 'Never gonna give you up',
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

