data = data.concat([

  { // begin new topic
    topic: 'Datetime',
    title: 'now, today',
    reference: '',
    description: ``,
    code: `
from datetime import datetime, date

now = datetime.now()
# datetime.datetime(2017, 10, 30, 19, 50, 29, 702774)

today = date.today()
# datetime.date(2017, 11, 7)
    `
  },

  { // begin new topic
    topic: 'Datetime',
    title: 'Format date with strftime',
    reference: '',
    description: `The mnemonic for strftime and strptime is that 'f' stands for format, and 'p' stands for parse`,
    code: `
from datetime import date, datetime
dt = datetime(2017, 10, 15, 23, 22)
d = date(2017, 2, 15)

print(dt.strftime("%H:%M %d/%m/%y"))  # 23:22 15/10/17
print(d.strftime("%d/%m/%y"))  # 15/02/17
    `
  },

  { // begin new topic
    topic: 'Datetime',
    title: 'Parse date with strptime',
    reference: '',
    description: `The mnemonic for strftime and strptime is that 'f' stands for format, and 'p' stands for parse. strptime is a class method of datetime.datetime.`,
    code: `
from datetime import datetime
d = datetime.strptime("02/15/97", "%m/%d/%y")
# datetime.datetime(1997, 2, 15, 0, 0) 
    `
  },

  { // begin new topic
    topic: 'Datetime',
    title: 'Weekdays',
    reference: '',
    description: `weekday() may be called by both a date and a datetime.<br><br>0 = Mon, 1 = Tue, 2 = Wed, 3 = Thu, 4 = Fri, 5 = Sat, 6 = Sun<br><br>For weekday names, use <code>calendar.day_name</code> or <code>calendar.day_abbr</code>. Convert them to lists if needed.`,
    code: `
from datetime import date
from calendar import day_abbr

d = date(2017, 11, 30)
print(day_abbr[d.weekday()])  # Thu
    `
  },

]);
