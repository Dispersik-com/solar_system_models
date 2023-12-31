# solar_system_models

This project is a simple example of simulating the movement of planets based on the ideas of different scientists. In this case, models of Copernicus and Newton are implemented, but in the future, I would like also to implement Einstein's model.

The project includes the basic classes **Space** and **SpaceObject**. The subclasses of **Space** (**CopernicusSpace** and **NewtonSpace**) implement mathematical models.

In the Copernicus model each planet moves along its own geometric trajectory. In **CopernicusSpace** the calculation of the movement of each planet is independent.

![Copernicus model](https://github.com/Dispersik-com/solar_system_models/blob/master/screenshots/Copernicus.gif)

![Sun light](https://github.com/Dispersik-com/solar_system_models/blob/master/screenshots/sun-light.png)

In **NewtonSpace** the main focus is on gravitational force and interaction between the objects. Therefore, the primary calculations take place within the space itself.

![Newton model](https://github.com/Dispersik-com/solar_system_models/blob/master/screenshots/Newton.gif)

![Trace](https://github.com/Dispersik-com/solar_system_models/blob/master/screenshots/trace.png)

## Scientific Clarifications:

This work does not claim to be scientifically accurate and is created **just for fun**.

Therefore, there are the following clarifications:

1. The gravitational constant, used in the project, is much larger than the actual value. In the project, ~~G = 6.67430e-2~~, while the actual value is **G = 6.67430e-11**. It was done to scale the sphere of gravity.

2. Additionally, the mass of the planets is chosen using a table of [relative values](https://en.wikipedia.org/wiki/List_of_Solar_System_objects_by_size).

The Table of Relative Values:

Planet | Relative Radius | Relative Mass | Relative Speed
-------|----------------|---------------|---------------
Mercury | 0.383 | 0.055 | 0.240
Venus | 0.949 | 0.815 | 0.615
Earth | 1.0 | 1.0 | 1.0
Mars | 0.532 | 0.107 | 0.327
Jupiter | 11.209 | 317.8 | 13.07
Saturn | 9.449 | 95.2 | 9.69
Uranus | 4.007 | 14.5 | 6.81
Neptune | 3.883 | 17.1 | 5.43

## How to use:

`python3 run_Copernicus_model.py`

`python3 run_Newton_model.py`

### Args:

The defined named arguments are as follows:

**--screen_size** - specifies the size of the screen and expects two integer values. It has a default value of **(800, 800)**.

**--time_delta** - specifies the time delta for the simulation and expects a float value. It has a default value of **0.1**.

**--trace enables** -  or disables tracing. It expects a boolean value (True or False). It has a default value of **False**.

**--trace_length** - specifies the length of the trace and expects an integer value. It has a default value of **100**.

**--show_gravitational_radius** - enables or disables showing the gravitational radius. It expects a boolean value. It has a default value of **False**.

**--num_sun_rays** - specifies the number of sun rays and expects an integer value. It has a default value of **100**.

To enable the sun rays, simply click on the sun.

If you want to exit - press "q".


