def solve(x_in, y_in, z_in, n):
    print([[x, y, z] 
           for x in range(x_in+1)
           for y in range(y_in+1)
           for z in range(z_in+1)
           if x+y+z != n])
