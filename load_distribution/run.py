import numpy as np
from parabolic import ParabolicLoadDistribution

# defining the parabolic load distribution function
Fz = 3600       # Total vertical load in Newtons
a_minus = -0.0700       # Half-length of the tire contact patch in meters
a_plus = 0.0700         # Half-length of the tire contact patch in meters

w_minus = -0.101       # Half-width of the tire contact patch in meters
w_plus = 0.101         # Half-width of the tire contact patch in meters

x_values = np.linspace(a_minus, a_plus, 71)  # x-coordinates within the contact patch
y_values = np.linspace(w_minus, w_plus, 102)  # y-coordinates within the contact patch
x_matrix = np.tile(x_values, (len(y_values), 1))  # Create a grid of x-coordinates
y_matrix = np.tile(y_values[:, np.newaxis], (1, len(x_values)))

qz_distribution = ParabolicLoadDistribution(Fz, x_matrix, y_matrix)
qz = qz_distribution.load_distribution()
qz_distribution.plot_load_distribution()
