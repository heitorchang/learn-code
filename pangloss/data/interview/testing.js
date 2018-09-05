data = data.concat([

////////////////////////////////////////////////////////////
//
// TESTING
//
////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Testing',
    title: 'assert (simple testing)',
    reference: '',
    description: ``,
    code: `
def f(x):
    return x + 1

def test():
    """
    Message string after assertion is optional, will appear on failure.
    Display "OK" at the end to indicate success.
    Call test() in interactive session.
    """
    assert f(99) == 100, "f of 99"
    assert f(f(9)) == 11, "Chain of f"
    assert f(f(0)) == 2
    print("OK")
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
