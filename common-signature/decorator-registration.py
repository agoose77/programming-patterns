step_funcs = []


# This is the same thing as `register_step = step_funcs.append`, except
# because list.append doesn't return the object you're appending, instead returning `None`,
# the functions `step_one`, `step_two`, ..., would be set equal to `None`,
# and therefore only available from the `step_funcs` list
def register_step(f):
    step_funcs.append(f)
    return f


@register_step
def step_one(input_data, reaction_paths, root_path):
    pass


@register_step
def step_two(input_data, reaction_paths, root_path):
    pass


@register_step
def step_three(input_data, reaction_paths, root_path):
    pass


## Decorator registration pattern
def invoke_all_steps(input_data, reaction_paths, root_path):
    for f in step_funcs:
        f(input_data, reaction_paths, root_path)




