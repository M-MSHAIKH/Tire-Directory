import numpy as np 
import matplotlib.pyplot as plt

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

def ParabolicLoadDistribution(x_matrix, y_matrix, Fz):
    """Calculate the parabolic load distribution at a given point (x, y).

    The load distribution is defined as:
        qz(x, y) = qzx(x) * qzy(y)
    where:
        qzx(x) = (3 * Fz / (4 * a)) * (1 - (x / a)^2)
        qzy(y) = 1 / (2 * b)

    Args:
        x_matrix (array): x-coordinate (or length) within the contact patch in a matrix form in meters.
        y_matrix (array): y-coordinate (or width) within the contact patch in a matrix form in meters.
        Fz (int): Total vertical load in Newtons.

    Returns:
        array: Load distribution value at each coordinate points within the contact patch.
    """

    x_min = np.min(x_matrix)
    x_max = np.max(x_matrix)
    y_min = np.min(y_matrix)
    y_max = np.max(y_matrix)

    qzx = ((3 * Fz) / (4 * x_max)) * (1 - (x_matrix / x_max) ** 2)
    qzy = 1 / (2 * y_max)

    qz = np.dot(qzx, qzy)

    # introduce here an integral to ensure that total Fz is maintained
    total_load = np.trapz(np.trapz(qz, x_values, axis=1), y_values)
    if np.isclose(total_load, Fz, rtol=0.01):
        print("Total load matches the specified Fz.")
    else:
        print("Total load does not match the specified Fz.")
        print(f"Total Load from Distribution: {total_load} N")

    return qz

def plot_load_distribution(x, y, qz):
    """Plot the load distribution over the tire contact patch."""

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    ax.plot_surface(x, y, qz, cmap='viridis')
    ax.set_xlabel('X (m)')
    ax.set_ylabel('Y (m)')
    ax.set_zlabel('Load Distribution qz (N/m²)')
    ax.set_title('Parabolic Load Distribution over Tire Contact Patch')
    plt.show()


qz_distribution = ParabolicLoadDistribution(x_matrix, y_matrix, Fz)
plot_load_distribution(x_matrix, y_matrix, qz_distribution)