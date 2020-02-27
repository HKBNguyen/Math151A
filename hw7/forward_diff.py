from math import exp

def forward_diff(x_0: int):
	delta = [10**-2,10**-4, 10**-6, 10**-8, 10**-10, 10**-12]
	for h in delta:
		curr_approx = (exp(x_0 + h) - exp(x_0))/h
		abs_error = abs(curr_approx - exp(0))
		print(h, curr_approx, abs_error)



if __name__ == '__main__':
	forward_diff(0)

'''
The error gets smaller and smaller as h grows bigger until 10e-8 and then the error starts to get larger.
This is most likely due to division by very small numbers and thus truncation occurs/inaccuracy of
machine numbers.
'''