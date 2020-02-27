from math import sin, cos
def funcDeriv(p:int):
    return 1 - cos(p)
def func(p:int):
    return p - sin(p)
def newtonMethod(p_0:int, error=10e-6):
    count = 1
    curr_p = p_0 - (func(p_0)/funcDeriv(p_0))
    prev_p = p_0
    while( abs(curr_p - prev_p) >= error and count <10):
        print("This is iteration: " + str(count) + " The current approximation is: " + str(curr_p))
        temp = curr_p
        curr_p = curr_p - (func(curr_p)/funcDeriv(curr_p))
        prev_p = temp
        count += 1
    print("This is the last iteration: " + str(count) + " The closest approximation so far is: " + str(curr_p))
if __name__ == '__main__':
    p_0 = float(input())
    newtonMethod(p_0)

'''
.5
This is iteration: 1 The current approximation is: 0.3319319394891097
This is iteration: 2 The current approximation is: 0.2208800007036197
This is iteration: 3 The current approximation is: 0.14713338829825784
This is iteration: 4 The current approximation is: 0.09805350728312182
This is iteration: 5 The current approximation is: 0.06535852642976443
This is iteration: 6 The current approximation is: 0.04356924831945554
This is iteration: 7 The current approximation is: 0.02904524652169955
This is iteration: 8 The current approximation is: 0.019363225413648648
This is iteration: 9 The current approximation is: 0.012908736275343655
This is the last iteration: 10 The closest approximation so far is: 0.008605800282829226


This is for problem 3 part 2 with the different Newton's method with multiplicity m known.
TThis is iteration: 1 The current approximation is: -0.00420418153267077
This is iteration: 2 The current approximation is: 2.4769199157004262e-09

This new Newton's method converges very very close to 0 but converges nearly as fast as the modified Newton's method.
'''
