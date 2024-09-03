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


def task3_data_generator(number, delta):
    # print("Task 3 generated data for x =", number, ", delta =", delta)
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


def task4_data_generator(number, delta):
    # print("Task 4 generated data for x =", number, ", delta =", delta)
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


def generate_task3_test_data():
    result = {}

    for i in range(1, 31):
        result[i] = [round(random.uniform(0.01, 100), 5), round(random.uniform(0.00001, 0.01), 5)]

    return result


def generate_task3_verification_data(test_data):
    result = {}

    for i in range(1, 31):
        number = test_data.get(i)[0]
        delta = test_data.get(i)[1]
        result[i] = task3_data_generator(number, delta)

    return result


def generate_task4_verification_data(test_data):
    result = {}

    for i in range(1, 31):
        number = test_data.get(i)[0]
        delta = test_data.get(i)[1]
        result[i] = task4_data_generator(number, delta)

    return result


generated_data = generate_task3_test_data()
print(generated_data)
print(generate_task3_verification_data(generated_data))
print(generate_task4_verification_data(generated_data))
