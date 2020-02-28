from math import exp

def forward_diff(x_0: int):
	delta = [10**-2,10**-4, 10**-6, 10**-8, 10**-10, 10**-12]
	print("h", "    Forward-diff approximation", "Absolute Error")
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

h       Forward-diff approx.       Absolute Error
========================================================
0.01    1.005016708416795          0.005016708416794913
0.0001  1.000050001667141          5.0001667140975314e-05
1e-06   1.0000004999621837         4.999621836532242e-07
1e-08   0.999999993922529          6.07747097092215e-09
1e-10   1.000000082740371          8.274037099909037e-08
1e-12   1.000088900582341          8.890058234101161e-05
'''