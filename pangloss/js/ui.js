function clearPanels() {
  $("#panels").html("");
}


function clearMenu() {
  $("#menuList").html("");
}

function clearSubmenu() {
  $("#submenuList").html("");
}

function clearPanels() {
  $("#panels").html("");
}

function clearAll() {
  clearMenu();
  clearSubmenu();
  clearPanels();
}

function addPanel(id, header, desc, code, ref) {

  // if description is an url, make it clickable
  var domains = ['.co', '.ne', '.or', '.ed', '.br', '.go', '.mi', '.io'];
  var domainsLen = domains.length;
  
  function wordContainsDomain(word) {
    for (var i = 0; i < domainsLen; i++) {
      if (word.indexOf(domains[i]) !== -1) {
        return true;
      }
    }
    return false;
  }

  var referenceSpan = "";

  if (ref !== "") {
  
    var refWords = ref.split(" ");
    
    var refWithLinks = "";
    
    for (var i = 0, len = refWords.length; i < len; i++) {
      var currentWord = refWords[i];
      if (wordContainsDomain(currentWord)) {
        if (currentWord.substr(0, 4) !== "http") {
          currentWord = "http://" + currentWord;
        }
        refWithLinks += '<a href="' + currentWord + '" target="_blank">' + currentWord + '</a> ';
      } else {
        refWithLinks += currentWord + " ";
      }
    }
 
    referenceSpan = `<span class="panel-ref"><i>Reference:</i>
      ${refWithLinks}
    </span>`;
  }
    
  code = code.substring(1).trimRight();

  if (code.length > 0) {
    code = "<pre>" + _.escape(code) + "</pre>";
  } 

  $("#panels").append(`
                      <div class="panel panel-primary" id="${id}">
                      <div class="panel-heading">
                      <h3 class="panel-title">${header}</h3>
                      </div>
                      <div class="panel-body" id="panelBody">
                      <p>
                      ${desc}
                      </p>
                      ${code}
                      ${referenceSpan}
                      </div>
                      </div>
                      `);
}

function addListItem(menuId, dataTarget, desc) {
  // if dataTarget already exists, do nothing
  if ($("#" + menuId).find("li[data-target='" + dataTarget + "']").length > 0) {
    console.log("Data target " + dataTarget + " for " + menuId + " already exists.");
    return;
  }
  
  $("#" + menuId).append(`
                         <li class="withripple" data-target="${dataTarget}">${desc}</li>
                         `);
}


function menuInteract() {
  
  $(".menu li").click(function () {
    if (!$(this).data("target")) return;
    if ($(this).is(".active")) return;
    $(".menu li").not($(this)).removeClass("active");
    $(".page").not(page).removeClass("active").hide();
    window.page = $(this).data("target");
    var page = $(window.page);
    window.location.hash = window.page;
    $(this).addClass("active");

    // console.log($(this).data("target") + " menu item clicked");
    buildSubmenu($(this).data("target"));    
    
    page.show();

    var totop = setInterval(function () {
      $(".pages").animate({scrollTop: 0}, 0);
    }, 1);

    setTimeout(function () {
      page.addClass("active");
      setTimeout(function () {
        clearInterval(totop);
      }, 1000);
    }, 100);

    $(".panels").animate({scrollTop: 0}, 0);
  });

  $(".submenu li").click(function () {
    if (!$(this).data("target")) return;
    if ($(this).is(".active")) return;
    $(".submenu li").not($(this)).removeClass("active");
    $(".page").not(page).removeClass("active").hide();
    window.page = $(this).data("target");
    var page = $(window.page);
    window.location.hash = window.page;
    $(this).addClass("active");

    page.show();

    var totop = setInterval(function () {
      $(".pages").animate({scrollTop: 0}, 0);
    }, 1);

    setTimeout(function () {
      page.addClass("active");
      setTimeout(function () {
        clearInterval(totop);
      }, 1000);
    }, 100);
  });

  $.material.init();
  
}         

function getMenuActive() {
  return $("#menuList .active").first().attr("data-target");
}

function changeFavicon(src) {
  var link = document.createElement('link'),
  oldLink = document.getElementById('dynamic-favicon');
  link.id = 'dynamic-favicon';
  link.rel = 'shortcut icon';
  link.href = src;
  if (oldLink) {
    document.head.removeChild(oldLink);
  }
  document.head.appendChild(link);
}

changeFavicon("favicon.ico");
