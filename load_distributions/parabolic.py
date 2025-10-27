import numpy as np 
import matplotlib.pyplot as plt

class ParabolicLoadDistribution:
    def __init__(self, Fz, x_matrix, y_matrix):
        self.Fz = Fz
        self.x_matrix = x_matrix
        self.y_matrix = y_matrix

    def load_distribution(self):
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

        x_max = np.max(self.x_matrix)
        y_max = np.max(self.y_matrix)

        qzx = ((3 * self.Fz) / (4 * x_max)) * (1 - (self.x_matrix / x_max) ** 2)
        qzy = 1 / (2 * y_max)

        qz = np.dot(qzx, qzy)

        # introduce here an integral to ensure that total Fz is maintained
        total_load = np.trapz(np.trapz(qz, self.x_matrix[1,:], axis=1), self.y_matrix[:,1])
        if np.isclose(total_load, self.Fz, rtol=0.01):
            print("Total load matches the specified Fz.")
        else:
            print("Total load does not match the specified Fz.\n")
            print(f"Total Load from Distribution: {total_load} N")

        return qz

    def plot_load_distribution(self):
        """Plot the load distribution over the tire contact patch."""
        qz = self.load_distribution()
        fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
        ax.plot_surface(self.x_matrix, self.y_matrix, qz, cmap='viridis')
        ax.set_xlabel('X (m)')
        ax.set_ylabel('Y (m)')
        ax.set_zlabel('Load Distribution qz (N/m²)')
        ax.set_title('Parabolic Load Distribution over Tire Contact Patch')
        plt.show()


