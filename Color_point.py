from point import Point
import random





class PointException(Exception):
    """
    Exception for invalid points (like if x or y isn't a number).
    """
    pass


class ColorPoint(Point):
    def __init__(self, x, y, color):
        """
        Colored point at (x, y). Checks if x and y are numbers.
        """
        if not isinstance(x, (int, float)):
            raise PointException("x must be a number")
        if not isinstance(y, (int, float)):
            raise PointException("y must be a number")

        super().__init__(x, y)
        self.color = color


    def __str__(self):
        """
        Shows color and coords (like color: x, y)
        """
        return f"<{self.color}: {self.x}, {self.y}>"



if __name__ == "__main__":
    # Test for basic point
    p = ColorPoint(1, 2, "red")
    print(p.distance_orig())
    print(p)


    #Random color points
    colors = ["red", "green", "blue", "yellow", "black", "magenta", "cyan", "white", "gold"]
    color_points = []
    for i in range(10):
        color_points.append(ColorPoint(random.randint(-10, 10), random.randint(-10, 10), random.choice(colors)))


    print(color_points)

    color_points.sort()

    print(color_points)