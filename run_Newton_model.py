from Engien import Engine
from Space.SpaceObjects.planets import NewtonPlanet
from Space.SpaceObjects.star import Sun
from Space.space import NewtonSpace
from arguments import create_arg_parser

bg_color = (0, 0, 0)


# create space objects
def create_space_objects(screen_size):
    mercury = NewtonPlanet(name="Mercury",
                           radius=3,
                           mass=15,
                           color=(128, 128, 128),
                           start_coord=(screen_size[0] // 2 + 50,
                                        screen_size[1] // 2 - 50),
                           velocity=(25, 25))

    venus = NewtonPlanet(name="Venus",
                         radius=9,
                         mass=240,
                         color=(50, 128, 255),
                         start_coord=(screen_size[0] // 2 + 100,
                                    screen_size[1] // 2 - 100),
                         velocity=(30, 30))

    earth = NewtonPlanet(name="Earth",
                         radius=10,
                         mass=300,
                         color=(0, 28, 200),
                         start_coord=(screen_size[0] // 2 + 150,
                                      screen_size[1] // 2 - 150),
                         velocity=(35, 35))

    mars = NewtonPlanet(name="Mars",
                        radius=5,
                        mass=150,
                        color=(250, 0, 0),
                        start_coord=(screen_size[0] // 2 + 200,
                                     screen_size[1] // 2 - 200),
                        velocity=(40, 40))

    jupiter = NewtonPlanet(name="Jupiter",
                           radius=16,
                           mass=600,
                           color=(255, 200, 100),
                           start_coord=(screen_size[0] // 2 + 300,
                                        screen_size[1] // 2 - 300),
                           velocity=(50, 50))

    planets = [mercury, venus, earth, mars, jupiter]

    sun = Sun(name='Sun',
              radius=30,
              mass=9e+5,
              color=(255, 255, 0),
              start_coord=(screen_size[0] / 2, screen_size[1] / 2))

    space_objects = planets + [sun]
    return space_objects


if __name__ == '__main__':
    screen_size = (800, 800)
    # create args parser
    parser = create_arg_parser()
    # get args from command line
    args = parser.parse_args()

    space_objects = create_space_objects(screen_size)
    space = NewtonSpace(space_objects)

    create_space_objects(screen_size)
    engine = Engine(screen_size, bg_color, time_delta=args.time_delta)
    engine.set_simulation_parameters(trace=args.trace,
                                     trace_length=args.trace_length,
                                     show_gravitational_radius=args.show_gravitational_radius,
                                     num_sun_rays=args.num_sun_rays)
    space.set_screen(engine.screen)
    engine.run(space)
