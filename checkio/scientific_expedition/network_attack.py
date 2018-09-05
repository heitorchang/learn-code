def capture(matrix):
    num_computers = len(matrix)
    time_left = []
    elapsed_time = 0

    # build list of time left to complete infection
    for row in range(len(matrix)):
        time_left.append(matrix[row][row])

    infected = [0] * num_computers
    touched = [0] * num_computers

    # starting condition
    infected[0] = 1
    touched[0] = 1
    
    while sum(infected) < num_computers:
    # while elapsed_time < 10:
        # inefficient method, repeatedly checks and adds computers

        # connect neighbors
        for i in range(num_computers):            
            if touched[i] == 1:
                links = matrix[i]
                for j, link in enumerate(links):
                    if link == 1 and infected[i] == 1:
                        touched[j] = 1

        # add 1 second to time
        for i, t in enumerate(touched):
            if t == 1:
                time_left[i] -= 1

        # check times left
        for i, t in enumerate(time_left):
            if t <= 0:
                infected[i] = 1
        elapsed_time += 1
    return elapsed_time

    """
        print(elapsed_time, time_left, touched, infected)

    print()
    print(elapsed_time)

    # return elapsed_time
    """

def test():
    #These "asserts" using only for self-checking and not necessary for auto-testing

    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 4, "Low security"

    assert capture([[0, 1, 1],
                    [1, 9, 1],
                    [1, 1, 9]]) == 9, "Small"

    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 8, "Base example"

    assert capture([[0,1,0],
                    [1,9,1],
                    [0,1,9]]) == 18, "edge"
                    

    print("all ok")
