import sys, time


def modify_primitive_number(n: float | int) -> None:
    n += 1


def increment_number_passed_in_list(lst) -> None:
    if lst is None or type(lst) is not list or len(lst) == 0:
        return
    if type(lst[0]) is int or type(lst[0]) is float:
        lst[0] += 1
    else:
        raise TypeError(f'Cannot increment something in a list that is not an int or float.  '
                        f'You passed in {type(lst[0])}')


def get_python_version() -> str:
    """ the version of python running this program"""
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'

def quizz_question1() -> None:
    favorite_color = "blue"

    if favorite_color != "blue":
        if favorite_color != "red":
            print("Must be yellow")
    elif favorite_color == "blue":
        if favorite_color != "yellow":
            print("Must be blue")
    elif favorite_color == "blue":
        if favorite_color != "yellow":
            print("I like purple")
    else:
        if favorite_color == "blue":
            print("Blue is the best")

def main():
    # as a primitive (int or float), our method does not affect the value (pass by value)
    n: float = 4.6
    print(f'before, {n =}')
    modify_primitive_number(n)
    print(f'after, {n =}')

    # use the 'trick' of passing the value as a in order to get pass by reference
    n: list[float | int] = [3.14159, ]
    print(f'before, {n =}')
    increment_number_passed_in_list(n)
    print(f'after, {n =}')
    n = n[0]
    print(f'after, {n = }')

    # this should fail
    n: list[str] = ['3.14159',]
    print(f'before, {n =}')
    try:
        increment_number_passed_in_list(n)
    except Exception as e:
        print(e, file = sys.stderr, flush = True)
        time.sleep(0.0115) # force error message to appear before Finally message.
    finally:
        print(f'after, {n =}')


    # quizz_question1()


if __name__ == "__main__":
    print(f'Python version: {get_python_version()}')
    main()
