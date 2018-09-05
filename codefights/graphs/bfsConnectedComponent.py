def traverse(matrix, visited, node, count):
    visited[node] = True
    for i, n in enumerate(matrix[node]):
        if n and visited[i] == False:  # n is the True/False in matrix
            return traverse(matrix, visited, i, count + 1)
    return count + 1

def bfsComponentSize(matrix):
    return traverse(matrix, [False for _ in range(len(matrix))], 1, 0)


assaf_r_solution = """
​
// JavaScript
function bfsComponentSize(matrix) {
  V = []  // visited
  Q = [1] // queue
  V[1] = true

  count = 0

  while(Q.length) {
    q = Q.pop()
    count++

    for (x in matrix[q]) {
      if (matrix[q][x] && !V[x]) {
        V[x] = true
        Q.push(x)
      }
    }
  }

  return count
}

"""
  
