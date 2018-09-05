data = data.concat([

////////////////////////////////////////////////////////////
//
// Calculus
//
////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Calculus',
    title: 'Integration, definite',
    reference: '',
    description: ``,
    code: `
def definite_integral(coeffs, a, b):
    """For the integral of a polynomial with given coefficients,
    where the rightmost element is a constant, second-to-last is x,
    third-to-last is x^2, etc.

    For definite_integral([1, 0, 1], 0, 2),
    the anti-derivative is (1/3)x^3 + x = [1/3, 0, 1]
    """
    anti_derivative = []  # ignore C, constant value
    len_coeffs = len(coeffs)
    for i, coeff in enumerate(coeffs):
        power = len_coeffs - i
        anti_derivative.append(1 / power * coeff)

    # compute anti_derivative with a and b
    len_anti_derivative = len(anti_derivative)
    result = 0
    for i, coeff in enumerate(anti_derivative):
        power = len_anti_derivative - i
        result += coeff * b ** power
        result -= coeff * a ** power
    return result    
    `
  },

  { // begin new topic
    topic: 'Calculus',
    title: 'Differentiation',
    reference: '',
    description: `Given an array of coefficients, where the rightmost element is a constant, second-to-last is x, third-to-last is x^2, etc. find the derivative`,
    code: `
def differentiate(coeffs):
    """Differentiate 2x^3 - 4x^2 + 10 (given as [2, -4, 0, 10]).
    The result is 6x^2 - 8x. [6, -8, 0]
    """
    len_terms = len(coeffs)
    result = []
    for i, coeff in enumerate(coeffs[:-1]):
        power = len_terms - i - 1
        result.append(power * coeff)
    return result    
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
