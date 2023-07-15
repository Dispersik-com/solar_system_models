from Engien import Engine
from Space.SpaceObjects.planets import CopernicusPlanet
from Space.SpaceObjects.star import Sun
from Space.space import CopernicusSpace
from arguments import create_arg_parser


bg_color = (0, 0, 0)

# create space objects
def create_space_objects(screen_size):
    mercury = CopernicusPlanet(name="Mercury",
                               radius=2,
                               mass=10e+3,
                               color=(128, 128, 128),
                               semimajor_axis=50,
                               eccentricity=0.01)

    venus = CopernicusPlanet(name="Venus",
                             radius=6,
                             mass=18e+3,
                             color=(50, 128, 255),
                             semimajor_axis=80,
                             eccentricity=0.01)

    earth = CopernicusPlanet(name="Earth",
                             radius=6.4,
                             mass=20e+3,
                             color=(0, 128, 255),
                             semimajor_axis=120,
                             eccentricity=0.2)

    mars = CopernicusPlanet(name="Mars",
                            radius=3.4,
                            mass=10e+3,
                            color=(255, 40, 10),
                            semimajor_axis=160,
                            eccentricity=0.09)

    jupiter = CopernicusPlanet(name="Jupiter",
                               radius=20,
                               mass=2e+3,
                               color=(255, 200, 100),
                               semimajor_axis=220,
                               eccentricity=0.05)

    saturn = CopernicusPlanet(name="Saturn",
                              radius=15,
                              mass=2e+1,
                              color=(255, 255, 200),
                              semimajor_axis=300,
                              eccentricity=0.06)

    uranus = CopernicusPlanet(name="Uranus",
                              radius=12,
                              mass=3e+3,
                              color=(100, 255, 255),
                              semimajor_axis=380,
                              eccentricity=0.04)

    neptune = CopernicusPlanet(name="Neptune",
                               radius=12,
                               mass=0.02,
                               color=(50, 50, 255),
                               semimajor_axis=460,
                               eccentricity=0.01)

    pluto = CopernicusPlanet(name="Pluto",
                             radius=1.5,
                             mass=0.0146,
                             color=(200, 200, 200),
                             semimajor_axis=540,
                             eccentricity=0.25)

    planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
    # planets.append(pluto) = )

    sun = Sun(name='Sun',
              radius=30,
              mass=9e+4,
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
    space = CopernicusSpace(space_objects)

    create_space_objects(screen_size)
    engine = Engine(screen_size, bg_color, time_delta=0.1)
    engine.set_simulation_parameters(trace=args.trace,
                                     trace_length=args.trace_length,
                                     show_gravitational_radius=args.show_gravitational_radius,
                                     num_sun_rays=args.num_sun_rays)
    space.set_screen(engine.screen)
    engine.run(space)
