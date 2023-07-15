from Space.SpaceObjects.space_object import SpaceObject
import pygame
import math


class CopernicusPlanet(SpaceObject):
    def __init__(self, name, radius, mass, color,
                 semimajor_axis, eccentricity, angle=0):
        """
       Constructor for the CopernicusPlanet class.

       Args:
           name (str): The name of the planet.
           radius (float): The radius of the planet.
           mass (float): The mass of the planet.
           color (tuple[int, int, int]): The color of the planet.
           semimajor_axis (float): The semimajor axis of the planet's elliptical orbit.
           eccentricity (float): The eccentricity of the planet's elliptical orbit.
           angle (float, optional): The initial angle of the planet in its orbit. Defaults to 0.
       """
        super().__init__(name, radius, mass, color)
        self.semimajor_axis = semimajor_axis
        self.eccentricity = eccentricity
        self.angle = angle
        self.angle_speed = math.sqrt(mass / semimajor_axis ** 3)
        self.x, self.y = (0, 0)

    def update(self, time_delta):
        self.angle += self.angle_speed * time_delta

        self.x = self.semimajor_axis * math.cos(self.angle) * (1 - self.eccentricity ** 2) / (
                    1 + self.eccentricity * math.cos(self.angle))
        self.y = self.semimajor_axis * math.sin(self.angle) * (
                    1 - self.eccentricity ** 2) / (1 + self.eccentricity * math.cos(self.angle))

    def draw(self, screen):
        self.x += screen.get_width() // 2
        self.y += screen.get_height() // 2
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)


class NewtonPlanet(SpaceObject):
    def __init__(self, name, radius, mass, color, start_coord, velocity):
        """
        Constructor for the NewtonPlanet class.

        Args:
            name (str): The name of the planet.
            radius (float): The radius of the planet.
            mass (float): The mass of the planet.
            color (tuple[int, int, int]): The color of the planet.
            start_coord (tuple[int, int]): The starting coordinates of the planet.
            velocity (tuple[float, float]): The initial velocity of the planet.
        """
        super().__init__(name, radius, mass, color)
        self.x, self.y = start_coord
        self.velocity = list(velocity)

    def update(self, time_delta):
        self.x += self.velocity[0] * time_delta
        self.y += self.velocity[1] * time_delta

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)