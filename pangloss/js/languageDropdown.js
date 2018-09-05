var languages = {
  php: "PHP",
  js: "JavaScript",
  py: "Python",
  julia: "Julia",
  sql: "SQL",
  clojure: "Clojure",
  scheme: "Scheme",
  interview: "Interviews (Python)",
  django: "Django",
  angular: "Angular",
};

// http://stackoverflow.com/questions/9658690/is-there-a-way-to-sort-order-keys-in-javascript-objects
Object.keys(languages).sort().forEach(function(key) {
  $("#languageList").append(`<li><a href='${key}.html'>${languages[key]}</a></li>`);
});
