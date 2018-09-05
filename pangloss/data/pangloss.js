// Use text-mode

var data = [

  {
    topic: 'Cards',
    title: 'Recording information',
    reference: '',
    description: 'Each language page refers to a single data file saved in the <code>data</code> folder. A card is an object in the <code>data</code> array.',
    code: `
    {  // BEGIN NEW CARD
      topic: '',
      title: '',
      reference: '',    // an URL or book and page number
      description: \`\`,  // a template string, HTML may be used
      code \`\`,  // special characters are escaped 
    }`
    },

  {
    topic: 'Pages',
    title: 'Setting up a new page',
    reference: '',
    description: `
      <p>
      Start with <code>template.html</code> and replace LANGUAGE with the new language's name. Also, replace <code>LANGUAGE.js</code> with an appropriate name for the language's note cards.
      </p>

      <p>
      Add the new language's filename and display name to <code>js/languageDropdown.js</code>
    </p>

      <p>
      Following the example of <code>data/LANGUAGE.js</code>, create note cards for the new language.
      </p>

`,
    code: `
// js/languageDropdown.js
var languages = {
  mylang: "My Language",
};
    `
  },

  { // begin new topic
    topic: 'Layout',
    title: 'Material Design theme',
    reference: 'http://fezvrasta.github.io/bootstrap-material-design/',
    description: 'The theme is "Bootstrap Material Design" by Fezvrasta',
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

