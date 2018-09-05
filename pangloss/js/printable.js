var topics = {};

data.forEach(function(card) {
  var topic = card['topic'];
  if(topic.trim() != "") {
    if(!topics[topic]) {
      topics[topic] = [card];
    } else {
      topics[topic] = topics[topic].concat(card);
    }
  }
});

var topicNames = Object.keys(topics).sort(function(a, b) { return a.toLowerCase().localeCompare(b.toLowerCase()) });

function printableCard(card) {
  var cardDiv = document.createElement("div");
  cardDiv.className = "printableCard";
  
  var titleHeader = document.createElement("h3");
  var titleText = card['topic'] + ": " + card['title'];
  var titleTextNode = document.createTextNode(titleText);
  titleHeader.appendChild(titleTextNode);
  cardDiv.appendChild(titleHeader);

  var descriptionPara = document.createElement("p");
  descriptionPara.innerHTML = card['description'];
  cardDiv.appendChild(descriptionPara);

  var codeText = card['code'];
  if (codeText.trim() != "") {
    var codePre = document.createElement("pre");
    var codeTextNode = document.createTextNode(codeText.trim());
    codePre.appendChild(codeTextNode);
    cardDiv.appendChild(codePre);
  }
  
  return cardDiv;
}

topicNames.forEach(function(topicName) {
  var contentDiv = document.getElementById("content");
  
  var cards = topics[topicName];
  cards.sort(function(a, b) { return a['title'].toLowerCase().localeCompare(b['title'].toLowerCase()) });
  cards.forEach(function(card) {
    contentDiv.appendChild(printableCard(card));
  });
});
