class Molecular:
    """
    A class used to represent a molecule in a simulation.
    """
    all_mol = []

    def __init__(self, x, y, vx, vy, color, radius):
        """
        Initialize the Molecular instance.

        Parameters:
        x (float): The x-coordinate of the molecule.
        y (float): The y-coordinate of the molecule.
        vx (float): The velocity of the molecule along the x-axis.
        vy (float): The velocity of the molecule along the y-axis.
        color (str): The color of the molecule.
        radius (float): The radius of the molecule.
        """
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.radius = radius

    def going(self):
        """
        Update the molecule's position based on its velocity.

        Reflects the molecule off the walls of the container if it reaches the edge.
        Adjusts the position if the molecule overlaps the wall due to its radius.
        """
        if not self.radius <= self.x + self.vx <= 700 - self.radius:
            self.vx = -self.vx
        if not self.radius <= self.y + self.vy <= 700 - self.radius:
            self.vy = -self.vy
        self.x += self.vx
        self.y += self.vy

        if self.x < self.radius:
            self.x = self.radius
        elif self.x > 700 - self.radius:
            self.x = 700 - self.radius

        if self.y < self.radius:
            self.y = self.radius
        elif self.y > 700 - self.radius:
            self.y = 700 - self.radius

    def __str__(self):
        """
        Return a string representation of the molecule's current state.
        """
        return f'{self.x}; {self.y}; {self.vx}; {self.vy}'

    def __repr__(self):
        """
        Return an unambiguous string representation of the molecule.
        """
        return Molecular.__str__(self)
