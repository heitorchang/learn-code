// Use text-mode

var data = [

  { // begin new topic
    topic: 'File I/O',
    title: 'Include a script',
    reference: 'http://docs.julialang.org/en/release-0.4/manual/getting-started/',
    description: 'To evaluate expressions written in a source file file.jl, evaluate include("file.jl").',
    code: `
    include("file.jl")
    `
  },

  { // begin new topic
    topic: 'File I/O',
    title: 'Working with Directories',
    reference: 'http://docs.julialang.org/en/release-0.4/stdlib/file/',
    description: '',
    code: `
    pwd()  # get current working directory

    cd([ dir::AbstractString ])  # set current working directory

    isdir(path)  # returns true if path is a directory

    isfile(path)  # returns true is path is a regular file

    dirname(path)  # get directory part of a path
    basename(path)  # get the file name part of a path
    `
  },

  { // begin new topic
    topic: 'Arrays',
    title: 'Concatenation',
    reference: 'REPL',
    description: '[a] concatenation, such as [1:2:9] is deprecated.',
    code: `
    collect(1:2:9)  # creates an array
    `
  },

  { // begin new topic
    topic: 'Types',
    title: 'Checking types',
    reference: 'help? type',
    description: '',
    code: `
    typeof(x)  # gets the concrete type of x
    
    `
  },

  { // begin new topic
    topic: 'Dicts',
    title: 'Dict is the standard associative collection',
    reference: 'http://docs.julialang.org/en/release-0.4/stdlib/collections/',
    description: '',
    code: `
    Dict("A" => 1, "B" => 2)

    [i => f(i) for i = 1:10]  # create with a comprehension

    d = Dict()
    d["a"] = 1
    `
  },

  { // begin new topic
    topic: 'Strings',
    title: 'Interpolation',
    reference: 'http://docs.julialang.org/en/release-0.4/manual/strings/',
    description: 'Like Perl, a variable\'s value may be inserted into a string literal using $. Any expression may be used inside parentheses, $(...)',
    code: `
    "$greet, $whom.\\n"

    "1 + 2 = $(1 + 2)"

    "Answer is $(qs[i].answer[2])"
    `
  },

  { // begin new topic
    topic: 'Arrays',
    title: 'Last element\'s index',
    reference: 'https://en.wikibooks.org/wiki/Introducing_Julia/Arrays_and_tuples',
    description: 'The last element of an array is <b>end</b>',
    code: `
    z = [10, 20, 30]

    z[end-1]  # 20
    `
  },

  { // begin new topic
    topic: 'Matrices',
    title: 'Get elements by indices',
    reference: '',
    description: 'Rows, columns, and items may be accessed with square brackets. In a 2-d matrix, the first dimension is rows and the second, columns',
    code: `
    > a = [3 4; 5 6; 2 1]

    3 4
    5 6
    2 1
    
    > a[:,1]

    3
    5
    2

    > a[[1,3], 2]

    4
    1
    `
  },

  { // begin new topic
    topic: 'Matrices',
    title: 'Size of a matrix',
    reference: '',
    description: '<code>ndims()</code> and <code>size()</code>',
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

