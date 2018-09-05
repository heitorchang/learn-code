from datetime import date, timedelta

def buildPyCal(month, year):
    curDay = date(year, month, 1)
    stop = False
    pyCal = []
    startWkdy = curDay.weekday()
    print(startWkdy)
    if startWkdy != 0:
        pyCal.append([-1 for _ in range(7)])
    
    while True:
        if curDay.month != month:
            break
        curWkdy = curDay.weekday()
        if curWkdy == 0:
            pyCal.append([-1 for _ in range(7)])
        calDay = curDay.strftime("%d")
        if calDay[0] == "0":
            calDay = calDay[1]
        pyCal[-1][curWkdy] = calDay
        curDay += timedelta(days=1)
    return pyCal
    
def websiteCalendar(month, year):
    pyCal = buildPyCal(month, year)
    firstDay = date(year, month, 1)
    monthHeader = firstDay.strftime("%B %Y")
    tableHeader = "<table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" class=\"month\"><tr><th colspan=\"7\" class=\"month\">%s</th></tr><tr><th class=\"mon\">Mon</th><th class=\"tue\">Tue</th><th class=\"wed\">Wed</th><th class=\"thu\">Thu</th><th class=\"fri\">Fri</th><th class=\"sat\">Sat</th><th class=\"sun\">Sun</th></tr>" % (monthHeader)

    # output table rows
    tableRows = ""
    classes = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
    for row in pyCal:
        tableRows += "<tr>"
        for i in range(7):
            col = row[i]
            if col == -1:
                cls = "noday"
                td = "&nbsp;"
            else:
                cls = classes[i]
                td = col
            tableRows += "<td class=\"%s\">%s</td>" % (cls, td)
        tableRows += "</tr>"
        
    print(tableRows)
    return tableHeader + tableRows + "</table>"
    
def test():
    testeql(websiteCalendar(2, 2096), "<table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" class=\"month\"><tr><th colspan=\"7\" class=\"month\">February 2096</th></tr><tr><th class=\"mon\">Mon</th><th class=\"tue\">Tue</th><th class=\"wed\">Wed</th><th class=\"thu\">Thu</th><th class=\"fri\">Fri</th><th class=\"sat\">Sat</th><th class=\"sun\">Sun</th></tr><tr><td class=\"noday\">&nbsp;</td><td class=\"noday\">&nbsp;</td><td class=\"wed\">1</td><td class=\"thu\">2</td><td class=\"fri\">3</td><td class=\"sat\">4</td><td class=\"sun\">5</td></tr><tr><td class=\"mon\">6</td><td class=\"tue\">7</td><td class=\"wed\">8</td><td class=\"thu\">9</td><td class=\"fri\">10</td><td class=\"sat\">11</td><td class=\"sun\">12</td></tr><tr><td class=\"mon\">13</td><td class=\"tue\">14</td><td class=\"wed\">15</td><td class=\"thu\">16</td><td class=\"fri\">17</td><td class=\"sat\">18</td><td class=\"sun\">19</td></tr><tr><td class=\"mon\">20</td><td class=\"tue\">21</td><td class=\"wed\">22</td><td class=\"thu\">23</td><td class=\"fri\">24</td><td class=\"sat\">25</td><td class=\"sun\">26</td></tr><tr><td class=\"mon\">27</td><td class=\"tue\">28</td><td class=\"wed\">29</td><td class=\"noday\">&nbsp;</td><td class=\"noday\">&nbsp;</td><td class=\"noday\">&nbsp;</td><td class=\"noday\">&nbsp;</td></tr></table>")

    testeql(websiteCalendar(9, 1986), "<table border=\"0\" cellpadding=\"0\" cellspacing=\"0\" class=\"month\"><tr><th colspan=\"7\" class=\"month\">September 1986</th></tr><tr><th class=\"mon\">Mon</th><th class=\"tue\">Tue</th><th class=\"wed\">Wed</th><th class=\"thu\">Thu</th><th class=\"fri\">Fri</th><th class=\"sat\">Sat</th><th class=\"sun\">Sun</th></tr><tr><td class=\"mon\">1</td><td class=\"tue\">2</td><td class=\"wed\">3</td><td class=\"thu\">4</td><td class=\"fri\">5</td><td class=\"sat\">6</td><td class=\"sun\">7</td></tr><tr><td class=\"mon\">8</td><td class=\"tue\">9</td><td class=\"wed\">10</td><td class=\"thu\">11</td><td class=\"fri\">12</td><td class=\"sat\">13</td><td class=\"sun\">14</td></tr><tr><td class=\"mon\">15</td><td class=\"tue\">16</td><td class=\"wed\">17</td><td class=\"thu\">18</td><td class=\"fri\">19</td><td class=\"sat\">20</td><td class=\"sun\">21</td></tr><tr><td class=\"mon\">22</td><td class=\"tue\">23</td><td class=\"wed\">24</td><td class=\"thu\">25</td><td class=\"fri\">26</td><td class=\"sat\">27</td><td class=\"sun\">28</td></tr><tr><td class=\"mon\">29</td><td class=\"tue\">30</td><td class=\"noday\">&nbsp;</td><td class=\"noday\">&nbsp;</td><td class=\"noday\">&nbsp;</td><td class=\"noday\">&nbsp;</td><td class=\"noday\">&nbsp;</td></tr></table>")
