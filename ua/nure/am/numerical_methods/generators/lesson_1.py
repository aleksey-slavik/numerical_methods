import random


def get_numbers_list(number):
    number_str = str(number)
    numbers_list = []

    for char in number_str:
        if char != '.':
            numbers_list.append(int(char))

    return numbers_list


def get_number_order_value(number):
    number_str = str(number)
    return number_str.index('.') - 1


def get_omega_pow_value(omega, delta):
    power = -10
    while omega*(10**power) < delta:
        power += 1
    return power


def task_1_data_generator():
    result = {}

    for i in range(1, 31):
        number = round(random.uniform(0, 1), 6)
        rounded_number = round(number, 3)
        D_value = abs(number - rounded_number)
        d_value = D_value / abs(number)
        result[i] = [number, rounded_number, D_value, d_value]

    return result


def task_2_a_data_generator(number, delta):
    numbers_count = len(get_numbers_list(number))
    # print("numbers_count =", numbers_count)
    number_order = get_number_order_value(number)
    # print("number_order =", number_order)
    omega_pow = get_omega_pow_value(0.5, delta)
    # print("omega_pow =", omega_pow)
    right_count = -omega_pow + number_order + 1
    # print("right_count =", right_count)
    right_numbers = ", ".join(str(i) for i in get_numbers_list(number)[:right_count])
    # print("right_numbers =", right_numbers)
    doubtful_count = numbers_count - right_count
    # print("doubtful_count =", doubtful_count)
    doubtful_numbers = ", ".join(str(i) for i in get_numbers_list(number)[right_count:])
    # print("doubtful_numbers =", doubtful_numbers)
    return [right_count, right_numbers, doubtful_count, doubtful_numbers]


def task_2_b_data_generator(number, delta):
    numbers_count = len(get_numbers_list(number))
    # print("numbers_count =", numbers_count)
    number_order = get_number_order_value(number)
    # print("number_order =", number_order)
    omega_pow = get_omega_pow_value(1, delta)
    # print("omega_pow =", omega_pow)
    right_count = -omega_pow + number_order + 1
    # print("right_count =", right_count)
    right_numbers = ", ".join(str(i) for i in get_numbers_list(number)[:right_count])
    # print("right_numbers =", right_numbers)
    doubtful_count = numbers_count - right_count
    # print("doubtful_count =", doubtful_count)
    doubtful_numbers = ", ".join(str(i) for i in get_numbers_list(number)[right_count:])
    # print("doubtful_numbers =", doubtful_numbers)
    return [right_count, right_numbers, doubtful_count, doubtful_numbers]


def generate_task_2_test_data():
    result = {}

    for i in range(1, 31):
        result[i] = [round(random.uniform(0.01, 100), 5), round(random.uniform(0.00001, 0.01), 5)]

    return result


def generate_task_2_a_verification_data(test_data):
    result = {}

    for i in range(1, 31):
        number = test_data.get(i)[0]
        delta = test_data.get(i)[1]
        result[i] = task_2_a_data_generator(number, delta)

    return result


def generate_task_2_b_verification_data(test_data):
    result = {}

    for i in range(1, 31):
        number = test_data.get(i)[0]
        delta = test_data.get(i)[1]
        result[i] = task_2_b_data_generator(number, delta)

    return result


def generate_task_3_data():
    result = {}

    for i in range(1, 31):
        a = random.randint(1, 10)
        b = random.randint(-10, 10)
        c = random.randint(-10, 10)
        x = round(random.uniform(-1, 1), 2)
        d_x = random.uniform(-0.1, 0.1)
        f = round(a * x**2 + b * x + c + d_x, 2)
        result[i] = [a, b, c, x, f]

    return result


print(generate_task_3_data())
