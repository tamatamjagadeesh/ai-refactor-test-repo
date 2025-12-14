def process(x, y, z):
    """
    Prints "valid" if all input conditions (x, y, and z) are true.

    Args:
        x: The first boolean condition.
        y: The second boolean condition.
        z: The third boolean condition.
    """
    if all([x, y, z]):
        print("valid")