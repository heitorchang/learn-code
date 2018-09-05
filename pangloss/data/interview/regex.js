data = data.concat([


//////////////////////////////////////////////////////////////////////
//
// REGEX
//
//////////////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Regex',
    title: 'Substitutions',
    reference: 'https://docs.python.org/3/howto/regex.html',
    description: `Replace all matches with a given replacement value<br><br>

sub(replacement, originalString, count=0)
<br><br>

subn(replacement, originalString, count=0) does the same thing, but returns a tuple of the new string and the number of replacements
`,
    code: `
p = re.compile(r'(blue|white|red)')
p.sub('color', 'blue socks and red shoes')
# 'color socks and color shoes'
    `
  },

  { // begin new topic
    topic: 'Regex',
    title: 'Groups (parenthesized)',
    reference: 'https://docs.python.org/3/howto/regex.html',
    description: `A match can be divided into groups, indicated by parentheses. Groups are numbered by counting opening parentheses from left to right.
<br><br>
matchObject.groups() returns a tuple of the strings from group 1 and up.
`,
    code: `
p = re.compile('(a(b)c)d')
m = p.match("abcd")
m.group(0)  # 'abcd'
m.group(1)  # 'abc'
m.group(2)  # 'b'
    `
  },

  { // begin new topic
    topic: 'Regex',
    title: 'Special sequences',
    reference: 'https://docs.python.org/3/howto/regex.html',
    description: `<p>The capitalized version of a special sequence is the inverse (\\d are digits, \\D are non-digits).</p>

<p>
<code>\\d</code> is any decimal digit, [0-9]
</p>

<p>
<code>\\s</code> is any whitespace character, [ \\t\\n\\r\\f\\v]
</p>

<p>
<code>\\w</code> is any alphanumeric character, [a-zA-Z0-9_]
</p>

<p>
| 'or' operator
</p>

<p>
^ matches the beginning of lines
</p>

<p>
$ matches the end of a line
</p>

<p>
\\A matches the start of the string
</p>

<p>
\\Z matches the end of the string
</p>

<p>
\\b word boundary
</p>

`,
    code: `    
    `
  },

  { // begin new topic
    topic: 'Regex',
    title: 'Repetition',
    reference: 'https://docs.python.org/3/howto/regex.html',
    description: `
<p>
* represents greedy repetition of the preceding character (zero or more times)
</p>

<p>
+ matches one or more times
</p>

<p>
? matches either zero or one time
</p>

<p>
{m,n} matches at least m and at most n times (endpoints are included)
</p>

<p>
To make a qualifier non-greedy, add a ? to its right, *?, +?, ??, and {m,n}?. They will match as little text as possible.
</p>
`,
    code: `
    `
  },

  { // begin new topic
    topic: 'Regex',
    title: 'Compiling or using module-level functions',
    reference: 'https://docs.python.org/3/howto/regex.html',
    description: `Compiling a pattern will save some function calls. Flags control the behavior of the RE.
<p>
ASCII (A) \\w, \\b, \\s, \\d match only ASCII characters
</p>

<p>
DOTALL (S) . matches any character, including newlines
</p>

<p>
IGNORECASE (I) case-insensitive matches
</p>

<p>
LOCALE (L) locale-aware match
</p>

<p>
MULTILINE (M) multi-line matching, affecting ^ and $
</p>

<p>
VERBOSE (X) enable verbose REs, which may be organized more clearly
</p>

`,
    code: `
import re

pat = re.compile(r'From\s+')
pat.match('From amk')  # <_sre.SRE_Match object ...>

re.match(r'From\s+', 'From amk')  # <_sre.SRE_Match object ...>
    `
  },


  { // begin new topic
    topic: 'Regex',
    title: 'Raw string',
    reference: 'https://docs.python.org/3/howto/regex.html',
    description: `A raw string is prefixed with an r. Everything is taken literally, so there is no need to escape backslashes.<br><br><code>s = r'\\\\section'</code>`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Regex',
    title: 'Matching',
    reference: 'https://docs.python.org/3/howto/regex.html',
    description: `
<p>
match() determines if the RE matches at the beginning of the string
</p>

<p>
search() looks for a match anywhere in the string
</p>

<p>
findall() finds all substrings and returns them as a list
</p>

<p>
finditer() finds all substrings and returns them as an iterator
</p>
`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Regex',
    title: 'Match object',
    reference: 'https://docs.python.org/3/howto/regex.html',
    description: `When a match is found, a match object is returned.`,
    code: `
pat = re.compile(r'[a-z]*')
m = pat.match("joe123")
m.group()  # "joe"
m.start(), m.end()  # (0, 3)
m.span()  # (0, 3)
    `
  },

  { // begin new topic
    topic: 'Regex',
    title: 'Backreferences',
    reference: 'https://docs.python.org/3/howto/regex.html',
    description: `A backreference allows you to specify that the contents of an earlier capturing group must also be found at the current location. \\1 will succeed if the contents of group 1 can be found at the current position.`,
    code: `
p = re.compile(r'(\\b\\w+)\\s+\\1')
p.search("Paris in the the spring").group()  # 'the the'
    `
  },

  { // begin new topic
    topic: 'Regex',
    title: 'Non-capturing group',
    reference: 'https://docs.python.org/3/howto/regex.html',
    description: `(?:...) where ... is a regex, denotes a part of a RE, but where we are not interested in the group's contents.
`,
    code: `
    `
  },

  { // begin new topic
    topic: 'Regex',
    title: 'Named groups',
    reference: 'https://docs.python.org/3/howto/regex.html',
    description: `(?P&lt;name&gt;...) allows you to retrieve the group's contents by its name`,
    code: `
p = re.compile(r'(?P<word>\\b\\w+\\b)')
m = p.search('(( lots of punctuation ))')
m.group('word')  # 'lots'
    `
  },

  { // begin new topic
    topic: 'Regex',
    title: 'Lookahead assertions',
    reference: 'https://docs.python.org/3/howto/regex.html',
    description: `
    <p>
    (?=...) is a positive lookahead assertion. It succeeds if the contained RE ... successfully matches at the current location. The matching engine does not advance. The rest of the pattern is tried where the assertion started.
    </p>

<p>
(?!...) is a negative lookahead assertion. It succeeds if the RE ... doesn't match at the current position.
</p>
    `,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Regex',
    title: 'Splitting a string',
    reference: 'https://docs.python.org/3/howto/regex.html',
    description: `split(string, maxsplit=0) will split the string where the RE was found.
`,
    code: `
p = re.compile(r'\d+')
p.split('a1b2c3')  # ['a', 'b', 'c', '']
    `
  },

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: `
`,
    code: `
    `
  },


  ]);
