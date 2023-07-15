from .space_object import SpaceObject
import math
import pygame


class Sun(SpaceObject):

    def draw(self, screen: pygame.display):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)

    def update(self, time_delta):
        pass

    def sun_light(self, screen: pygame.display, space_objects: list, num_rays: int):
        """
        Draws rays of light from the sun to intersecting planets.

        :param screen: pygame.display
        :param space_objects: list that contains all planets
        :param num_rays: number of rays.
        """
        ray_length = 2000
        planets_light_stop_pos = []
        planets_light_stop_num = []

        for i in range(num_rays):
            angle = i * (2 * math.pi / num_rays)
            sun_pos = (
                self.x + self.radius * math.cos(angle),
                self.y + self.radius * math.sin(angle)
            )
            end_pos = (
                sun_pos[0] + ray_length * math.cos(angle),
                sun_pos[1] + ray_length * math.sin(angle)
            )
            min_radius = float('inf')
            intersected_planet_pos = None
            for planet in space_objects:
                planet_pos = intersect_line_circle(sun_pos, end_pos, (planet.x, planet.y), planet.radius)
                if planet_pos:
                    if planet.radius <= min_radius:
                        min_radius = planet.radius
                        intersected_planet_pos = planet_pos
            if intersected_planet_pos:
                for index, items in enumerate(planets_light_stop_num):
                    if i == items:
                        intersected_planet_pos = planets_light_stop_pos[index]
                        pygame.draw.line(screen, (255, 255, 0), sun_pos, intersected_planet_pos)
                        break
                else:
                    planets_light_stop_pos.append(intersected_planet_pos)
                    planets_light_stop_num.append(i)
                    pygame.draw.line(screen, (255, 255, 0), sun_pos, intersected_planet_pos)
            else:
                pygame.draw.line(screen, (255, 255, 0), sun_pos, end_pos)


def intersect_line_circle(start: float | int, end: float | int, center: tuple, radius: float | int):
    """
    Checks if a line intersects a circle and returns the intersection point if true.

    :param start: starting point of the line
    :param end: ending point of the line
    :param center: center of the circle
    :param radius: radius of the circle
    :return: intersection point if line intersects the circle, False otherwise
    """
    # Step 1: Find vector connecting start and center
    v = (center[0] - start[0], center[1] - start[1])

    # Step 2: Find projection of vector v onto line direction
    u = (end[0] - start[0], end[1] - start[1])
    vu = v[0] * u[0] + v[1] * u[1]
    uu = u[0] * u[0] + u[1] * u[1]
    t = vu / uu

    # Step 3: Check if intersection is within the line segment
    if t < 0 or t > 1:
        return False

    # Step 4: Find closest point on line to center of circle
    p = (start[0] + t * u[0], start[1] + t * u[1])
    d = math.sqrt((center[0] - p[0]) ** 2 + (center[1] - p[1]) ** 2)

    # Step 5: Check if intersection is within the circle
    if d <= radius:
        return p
    else:
        return False
