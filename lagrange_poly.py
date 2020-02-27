import numpy as np
from scipy.interpolate import lagrange
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
from math import cos, pi

x = np.array([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]) #actual nodes not the x-axis
y = 1/(x**2+1) #The function we're trying to mimic
poly = lagrange(x, y)
x_plot = []
p_plot = []
y_plot = []
cosPoly_Y = [] # output values from the Lagrange poly using the cosine for the nodes 
cosPoly_X = [] # the actual nodes themselves using the cosine
for x in np.arange(-5, 5, 0.1):
    x_plot.append(x)
    p_plot.append(poly(x))
    y_plot.append(1/((x)**2+1))

for x in range (0, 11):
	cosPoly_X.append(5*cos(((x)*pi)/10))
cos_poly = lagrange(cosPoly_X, y)
for x in np.arange(-5, 5, 0.1):
	cosPoly_Y.append(cos_poly(x))


plt.figure(0)
plt.subplot(2,1,1)
plt.plot(x_plot, p_plot, color="orange")
plt.title("Lagrange Interpolating Polynomial")
plt.xlabel("X Values from -5 to 5, nodes from 0 to 10")
plt.ylabel("Output Values from P(x)")


plt.subplot(2,1,2)
plt.plot(x_plot, y_plot)
plt.title("Original Polynomial")
plt.xlabel("X Values from -5 to 5, nodes from -5 to 5")
plt.ylabel("Output Values from f(x)")
plt.tight_layout()
plt.savefig("plots.png", dpi=500)
plt.show()

plt.figure(1)
plt.plot(x_plot, cosPoly_Y)
plt.title("Lagrange Interpolating Polynomial v2")
plt.xlabel("X Values from -5 to 5, nodes from 5 to -5")
plt.ylabel("Output Values from P(x)")
plt.savefig("plots_2.png", dpi=500)
plt.show()



''' 
Question 2, part 2: So, the two functions are quite similar and the error appears to be very small. It is most
likely so accurate because we're using 10 nodes, thus producing a 9th degree polynomial. From theorem 3.3, the error
gets smaller and smaller as more and more data points are added and from the data points. The Runge Function is actually
a special function that causes oscillation at the end points for the Lagrange Interpolating polynomials and this is evident
with the plots. Near the actual data points, it oscillates much less.

Question 2, part 3: Using this set of nodes, you can see that there is less issue with osciallation because the data points are
calculated much closer to the real value than the generation of the nodes from part 2. Thus, the error also tends to be smaller
and fits more of the bell curve shape that we're looking for.
'''


