#!/usr/bin/python3

class Square:
    """
    A class representing a square shape.
    
    Attributes:
    - width: The width of the square.
    - height: The height of the square.
    """

    def __init__(self, width=0, height=0):
        """
        Initializes a square with the given width and height.
        
        Args:
        - width (int): The width of the square. Defaults to 0.
        - height (int): The height of the square. Defaults to 0.
        """
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """
        Calculates the area of the square.
        
        Returns:
        - int: The area of the square, calculated as width * height.
        """
        return self.width * self.height

    def perimeter_of_my_square(self):
        """
        Calculates the perimeter of the square.
        
        Returns:
        - int: The perimeter of the square, calculated as 2 * (width + height).
        """
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """
        Returns a string representation of the square.
        
        Returns:
        - str: A string representation of the square in the format 'width/height'.
        """
        return "{}/{}".format(self.width, self.height)

if __name__ == "__main__":
    # Create an instance of the Square class with width 12 and height 9
    s = Square(width=12, height=9)
    # Print the string representation of the square
    print(s)
    # Print the area of the square
    print(s.area_of_my_square())
    # Print the perimeter of the square
    print(s.perimeter_of_my_square())

