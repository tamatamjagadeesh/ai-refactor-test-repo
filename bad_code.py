def check(a, b, c):
    """
    Prints "changed again" if all conditions a, b, and c are true.

    Args:
        a: The first condition.
        b: The second condition.
        c: The third condition.
    """
    if all([a, b, c]):
        print("changed again")