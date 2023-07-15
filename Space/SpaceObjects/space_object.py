from abc import ABC, abstractmethod
from Space.space import G


class SpaceObject(ABC):
    """
    This is a basic abstract class for all objects in space.
    """
    def __init__(self, name: str, radius: float, mass: float,
                 color: tuple[int, int, int], start_coord: tuple[int, int] = (0, 0)):
        """
        Constructor for the SpaceObject class.

        Args:
            name (str): The name of the space object.
            radius (float): The radius of the space object.
            mass (float): The mass of the space object.
            color (tuple[int, int, int]): The color of the space object.
            start_coord (tuple[int, int]): The starting coordinates of the space object. Defaults to (0, 0).
        """
        self.name = name
        self.radius = radius
        self.color = color
        self.mass = mass
        self.x, self.y = start_coord
        self.gravitational_radius = G * mass

    @abstractmethod
    def update(self, time_delta):
        pass

    @abstractmethod
    def draw(self, screen):
        pass
