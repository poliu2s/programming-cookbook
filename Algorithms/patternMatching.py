# A sorted array has been rotated so that the elements might appear in the order
# 3456712. How would you find the minimum element? You may assume
# that the array has all unique elements

problem = [ 3,4,5,6,7,1,2 ]
problem2 = [ 4,5,6,7,8,9,10,1,2,3]


def solve(input):
    print input
    midpoint = (len(input) - 1) / 2
    endpoint = len(input) - 1

    print "midpoint: " + str(input[midpoint])
    print "endpoint: " + str(input[endpoint])
    if len(input) == 2:
        return input[1]

    elif input[midpoint] > input[endpoint]:
        print 'going right'
        solve([input[i] for i in range(midpoint, endpoint + 1)])
    else:
        print 'going left'
        solve([input[i] for i in range(0, midpoint + 1)])

solve(problem2)