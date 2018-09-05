"use strict";

function dashed(s) {
  // return s.toLowerCase().replace(/ /g, "-").replace(/\//g, "-").replace(/'/g, "-");
  return s.toLowerCase().replace(/[\W_]/g, "-");
}

var menuDisplay = {};
var dataCapsule = {};

// assign data entries to their topics
for (var i = 0; i < data.length; i++) {
  var entry = data[i];
  var id = dashed(entry.topic);
  
  if (!dataCapsule.hasOwnProperty(id)) {
    dataCapsule[id] = [entry];
    menuDisplay[id] = entry.topic;
  } else {
    dataCapsule[id].push(entry);
  }
}
  

function displayPanels(entries) {
  clearPanels();
  for (var i = 0; i < entries.length; i++) {
    var entry = entries[i];
    if (entry.topic !== "") {
      var hashId = entry.topic.toLowerCase() + "-" + entry.title.toLowerCase().replace(/ /g, "-");
      addPanel(hashId, entry.title, entry.description, entry.code);
    }
  }
}

function sortAndBuildMenu(dataCapsule) {
  var menuItems = [];

  for (var topic in dataCapsule) {
    if (topic !== "") {
      menuItems.push(topic);
    }
  }

  menuItems.sort();

  for (var i = 0; i < menuItems.length; i++) {
    var entry = menuItems[i];
    addListItem("menuList", dashed(entry), menuDisplay[dashed(entry)]);
  }
}

function buildSubmenu(id) {
  clearSubmenu();
  clearPanels();
  
  var entries = dataCapsule[id];

  entries.sort(function (a, b) {
    return a.title.toLowerCase() <= b.title.toLowerCase() ? -1 : 1;
  });
               
  for (var i = 0; i < entries.length; i++) {
    var entry = entries[i];
    var id = getMenuActive() + "-" + dashed(entry.title)
    addListItem("submenuList", id, entry.title);
    addPanel(id, entry.title, entry.description, entry.code, entry.reference);
  }

  menuInteract();
}

sortAndBuildMenu(dataCapsule);

