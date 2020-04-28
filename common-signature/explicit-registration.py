def step_one(input_data, reaction_paths, root_path):
    pass


def step_two(input_data, reaction_paths, root_path):
    pass


def step_three(input_data, reaction_paths, root_path):
    pass


## Explicit registration pattern
step_funcs = [step_one, step_two, step_three]
def invoke_all_steps(input_data, reaction_paths, root_path):
    for f in step_funcs:
        f(input_data, reaction_paths, root_path)




