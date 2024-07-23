#!/usr/bin/python3
""" 
User class
This module defines a User class with a private email attribute and 
provides getter and setter methods to access and modify the email attribute.
"""

class User:
    def __init__(self):
        """Initialize a new User instance with a private email attribute."""
        self.__email = None

    @property
    def email(self):
        """Getter for email.
        
        Returns:
            str: The email address of the user.
        """
        return self.__email

    @email.setter
    def email(self, value):
        """Setter for email.
        
        Args:
            value (str): The email address to set for the user.
            
        Raises:
            TypeError: If the provided value is not a string.
        """
        if not isinstance(value, str):
            raise TypeError("email must be a string")
        self.__email = value

if __name__ == "__main__":
    # Create an instance of the User class
    u = User()
    # Set the email attribute using the setter method
    u.email = "john@snow.com"
    # Print the email attribute using the getter method
    print(u.email)

