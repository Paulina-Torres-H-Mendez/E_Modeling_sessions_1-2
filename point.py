import random





class Point:
    def __init__(self, x, y):
        """
        Creates a point at (x, y).

        Args:
            x (int or float): X-coordinate.
            y (int or float): Y-coordinate.

        """
        self.x = x
        self.y = y

    def __str__(self):
        """
        Returns a string like <x, y>.

        """
        return f"<{self.x}, {self.y}>"


    def __repr__(self):
        """
        Returns the same as __str__ for easy viewing.

        """
        return self.__str__()


    def distance_orig(self):
        """
        Calculates distance from the origin (0, 0).

        Returns the distance from origin.
        """
        return (self.x**2 + self.y**2)**0.5


    def __gt__(self, other):
        """
        Checks if this point is farther from origin than another.
        Args:
            other (Point): Another point to compare.

        Returns True if farther, False otherwise.
        """
        return self.distance_orig() > other.distance_orig()


    def __eq__(self, other):
        """
        Checks if this point is the same distance from origin as another.
        Args:
            other (Point): Another point to compare.
        Returns True if equal, False otherwise.
        """
        return self.distance_orig() == other.distance_orig()


if __name__ == "__main__":
    #Creates a point at (1, 2)
    p = Point(1, 2)
    print(f"p.x={p.x}, p.y={p.y}")

    #Change x to 20
    p.x = 20
    print(f"p.x={p.x}, p.y={p.y}")
    print(p)

    #Generate 5 random points
    points = [Point(random.randint(-10, 10), random.randint(-10, 10)) for _ in range(5)]
    print("Random points:", points)

    # Distance check
    p = Point(3, 4)
    print("Distance from origin:", p.distance_orig())

    # Compare points
    p2 = Point(1, 1)
    print("Is p > p2?", p > p2)

    # Sort and print points
    points.sort()
    print("Sorted points:", points)


if __name__ == "__main__":
    # Instance
    p = Point(1, 2) #  p = instance of 1 n 2
    print(f"p.x={p.x} and p.y={p.y}")
    p.x = 20
    print(f"p.x={p.x} and p.y={p.y}")
    print(p)
    # list of 5 random points
    points = []
    for i in range(5):
        points.append(Point(random.randint(-10, 10), #x
                            random.randint(-10, 10))) #y



    print("I got these 5 random points:")
    print(points)
    p = Point(3, 4)
    print(p.distance_orig()) # expecting 5
    p2 = Point(1, 1)
    print(f"I am comparing p > p2: {p>p2}") # I expect to have True
    print("the sorted list of points is:")
    points.sort()
    print(points)