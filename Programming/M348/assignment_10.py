import math

def f(t, y):
	return math.exp(t - y)

def y(t):
	return math.log(math.exp(t) + math.exp(1) - 1)

################################ PROBLEM 4 #######################################

def problem4 (a, b, h, initial):

	t = a
	w = initial
	print("t = {}\nw = {}".format(t, w))

	while (t <= b):
		K1 = h * f(t, w)
		K2 = h * f(t + h/2, w + K1/2)
		K3 = h * f(t + h/2, w + K2/2)
		K4 = h * f(t + h, w + K3)

		w += (K1 + 2*K2 + 2*K3 + K4)/6
		t += h
		print("t = {}\nw = {}\n".format(t, w))

	return w

################################ PROBLEM 5 ########################################

def problem5 (a, b, initial, TOL, hmax, hmin):

	t = a
	w = initial
	h = hmax
	FLAG = 1
	print("t = {}\nw = {}".format(t, w))

	while (FLAG == 1):

		K1 = h * f(t, w)
		K2 = h * f(t + 0.25*h, w + 0.25*K1)
		K3 = h * f(t + (3/8)*h, w + (3/32)*K1 + (9/32)*K2)
		K4 = h * f(t + (12/13)*h, w + (1932/2197)*K1 - (7200/2197)*K2 + (7296/2197)*K3)
		K5 = h * f(t + h, w + (439/216)*K1 - 8*K2 + (3680/513)*K3 - (845/4104)*K4)
		K6 = h * f(t + .5*h, w - (8/27)*K1 + 2*K2 - (3544/2565)*K3 + (1859/4104)*K4 - (11/40)*K5)

		R = (h**-1)*abs((1/360)*K1 - (128/4275)*K3 - (2197/75240)*K4 + (1/50)*K5 + (2/55)*K6)
		
		if (R <= TOL):
			t += h
			w += ((25/216)*K1 + (1408/2565)*K3 + (2197/4104)*K4 - .2*K5)
			print("t = {}\nw = {}\nh = {}\n".format(t, w, h))

		delta = 0.84*(TOL/R)**.25
		
		if (delta <= .1):
			h = .1*h
		else:
			if (delta >= 4):
				h = 4*h
			else:
				h = delta*h

		if (h > hmax):
			h = hmax

		if (t >= b):
			FLAG = 0
		else:
			if (t + h > b):
				h = b - t
			else:
				if (h < hmin):
					FLAG = 0
					return "Minimum h exceeded."

	return w

###################################################################################


def main():
	Q = int(input("Which question? (4 or 5):" ))

	if Q == 4:

		a = 0
		b = 1
		h = 0.01
		w0 = 1

		approx = problem4(a, b, h, w0)
		actual = y(b)
		error = abs(approx - actual)

		print ("Approximated answer: {}".format(approx))
		print ("Actual answer: {}".format(actual))
		print ("Error: {}\n".format(error))

	elif Q == 5:

		a = 0
		b = 1
		w0 = 1
		TOL = 10**-4
		hmax = .025
		hmin = .005

		approx = problem5(a, b, w0, TOL, hmax, hmin)
		actual = y(b)
		error = abs(approx - actual)

		print ("Approximated answer: {}".format(approx))
		print ("Actual answer: {}".format(actual))
		print ("Error: {}".format(error))

main()