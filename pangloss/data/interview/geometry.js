data = data.concat([

  { // begin new topic
    topic: 'Geometry',
    title: 'Law of cosines',
    reference: 'https://en.wikipedia.org/wiki/Law_of_cosines',
    description: `The law of cosines relates the lengths of a triangle's sides to the cosine of one of its angles.`,
    code: `
from math import cos, sqrt

def sideLen(a, b, angleC):
    return sqrt(a**2 + b**2 - 2*a*b*cos(angleC))
    `
  },

  { // begin new topic
    topic: 'Geometry',
    title: 'Radians to degrees',
    reference: '',
    description: ``,
    code: `
from math import pi
    
def radToDeg(r):
    return r / pi * 180
    `
  },

  { // begin new topic
    topic: 'Geometry',
    title: 'Degrees to radians',
    reference: '',
    description: ``,
    code: `
from math import pi
    
def degToRad(d):
    return d / 180 * pi
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
