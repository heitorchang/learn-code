// Use text-mode

var data = [


  // TODO
  // explode
  // array_slice
  
  {
    topic: 'Syntax',
    title: 'PHP tags',
    reference: 'http://php.net/manual/en/language.basic-syntax.phptags.php',
    description: 'For pure PHP code, it is preferable to omit the PHP closing tag at the end of the file',
    code: `
<?php
echo "Hello World";

// more code

// end without closing tag
    `
  },

  { // BEGIN NEW CARD
    topic: 'Syntax',
    title: 'Short echo tag',
    reference: 'http://php.net/manual/en/language.basic-syntax.phpmode.php',
    description: 'Always enabled since PHP 5.4',
    code: `
<?= $var; ?>
    `
  },

  { // BEGIN NEW CARD
    topic: 'Types',
    title: '8 primitive types and 6 pseudo-types',
    reference: 'http://php.net/manual/en/language.types.intro.php',
description: `
The primitives are:
<p>
Four scalar types:
<ul>
<li>boolean</li>
<li>integer</li>
<li>float (it is the same as double)</li>
<li>string</li>
</ul>

Two compound types:
<ul>
<li>array</li>
<li>object</li>
</ul>

Two special types:
<ul>
<li>resource</li>
<li>NULL</li>
</ul>

Six pseudo-types:
<ul>
<li>mixed</li>
<li>number</li>
<li>callback (or callable)</li>
<li>array|object</li>
<li>void</li>
<li>$... (pseudo-variable)</li>
</ul>

</p>
`,

code: `

`
  },

  { // BEGIN NEW CARD
    topic: 'Types',
    title: 'Checking and testing for types',
    reference: 'http://php.net/manual/en/language.types.intro.php',
description: `
<p>
To check the type and value of an expression, use <code>var_dump()</code>.
</p>

<p>
For human-readable representations, use <code>gettype()</code>.
</p>

<p>
To check for a certain type, use <code>is_int()</code>, <code>is_string()</code> and so on.
</p>
`,

code: `
<?php
$a_bool = TRUE;
$an_int = 12;

echo gettype($a_bool);  // prints: boolean

if (is_int($an_int)) {
    $an_int += 3;
}
?>
`
  },
  
  { // BEGIN NEW CARD
    topic: 'Types',
    title: 'Type casting',
    reference: 'http://php.net/manual/en/language.types.type-juggling.php#language.types.typecasting',
description: `
The name of the desired type is written in parentheses before the variable which is to be cast. Tabs and spaces are allowed inside the parentheses.
`,

code: `
<?php
$a = 10;
$b = (boolean) $a;

/* the following casts are allowed:

(int), (integer)
(bool), (boolean)
(float), (double), (real)
(string)
(binary)  // binary strings
(array)
(object)
(unset)  // cast to NULL

*/
?>
`
  },
  
  { // BEGIN NEW CARD
    topic: 'Booleans',
    title: 'Constants are case-insensitive',
    reference: 'http://php.net/manual/en/language.types.boolean.php',
description: `
A boolean expresses a truth value. TRUE and FALSE are case-insensitive.
`,

code: `

`
  },
  
  
  { // BEGIN NEW CARD
    topic: 'Booleans',
    title: 'False values',
    reference: 'http://php.net/manual/en/language.types.boolean.php',
description: `
The following are considered FALSE:
<ul>
<li>the boolean FALSE</li>
<li>the integer 0</li>
<li>the float 0.0</li>
<li>the empty string and the string "0"</li>
<li>an array with zero elements</li>
<li>an object with zero member variables (PHP 4 only)</li>
<li>the special type NULL and unset variables</li>
<li>SimpleXML objects created from empty tags</li>
</ul>

<b>Warning:</b> any non-zero number (1, -1, and others) are considered TRUE
`,

code: `

`
  },
  
  
  { // BEGIN NEW CARD
    topic: 'Integers',
    title: 'Arbitrary-length integers (GMP)',
    reference: 'http://php.net/manual/en/intro.gmp.php',
description: `
The GMP (GNU Multiple Precision) class is a GMP number. These objects support overloaded arithmetic, bitwise, and comparison operators.
`,

code: `

`
  },
  
  
  { // BEGIN NEW CARD
    topic: 'Integers',
    title: 'Maximum size',
    reference: 'http://php.net/manual/en/language.types.integer.php',
description: `
<code>PHP_INT_SIZE</code> is a constant representing the integer size. <code>PHP_INT_MAX</code> and <code>PHP_INT_MIN</code> are the limits of the integer type.
`,

code: `

`
  },
  
  
  { // BEGIN NEW CARD
    topic: 'Integers',
    title: 'Bases',
    reference: 'http://php.net/manual/en/language.types.integer.php',
description: `
<ul>
<li>Binary: 0b111111</li>
<li>Octal: 0123</li>
<li>Hexadecimal: 0x1A</li>
</ul>
`,

code: `

`
  },
  
  
  { // BEGIN NEW CARD
    topic: 'Integers',
    title: 'Overflow',
    reference: 'http://php.net/manual/en/language.types.integer.php',
description: `
An integer outside the bounds of the integer type will be interpreted as a float.
`,

code: `

`
  },
  
  
  { // BEGIN NEW CARD
    topic: 'Floats',
    title: 'NAN',
    reference: 'http://php.net/manual/en/language.types.float.php',
description: `
<p>
Some numeric operations result in the constant <code>NAN</code>. It represents an undefined or unrepresentable value. Any loose or strict comparisons against any value, including itself, results in <code>FALSE</code>.
</p>

<p>
To check for <code>NAN</code>, use <code>is_nan()</code>
</p>
`,

code: `

`
  },
  

  { // BEGIN NEW CARD
    topic: 'Strings',
    title: 'Characters are limited to a byte',
    reference: 'http://php.net/manual/en/language.types.string.php',
description: `
<p>A string is a series of characters, where a character is a byte. PHP does not natively support Unicode.</p>

<p>If Zend Multibyte is enabled, the PHP script may be written in any encoding.</p>

<p>When writing programs using Unicode, use the <code>intl</code> and <code>mbstring</code> extensions.</p>
`,

code: `

`
  },
  
  { // BEGIN NEW CARD
    topic: 'Strings',
    title: 'Single quoted',
    reference: 'http://php.net/manual/en/language.types.string.php#language.types.string.details',
description: `
This is the simplest way to specify a string. For a literal single quote, escape it with a backslash <code>\\</code>. A literal backslash is a double backslash <code>\\\\</code>. Nothing is interpreted or expanded in a single-quoted string.
`,

code: `

`
  },
  
  { // BEGIN NEW CARD
    topic: 'Strings',
    title: 'Double quoted',
    reference: 'http://php.net/manual/en/language.types.string.php#language.types.string.details',
description: `
<p>
In a double-quoted string, sequences such as <code>\\n</code> have special meaning (in this case, a linefeed). The most important feature is that variable names will be expanded.
</p>
`,

code: `
$name = "Peter";
echo "Hello, $name";
`
  },
  
  { // BEGIN NEW CARD
    topic: 'Arrays',
    title: 'Pre-count array size for a loop',
    reference: 'https://stackoverflow.com/questions/3974385/php-array-count-or-sizeof',
description: `
$size = count($a);

for ($i = 0; $i < $size; $i++) {
    // ...
}
`,

code: `

`
  },
  
  { // BEGIN NEW CARD
    topic: 'Functions',
    title: 'Variable scope',
    reference: '',
description: `
PHP does not have lexical scope. Variables outside the function cannot be accessed, unless <code>global $var;</code> is declared.
`,

code: `

`
  },
  
  { // BEGIN NEW CARD
    topic: '',
    title: '',
    reference: '',
description: `

`,

code: `

`
  },
  
  { // BEGIN NEW CARD
    topic: '',
    title: '',
    reference: '',
description: `

`,

code: `

`
  },
  
  { // BEGIN NEW CARD
    topic: '',
    title: '',
    reference: '',
description: `

`,

code: `

`
  },
  
  { // BEGIN NEW CARD
    topic: '',
    title: '',
    reference: '',
description: `

`,

code: `

`
  },
  
  { // BEGIN NEW CARD
    topic: '',
    title: '',
    reference: '',
description: `

`,

code: `

`
  },
  
  { // BEGIN NEW CARD
    topic: '',
    title: '',
    reference: '',
description: `

`,

code: `

`
  },
  
  { // BEGIN NEW CARD
    topic: '',
    title: '',
    reference: '',
description: `

`,

code: `

`
  },
  
  { // BEGIN NEW CARD
    topic: '',
    title: '',
    reference: '',
description: `

`,

code: `

`
  },
  
  { // BEGIN NEW CARD
    topic: '',
    title: '',
    reference: '',
description: `

`,

code: `

`
  },
  
  { // BEGIN NEW CARD
    topic: '',
    title: '',
    reference: '',
description: `

`,

code: `

`
  },
  
  { // BEGIN NEW CARD
    topic: '',
    title: '',
    reference: '',
description: `

`,

code: `

`
  },
  
  { // BEGIN NEW CARD
    topic: '',
    title: '',
    reference: '',
description: `

`,

code: `

`
  },
  
  { // BEGIN NEW CARD
    topic: '',
    title: '',
    reference: '',
description: `

`,

code: `

`
  },
  
  { // BEGIN NEW CARD
    topic: '',
    title: '',
    reference: '',
description: `

`,

code: `

`
  },
  
  { // BEGIN NEW CARD
    topic: '',
    title: '',
    reference: '',
description: `

`,

code: `

`
  },
  
  { // BEGIN NEW CARD
    topic: '',
    title: '',
    reference: '',
description: `

`,

code: `

`
  },
  

  // END LIST OF CARDS  
];

