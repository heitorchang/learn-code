// Use text-mode

var data = [

  {
    topic: 'Strings',
    title: 'Concatenation',
    reference: 'CIA2, p. 8',
    description: '',
    code: `
    (str "Hello, " "World!")
    (str "Commas ", "are ignored")
    `
  },

  { // begin new topic
    topic: 'References',
    title: 'Clojure in Action, 2nd ed.',
    reference: '',
    description: 'The abbreviation is CIA2',
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Syntax',
    title: 'Opening parenthesis is function call',
    reference: 'CIA2 p. 9',
    description: 'The left parenthesis is like a phone being held up to the function\'s ear, getting ready to call it.',
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Java interop',
    title: 'Dot operator by itself',
    reference: 'CIA2 p. 12',
    description: 'The dot operator should be read as "in the scope of A do B with arguments ..."',
    code: `
    (. Math PI)
    (. Math abs -3)
    `
  },

  { // begin new topic
    topic: 'Java interop',
    title: 'Static fields and methods',
    reference: 'CIA2 p. 13',
    description: 'Static fields and methods are accessed with a forward slash.',
    code: `
    Math/PI
    (Math/abs -3)
    `
  },

  { // begin new topic
    topic: 'Java interop',
    title: 'Dot operator as instance method invocation',
    reference: 'CIA2 p. 13',
    description: 'Method invocation looks like a function call.',
    code: `
    (.toUpperCase "foo")
    `
  },

  { // begin new topic
    topic: 'Classes',
    title: 'Creating instances',
    reference: 'CIA2 p. 13',
    description: 'The <code>new</code> operator or a trailing dot calls a class\'s constructor.',
    code: `
    (new Integer "42")
    (Integer. "42")
    `
  },

  { // begin new topic
    topic: 'Documentation',
    title: 'Looking up documentation',
    reference: 'CIA2 p. 20',
    description: 'The macro <code>doc</code> accepts the name of a function or macro.',
    code: `
    (doc +)
    `
  },

  { // begin new topic
    topic: 'Documentation',
    title: 'Searching inside documentation',
    reference: 'CIA2 p. 21',
    description: '<code>find-doc</code> accepts a string (or regex) and prints all documentation matching the supplied input.',
    code: `
    (find-doc "lazy")
    `
  },

  { // begin new topic
    topic: 'Documentation',
    title: 'Search in function names',
    reference: 'CIA2 p. 21',
    description: '<code>apropos</code> prints the names of functions and macros matching the given Symbol.',
    code: `
    (apropos 'doc)
    `
// '
  },

  { // begin new topic
    topic: 'Comments',
    title: 'Semicolons',
    reference: 'CIA2 p. 23',
    description: 'Use single semicolons for comments after some code. Double semicolons comment out an entire line. Triple semicolons are used for block comments',
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Comments',
    title: 'Multiline comments',
    reference: 'CIA2 p. 23',
    description: 'The <code>comment</code> macro causes the entire s-expression to be treated as a comment',
    code: `
    (comment
     (defn some-fn [x]
      (+ x y)))
    `
  },

  { // begin new topic
    topic: 'Types',
    title: 'Nil, truth and falsehood',
    reference: 'CIA2 p. 24',
    description: '<code>nil</code> is equivalent to <code>null</code> in Java.<br><br>Everything other than <code>false</code> and <code>nil</code> is considered true. There is a <code>true</code> value.',
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Types',
    title: 'Characters',
    reference: 'CIA2 p. 24',
    description: 'Characters are Java characters (16-bit UTF-16 code points), and a backslash is used to denote characters.',
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Types',
    title: 'Strings',
    reference: 'CIA2 p. 24',
    description: 'Strings are Java strings. They are denoted using double quotes. Single quotes are used for <code>Symbol</code>s.',
    code: `

    `
  },

  { // begin new topic
    topic: 'Types',
    title: 'Numbers',
    reference: 'CIA2 p. 25',
    description: 'Numbers are 64-bit Java longs or 64-bit Java doubles. There are also big integers (with N after the number), big decimals (with M after the number), and ratios.',
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Types',
    title: 'Autopromoting to big number',
    reference: 'CIA2 p. 26',
    description: 'Normally, overflow throws an ArithmeticException. To autopromote, use <code>+\', -\', *\', inc\'</code> and <code>dec\'</code>',
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Types',
    title: 'Symbols',
    reference: 'CIA2 p. 26',
    description: 'Symbols are identifiers, that is, names that signify values. By themselves, they are just names with an optional namespace, but when an expression is evaluated, they are replaced with the value they signify.<br><br>To treat a symbol as a value itself, quote it with a leading single quote. The symbol is treated as data, not code.<br><br>A symbol can be constructed with the <code>symbol</code> function.',
    code: `
    'arglebarg

    (symbol "foo")
    (symbol "foo bar")
    `
// '  
  },

  { // begin new topic
    topic: 'Types',
    title: 'Keywords',
    reference: 'CIA2 p. 27',
    description: 'Keywords are like autoquoted symbols. They never reference some other value, and always evaluate to themselves. Keywords start with a colon, and can be constructed with the <code>keyword</code> function.',
    code: `
    :foo

    (keyword "foo")
    (keyword "foo" "bar")
    `
  },

  { // begin new topic
    topic: '',
    title: '',
    reference: 'CIA2 p. ',
    description: '',
    code: `
    
    `
  },

  { // begin new topic
    topic: '',
    title: '',
    reference: 'CIA2 p. ',
    description: '',
    code: `
    
    `
  },

  { // begin new topic
    topic: '',
    title: '',
    reference: 'CIA2 p. ',
    description: '',
    code: `
    
    `
  },

  { // begin new topic
    topic: '',
    title: '',
    reference: 'CIA2 p. ',
    description: '',
    code: `
    
    `
  },

  { // begin new topic
    topic: '',
    title: '',
    reference: 'CIA2 p. ',
    description: '',
    code: `
    
    `
  },

  { // begin new topic
    topic: '',
    title: '',
    reference: 'CIA2 p. ',
    description: '',
    code: `
    
    `
  },

  { // begin new topic
    topic: '',
    title: '',
    reference: 'CIA2 p. ',
    description: '',
    code: `
    
    `
  },

  { // begin new topic
    topic: '',
    title: '',
    reference: 'CIA2 p. ',
    description: '',
    code: `
    
    `
  },

    
];

