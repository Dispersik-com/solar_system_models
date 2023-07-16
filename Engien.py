import pygame


class Engine:
    def __init__(self, screen_size, bg_color, time_delta=0.1):
        pygame.init()
        self.screen_size = screen_size
        self.screen = pygame.display.set_mode(screen_size)
        pygame.display.set_caption("Solar system")
        self.bg_color = bg_color
        self.light_on = False
        self.time_delta = time_delta
        self.shift_mouse_x, self.shift_mouse_y = (0, 0)

    def set_simulation_parameters(self, trace=False, trace_length=100, show_gravitational_radius=False, num_sun_rays=100):
        self.trace = trace
        self.trace_length = trace_length
        self.show_gravitational_radius = show_gravitational_radius
        self.num_sun_rays = num_sun_rays

    def run(self, space):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        pygame.quit()
                        quit()

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    sun = space.get_object_by_name('Sun')

                    if sun.x - sun.radius < pygame.mouse.get_pos()[0] < sun.x + sun.radius:
                        if sun.y - sun.radius < pygame.mouse.get_pos()[1] < sun.y + sun.radius:
                            if self.light_on:
                                self.light_on = False
                            else:
                                self.light_on = True


            self.screen.fill(self.bg_color)

            space.update(self.time_delta)
            space.draw(trace=self.trace, trace_length=self.trace_length,
                       gravitational_radius=self.show_gravitational_radius)

            sun = space.get_object_by_name('Sun')
            if self.light_on:
                sun.sun_light(self.screen, space.get_space_objects(), self.num_sun_rays)

            pygame.time.Clock().tick(60)
            pygame.display.update()
