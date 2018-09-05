data = data.concat([

////////////////////////////////////////////////////////////
//
// SEARCHING
//
////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Searching',
    title: 'Binary search',
    reference: 'http://code.activestate.com/recipes/81188-binary-search/',
    description: ``,
    code: `
def binarySearch(arr, x):
    # returns the index of x in arr, or -1 if not found
    # arr must be sorted
    left = 0
    right = len(arr) - 1
    while True:
        if right < left:
            return -1

        midpoint = (left + right) // 2
        if arr[midpoint] < x:
            left = midpoint + 1
        elif arr[midpoint] > x:
            right = midpoint - 1
        else:
            return midpoint    
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
    `
  },


]);
