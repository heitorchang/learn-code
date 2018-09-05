data = data.concat([

  { // begin new topic
    topic: 'Time',
    title: 'timeit',
    reference: 'https://runestone.academy/runestone/static/pythonds/AlgorithmAnalysis/Lists.html',
    description: `The timeit module allows you to measure how long a procedure takes to complete.<br><br>t = Timer(statement/function to be repeatedly called, setup statement)<br><br>t.timeit(number=repetitions)`,
    code: `
from timeit import Timer

def test1():
    s = 0
    for i in range(100):
        s += i
    return s
    
t = Timer("test1()", "from __main__ import test1")
print(t.timeit(number=1000), "seconds")
    `
  },

  { // begin new topic
    topic: 'Time',
    title: 'Time since Epoch',
    reference: '',
    description: ``,
    code: `
from time import time

time()
    `
  },

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
    `
  },

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
    `
  },

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
    `
  },

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
    `
  },


]);
