import random

def generate_variable():
    return chr(random.randint(97, 122))

def generate_lambda_term(depth):
    if depth <= 0:
        return generate_variable()
    else:
        choice = random.choice([0, 1, 2])
        if choice == 0:
            # Generate a variable
            return generate_variable()
        elif choice == 1:
            # Generate an abstraction
            var = generate_variable()
            body = generate_lambda_term(depth - 1)
            return "(λ{}.{})".format(var, body)
        else:
            # Generate an application
            func = generate_lambda_term(depth - 1)
            arg = generate_lambda_term(depth - 1)
            return "({} {})".format(func, arg)

def fuzzer(num_terms, max_depth):
    for _ in range(num_terms):
        depth = random.randint(1, max_depth)
        term = generate_lambda_term(depth)
        print(term)

# Example usage:
fuzzer(num_terms=5, max_depth=10000)
