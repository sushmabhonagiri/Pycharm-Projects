


def fib_input(nth_count):
    fib_list = [0, 1]
    for x in range(1, nth_count - 1):
        # calc next value
        new_val = fib_list[x] + fib_list[x - 1]
        # print(new_val)
        fib_list.append(new_val)
        # append next value to list
    return fib_list


print(fib_input(9))

