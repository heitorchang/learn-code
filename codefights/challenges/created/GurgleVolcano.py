import numpy as np
from scipy import sparse

#   0 1 2
#   S L G        
# 3 L L L 5
# 6 L L F 8
#     7

#  0 1 2 3 4 5 6 7 8
g = [
  [None,1,None,1,None,None,None,None,None],
  [0,None,0,None,1,None,None,None,None],
  [None,1,None,None,None,1,None,None,None],
  [0,None,None,None,1,None,1,None,None],
  [None,1,None,1,None,1,None,1,None],
    [None,None,0,None,1,None,None,None,0],
  [None,None,None,1,None,None,None,1,None],
  [None,None,None,None,None,None,1,None,1],
  [None,None,None,None,None,1,None,1,None]]


g = [
  [0,2,0,2,0,0,0,0,0],
  [1,0,1,0,2,0,0,0,0],
  [0,2,0,0,0,2,0,0,0],
  [1,0,0,0,2,0,2,0,0],
  [0,2,0,2,0,2,0,2,0],
  [0,0,1,0,2,0,0,0,1],
  [0,0,0,2,0,0,0,2,0],
  [0,0,0,0,0,0,2,0,2],
  [0,0,0,0,0,2,0,2,0]]

# 012
# SLL
# LGF
# 345

# [[n,1,n,1,n,n],
#  [0,n,1,n,0,n],
#  [n,1,n,n,n,0],
#  [0,n,n,n,0,n],
#  [n,1,n,1,n,0],
#  [n,n,1,n,0,n]]

row_ind = np.array([0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5]) # from
col_ind = np.array([1, 3, 0, 2, 4, 1, 5, 0, 4, 1, 3, 5, 2, 4]) # to
data =    np.array([1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0]) # lava?

mat_coo = sparse.coo_matrix((data, (row_ind, col_ind)))
