"""Intro to Object Oriented Programming."""

from __future__ import annotations

__author__ = "730656260"


class Point: 
    """Representation of an x,y coordinate graph."""

    x: float
    y: float

    def __init__(self, x_init: float = 0.0, y_init: float = 0.0):
        """Initializes a point."""
        self.x = x_init
        self.y = y_init

    def scale_by(self, factor: int) -> None:
        """Scales the point coordinates by a specific factor."""
        self.x *= factor
        self.y *= factor
    
    def scale(self, factor: int) -> Point:
        """Make a new point with existing points properties multipled by the factor."""
        new_point: Point = Point(self.x * factor, self.y * factor)
        return new_point
    
    def __str__(self) -> str:
        """Returns the string representation of a point."""
        return f"x: {self.x}; y: {self.y}"
    
    def __mul__(self, factor: int | float) -> Point:
        """Multiplies the previous points by a set factor."""
        return Point(self.x * factor, self.y * factor)
    
    def __add__(self, add: int | float) -> Point:
        """Adds the x and y attributes to a new point."""
        return Point(self.x + add, self.y + add)
    