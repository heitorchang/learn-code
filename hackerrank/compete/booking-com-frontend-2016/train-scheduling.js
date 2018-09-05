// Aug. 5, 2016

// As you leave your hotel, you check the train schedule and notice it's bugged — you can't see when the trains are arriving! Because you need to know the exact order of arrival of each train, you hack around the page and find a series of instructions that must be parsed by a JavaScript compiler code in order to display the arrival messages.
// 
// The compiler displays these messages using the  statement. If there's a programmed delay to display it, that statement is wrapped inside a  function. The compiler also trims any trailing spaces from the messages and appends a  at the end of every  statement messages.
// 
// There is specific syntax for writing code for the compiler. For example:
// 
// msg : () is used for
// console.log(msg)
// msg : (a) is used for
// setTimeout(function() {
//     console.log(msg);
// }, a);
// msg : ((a)b) is used for
// setTimeout(function() {
//     setTimeout(function() {
//         console.log(msg);
//     }, a);
// }, b);
// msg : (((a)b)c) is used for
// setTimeout(function() {
//     setTimeout(function() {
//         setTimeout(function() {
//             console.log(msg);
//         }, a);
//     }, b);
// }, c);
// Given  valid codes, print the correctly compiled output for each code on a new line.
// 
// Note 
// You are not allowed to use setTimeout function call in your code.
// 
// Input Format
// 
// The first line contains a single integer, , denoting the total number of  statements. 
// Each of the  subsequent lines contains code for a  statement.
// 
// Constraints
// 1 <= n <= 200
// 100 nested calls

// msg is a string consisting of lowercase English letters (), numbers, and spaces.
// The length of msg is not greater than .
// It is guaranteed that no  is delayed for more than  seconds.
// It is guaranteed that no two  statements will be delayed for the same amount of time.
// There will be no more than  nested  function calls.
// Output Format
// 
// Print the output of the code after successful execution.
// 
// 
// 

let schedule = [];

let runEvents = () => {
  if (schedule.length > 0) {
    let firstTime = schedule.findIndex(n => n !== undefined);
    let queue = schedule[firstTime];
    if (queue !== undefined) {
      for (var i = 0, end = queue.length; i < end; i++) {
  	    queue[i]();
      }
      
      // reduce index (let time pass)
      schedule[firstTime] = undefined;
      let nextTime = schedule.findIndex(n => n !== undefined);
      schedule = schedule.slice(nextTime);
      runEvents();
    }
  }
}

let addToSchedule = (item, time) => {
  if (schedule[time] === undefined) {
    schedule[time] = [item];
  } else {
    schedule[time].push(item);
  }
}

let printMsg = msg => {
  console.log(msg.trim() + ".");
}

let parseLine = inputLine => {
  let parts = inputLine.split(":");
  let msg = parts[0].trim();
  
  let commands = parts[1].trim();
  let tmoutValues = commands.replace(/[()]/g, " ").trim();
  if (tmoutValues.length === 0) {
    tmoutValues = "0";
  }
  
  let tmoutList = tmoutValues.split(" ");
  tmoutList = tmoutList;
  tmoutList.push(msg);
  return tmoutList;
}

// lst is a list of times and the message
let buildCommand = lst => {
  if (lst) {
    if (lst.length === 2) {
      addToSchedule(() => printMsg(lst[1]), parseInt(lst[0], 10));
    } else {
      addToSchedule(() => buildCommand(lst.slice(1)), parseInt(lst[0], 10))
    }
  }
}

function processData(input) {
  let lines = input.split("\n");
  for (var i = 1, end = lines.length; i < end; i++) {
    buildCommand(parseLine(lines[i]));             
  }
  runEvents();
}

process.stdin.resume();
process.stdin.setEncoding("ascii");
_input = "";
process.stdin.on("data", function (input) {
  _input += input;
});

process.stdin.on("end", function () {
  processData(_input);
});
