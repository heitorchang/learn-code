// Use text-mode

var data = [

  /*
  {
    topic: 'TOPIC',
    title: 'CARD TITLE',
    reference: 'REFERENCE SOURCE',
    description: 'DESCRIPTION',
    code: `
CODE
CODE    
    `
  },
  */
  
  { // begin new topic
    topic: 'Strings',
    title: 'string?',
    reference: '',
    description: '',
    code: `
(string? obj)
    `
  },

  { // begin new topic
    topic: 'Strings',
    title: 'make-string',
    reference: '',
    description: '',
    code: `
(make-string len)
(make-string len char)
    `
  },

  { // begin new topic
    topic: 'Strings',
    title: 'string',
    reference: '',
    description: 'Returns a newly allocated string composed of one or more character arguments',
    code: `
(string char ...)
    `
  },

  { // begin new topic
    topic: 'Characters',
    title: 'Literals',
    reference: '',
    description: '',
    code: `
#\\a
#\\space
#\\newline
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'do',
    reference: '',
    description: '4.2.4',
    code: `
(do ((<variable1> <init1> <step1>)
     (<variable2> <init2> <step2>)
     ...)
    (<test> <expression> ...)
  <command> ...)
    `
  },

  { // begin new topic
    topic: 'Conditionals',
    title: 'cond',
    reference: '4.2.1',
    description: '',
    code: `
(cond <clause1> <clause2> ...)

;; where clause is
(<test> <expression1> <expression2> ...)

;; the last (optional) clause is
(else <expression1> <expression2> ...)
    `
  },

  { // begin new topic
    topic: 'Types',
    title: 'Predicates',
    reference: '',
    description: '',
    code: `
boolean?
number?

char?
string?

symbol?

pair?
vector?

procedure?

port?
    `
  },

  { // begin new topic
    topic: 'Lists and pairs',
    title: 'Creating lists',
    reference: '6.3.2',
    description: 'Quoting a list does not evaluate anything. To evaluate list members, use <code>list</code>',
    code: `
'(1 (+ 2 3))
;;> (1 (+ 2 3))

(list 1 (+ 2 3))
;;> (1 5)
    `
  },

  { // begin new topic
    topic: 'Numbers',
    title: 'Tower of types',
    reference: '',
    description: 'Each level is a subset of the level above it.<br><br>number<br>complex<br>real<br>rational<br>integer',
    code: `
    
    `
  },

    { // begin new topic
    topic: 'Booleans',
    title: 'True/false values',
    reference: '6.3.1', 
    description: 'Only <code>#f</code> counts as false in conditional expresssions.',
    code: `

    `
  },

    { // begin new topic
    topic: 'Symbols',
    title: 'symbol->string',
    reference: '6.3.3',
    description: 'In the standard, symbol names are case-insensitive, but implementations may be case-sensitive.',
    code: `
    
    `
  },

    { // begin new topic
    topic: 'Symbols',
    title: 'string->symbol',
    reference: '6.3.3',
    description: 'In the standard, symbol names are case-insensitive, but implementations may be case-sensitive.',
    code: `
    
    `
  },

    { // begin new topic
    topic: 'Procedures',
    title: 'lambda',
    reference: '',
    description: '',
    code: `
(lambda <formals> <body>)

;; <formals> is a formal argument list
;; <body> is a sequence of one or more expressions
    `
  },

    { // begin new topic
    topic: 'Vectors',
    title: 'make-vector',
    reference: '',
    description: '',
    code: `
(make-vector len fill)
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

