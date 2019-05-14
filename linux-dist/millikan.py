#!/usr/bin/env python3
import csv
import numpy as np
import math

""" Millikan's Oil Droplet Experiement """

try:
	data = np.genfromtxt("results.csv", delimiter = ',')
	time = data[:,0]
	voltage = data[:,1]
	distance = data[:,2]

	xfit, yfit = None, None

except OSError as e:
	print(e)


time_list = []
voltage_list = []
dist_list = []

array_x_plot = []
array_y_plot = []


class Millikan():
	def __init__(self):
		super(Millikan, self).__init__()


	def formulas():
		# Constants
		charge_of_electron = 1.6021765e-19
		a = 7.776e-8
		pi = math.pi
		gravity = 9.81
		dens_of_oil = 877
		dens_of_air = 1.16
		rho = 2*((dens_of_oil - dens_of_air)*gravity)
		plate_dist = 0.006

		for i in range(0, len(data[:,0])):
			t, volt, dist = time[i], voltage[i], distance[i]
			velocity = dist/t

			visc_of_air = 1.789*10**-5
			r = ((9*visc_of_air*velocity)/rho)**0.5
			q_sqrt = (visc_of_air**3*velocity**3/rho)**0.5
			q = 18*pi*plate_dist/volt*q_sqrt
			array_x_plot.append(r)
			array_y_plot.append(q)


	def graph(self, plot_x, plot_y):
		xmin = plot_x[0]
		xmax = plot_x[len(plot_x)-1]
		interval = (xmax-xmin)/99
		coefs = (np.polyfit(plot_x, plot_y, 2))

		xfit = np.arange(xmin, xmax + interval, interval)
		yfit = np.polyval(coefs, xfit)

		return xfit, yfit


	def sort(self):
		ord1 = np.array(array_x_plot)
		ord2 = np.array(array_y_plot)

		orig_array = np.column_stack([ord1, ord2])
		sorted_array = orig_array[orig_array[:,0].argsort()]

		x = sorted_array[:,0]
		y = sorted_array[:,1]

		return x, y


	formulas()


# Run module if called directly
if __name__ == "__main__":
	import matplotlib.pyplot as plt

	app = Millikan()
	x, y = app.sort()
	xfit, yfit = app.graph(x, y)

	# Create graph with LoBF - quadratic graph
	plt.plot(x, y, 'ro', xfit, yfit)
	plt.show()
