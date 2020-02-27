from math import sin, cos
def func2ndDeriv(p:int):
    return sin(p)
def funcDeriv(p:int):
    return 1 - cos(p)
def func(p:int):
    return p - sin(p)
def newtonMethod(p_0:int, error=10e-6):
    count = 1
    curr_p = p_0 - ((func(p_0)*funcDeriv(p_0))/((funcDeriv(p_0)*funcDeriv(p_0)) - func(p_0)*func2ndDeriv(p_0)))
    prev_p = p_0
    while( abs(curr_p - prev_p) >= error and count <10):
        print("This is iteration: " + str(count) + " The current approximation is: " + str(curr_p))
        temp = curr_p
        curr_p = curr_p - ((func(curr_p)*funcDeriv(curr_p))/((funcDeriv(curr_p)*funcDeriv(curr_p)) - func(curr_p)*func2ndDeriv(curr_p)))
        prev_p = temp
        count += 1
    print("This is the last iteration: " + str(count) + " The closest approximation so far is: " + str(curr_p))
if __name__ == '__main__':
    p_0 = float(input())
    newtonMethod(p_0)

'''
.5
This is iteration: 1 The current approximation is: 0.008274056887745018
This is iteration: 2 The current approximation is: 3.776298919053178e-08
This is the last iteration: 3 The closest approximation so far is: 1.5022020879298054e-08

I noticed that the modified Netwon's method converges significantly faster than the regular Netwon's method. The tradeoff
seems worth it!
'''