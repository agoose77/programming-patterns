def step_one(input_data, reaction_paths, root_path):
    pass


def step_two(input_data, reaction_paths, root_path):
    pass


def step_three(input_data, reaction_paths, root_path):
    pass


# Name prefix pattern
def invoke_all_steps(input_data, reaction_paths, root_path):
    for name, value in globals().items():
        if name.startswith("step_") and callable(value):
            # If name prefixed with step, and the value is callable,
            # then we assume the value is a function taking these three args:
            value(input_data, reaction_paths, root_path)
