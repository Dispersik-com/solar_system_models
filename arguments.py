import argparse

def create_arg_parser():
    """
    Create an argument parser and define the named arguments.

    Returns:
        argparse.ArgumentParser: The argument parser.
    """
    parser = argparse.ArgumentParser()

    # Define the named arguments here
    parser.add_argument('--screen_size', type=int, nargs=2, help='The size of the screen', default=(800, 800))
    parser.add_argument('--time_delta', type=float, help='The time delta', default=0.1)
    parser.add_argument('--trace', type=bool, help='Enable or disable tracing', default=False)
    parser.add_argument('--trace_length', type=int, help='The length of the trace', default=100)
    parser.add_argument('--show_gravitational_radius', type=bool, help='Enable or disable showing gravitational radius', default=False)
    parser.add_argument('--num_sun_rays', type=int, help='The number of sun rays', default=100)

    return parser