import random
import functools
import operator
import matplotlib.pyplot as plt

MAX_X = 25
MIN_X = 0
MAX_Y = 25
MIN_Y = 0

def stop_gen(number):
	global MAX_X, MAX_Y
	stops = []
	for x in range(number):
		stop = (float(random.randint(MIN_X,MAX_X)),float(random.randint(MIN_X,MAX_X)))
		stops.append(stop)
	return stops

class traveler(object):
	def __init__(self, stops):
		self.stops = list(stops)
		self.cur_loc = stops[random.randint(0,len(self.stops)-1)]
		self.origin = self.cur_loc
		self.stops.pop(stops.index(self.cur_loc))
		self.path = []

	@staticmethod
	def find_distance(stop_a, stop_b):
		x_range = functools.reduce(operator.__sub__, sorted([coord[0] for coord in [stop_a, stop_b]]))
		y_range = functools.reduce(operator.__sub__, sorted([coord[1] for coord in [stop_a, stop_b]]))
		distance = ((x_range**2) + (x_range**2))**(0.5)
		return distance

	def find_closest(self):
		least = None
		closest = None
		for stop in self.stops:
			dist = self.find_distance(self.cur_loc, stop)
			if closest and dist > least:
				continue
			else:
				closest = stop
				least = dist

		return closest

	def find_path(self):
		print(self.cur_loc)
		self.path.append(self.cur_loc)
		while True:
			next = self.find_closest()
			self.stops.pop(self.stops.index(next))
			print(next)
			self.path.append(next)

			if not self.stops:
				break
		self.path.append(self.origin)


def display(stops):
	xs = [coord[0] for coord in stops]
	ys = [coord[1] for coord in stops]
	plt.plot(xs, ys)
	for x in xs:
		i = xs.index(x)
		plt.text(x, ys[i], str(i))
	plt.savefig("test.png")
	

if __name__ == "__main__":
	stops = stop_gen(5)
	t = traveler(stops)
	print(stops)
	t.find_path()
	display(t.path)