from math import sin, cos
def funcDeriv(p:int):
    return 1 - cos(p)
def func(p:int):
    return p - sin(p)
def newtonMethod(p_0:int, error=10e-6):
    count = 1
    curr_p = p_0 - (3*func(p_0)/funcDeriv(p_0))
    prev_p = p_0
    while( abs(curr_p - prev_p) >= error and count <10):
        print("This is iteration: " + str(count) + " The current approximation is: " + str(curr_p))
        temp = curr_p
        curr_p = curr_p - (3*func(curr_p)/funcDeriv(curr_p))
        prev_p = temp
        count += 1
    print("This is the last iteration: " + str(count) + " The closest approximation so far is: " + str(curr_p))
if __name__ == '__main__':
    p_0 = float(input())
    newtonMethod(p_0)