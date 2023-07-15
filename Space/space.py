from abc import ABC, abstractmethod
import math
import pygame
from Space import SpaceObjects

G = 6.67430e-2 #Gravitational constant

class Space(ABC):
    def __init__(self, space_objects: list[SpaceObjects]):
        """
        Constructor for the Space class.

        Args:
            space_objects (list[SpaceObjects]): List of space objects.
        """
        self.space_objects = {sp_obj.name: sp_obj for sp_obj in space_objects}
        self.dict_trace = dict()

    def set_screen(self, screen):
        """
        Set the screen for drawing the space objects.

        Args:
            screen: The screen for drawing.
        """
        self.screen = screen

    def add_space_object(self, space_object):
        """
        Add a space object to the space.

        Args:
            space_object: The object to add to the space.
        """
        if self.get_object_by_name(space_object.name):
            raise "This object is already exists in space"
        self.space_objects[space_object.name] = space_object

    def get_space_objects(self) -> list:
        """
        Get all the space objects.

        Returns:
            All space objects.
        """
        return self.space_objects.values()

    def get_object_by_name(self, name):
        """
        Get an object by its name.

        Args:
            name (str): The name of the object.

        Returns:
            The object with the specified name or None if the object is not found.
        """
        return self.space_objects.get(name)

    @abstractmethod
    def update(self, time_delta):
        pass

    def draw(self, trace=False, trace_length=100, gravitational_radius=False):
        """
        Draw the space objects on the screen.

        Args:
            trace (bool, optional): Enable drawing object traces. Default is False.
            trace_length (int, optional): Number of trace points. Default is 100.
            gravitational_radius (bool, optional): Enable drawing gravitational radii of objects.
                                                   Default is False.
        """
        for space_object in self.get_space_objects():
            space_object.draw(self.screen)
            if trace:
                self.trace(space_object, trace_length)
            if gravitational_radius:
                self.draw_gravitational_radius(space_object)

    def draw_gravitational_radius(self, space_object):
        """
        Draw the gravitational radius of an object on the screen.

        Args:
            space_object: The object for which to draw the gravitational radius.
        """
        radius = space_object.gravitational_radius
        pygame.draw.circle(self.screen, (0, 255, 0), (space_object.x, space_object.y), int(radius), 1)

    def trace(self, space_object, trace_length):
        """
        Draw the trace of an object on the screen.

        Args:
            space_object: The object for which to draw the trace.
            trace_length: The length of the trace (number of points).
        """
        if self.dict_trace.get(space_object.name, None) is None:
            self.dict_trace[space_object.name] = {'color': space_object.color, 'points': []}

        if space_object.x and space_object.y:
            self.dict_trace[space_object.name]['points'].append((space_object.x, space_object.y))
            if len(self.dict_trace[space_object.name]['points']) > trace_length:
                self.dict_trace[space_object.name]['points'].pop(0)

        for trace in self.dict_trace.values():
            if len(trace['points']) >= 2:
                pygame.draw.lines(self.screen, trace['color'], False, trace['points'])



class CopernicusSpace(Space):

    def update(self, time_delta):
        for space_object in self.get_space_objects():
            space_object.update(time_delta)


class NewtonSpace(Space):

    def update(self, time_delta):
        # Get all the space objects
        space_objects = self.get_space_objects()
        for space_object in space_objects:
            for other_space_object in space_objects:
                if space_object != other_space_object:
                    # Calculate the distance between objects
                    distance = math.sqrt(
                        (space_object.x - other_space_object.x) ** 2 + (space_object.y - other_space_object.y) ** 2)
                    if distance <= space_object.gravitational_radius or distance <= other_space_object.gravitational_radius:
                        # Calculate the gravitational force
                        force = (G * space_object.mass * other_space_object.mass) / distance ** 2
                        # Calculate the acceleration relative to the mass
                        # The coefficient of 10 is needed for a smooth transition of the planets' acceleration.
                        acceleration = force / space_object.mass + 10
                        # Calculate the difference in distances along the axes
                        delta_x = other_space_object.x - space_object.x
                        delta_y = other_space_object.y - space_object.y
                        # Calculate the angle of the gravitational force
                        angle = math.atan2(delta_y, delta_x)
                        if space_object.name == 'Sun':
                            # Skip the Sun object as it does not experience gravitational acceleration in this model
                            continue
                        # Apply the acceleration to the velocity
                        space_object.velocity[0] += acceleration * math.cos(angle) * time_delta
                        space_object.velocity[1] += acceleration * math.sin(angle) * time_delta
            # Update the position of the space object
            space_object.update(time_delta)