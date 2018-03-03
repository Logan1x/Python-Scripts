# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation


def f(order, coefficients, x):
    s = sum([coefficients[i]*(x**(order-i)) for i in range(order+1)])
    return s


class Integrate(object):
    def __init__(self):
        self.N = None
        self.I = None

    def graph(self, order, coefficients, low, high, interval, ans):
        fig = plt.figure()
        plt.axes(xlim=(low-5, high+5))
        lines = [plt.plot([], [], color='r')[0] for i in range(30)]
        plt.title('Trapezoid Method\nRequired area is %0.2f units' % (ans))
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.axhline(y=0, color='k')
        plt.axvline(x=0, color='k')
        x = np.linspace(low, high, 500)
        y = f(order, coefficients, x)
        s = ''
        for i in range(order+1):
            if coefficients[i] >= 0:
                s = s+(' +'+str(coefficients[i])+'x^'+str(order-i))
            else:
                s = s+(' '+str(coefficients[i])+'x^'+str(order-i))
        s = s+' = 0'
        plt.plot(x, y, 'darkslateblue', label=s)

        def init():
            for line in lines:
                line.set_data([], [])
            return lines

        def animate(i):
            if i < 2:
                for j in range(30):
                    lines[j].set_data([], [])
            else:
                x = np.linspace(low, high, i)
                y = f(order, coefficients, x)
                lines[29].set_data(x, y)
                for j in range(i):
                    lines[j].set_data([x[j], x[j]], [y[j], 0])
                for j in range(i, 29):
                    lines[j].set_data([], [])
            return lines

        animation.FuncAnimation(
            fig, animate, init_func=init, frames=30, interval=500, blit=True)
        plt.legend(loc='upper right', numpoints=1)
        plt.show()

    def Trapezoid(self, order, coefficients, low, high, interval):
        self.N = (high - low)/interval
        self.I = sum([2*f(order, coefficients, low + (i*interval))
                      for i in range(1, int(self.N))])
        self.I += (f(order, coefficients, low) + f(order, coefficients, high))
        ans = (self.I*(high - low))/(2*self.N)
        self.graph(order, coefficients, low, high, interval, ans)
        return ans

    def Simpson(self, order, coefficients, low, high, interval):
        self.N = (high - low)/(2*interval)
        self.I = sum([4*f(order, coefficients, low + (i*interval)) if i % 2 == 1 else 2 *
                      f(order, coefficients, low + (i*interval)) for i in range(1, int(2*self.N))])
        self.I += (f(order, coefficients, low) + f(order, coefficients, high))
        return (self.I*(high - low))/(6*self.N)

    def solve(self, order, coefficients, low, high, method, interval=1e-3):
        if method == 'trapezoid':
            return self.Trapezoid(order, coefficients, low, high, interval)
        elif method == 'simpson':
            return self.Simpson(order, coefficients, low, high, interval)


igr = Integrate()
for method in ['trapezoid']:
    solution = igr.solve(3, [7, 3, -6, 10], -50, 65, method=method)
    print(solution)
