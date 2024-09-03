import math


def print_test_result(condition):
    if condition:
        print("Test passed.")
    else:
        print("Test not passed. Try again.")


def sample_test(variant):
    print("Test passed. Variant used:", variant)


def task1(variant, number, significant_numbers):
    answers = {
        0: [0.001230, "1, 2, 3, 0"],
        1: []
    }

    print_test_result(answers.get(variant)[0] == number and
                      answers.get(variant)[1] == significant_numbers)


def task2(variant, absolute_error, relative_error):
    answers = {
        0: [0.0013, 0.003714],
        1: []
    }

    print_test_result(math.isclose(answers.get(variant)[0], absolute_error) and
                      math.isclose(answers.get(variant)[1], relative_error))


def task3(variant, right_count, right_numbers, doubtful_count, doubtful_numbers):
    answers = {
        0: [5, "1, 7, 6, 8, 7", 2, "1, 4"],
        1: []
    }

    print_test_result(answers.get(variant)[0] == right_count and
                      answers.get(variant)[1] == right_numbers and
                      answers.get(variant)[2] == doubtful_count and
                      answers.get(variant)[3] == doubtful_numbers)


def task4(variant, right_count, right_numbers, doubtful_count, doubtful_numbers):
    answers = {
        0: [5, "1, 7, 6, 8, 7", 2, "1, 4"],
        1: []
    }

    print_test_result(answers.get(variant)[0] == right_count and
                      answers.get(variant)[1] == right_numbers and
                      answers.get(variant)[2] == doubtful_count and
                      answers.get(variant)[3] == doubtful_numbers)


def task5(variant, calculated_value, absolute_error, relative_error):
    answers = {
        0: [5, "1, 7, 6, 8, 7", 2, "1, 4"],
        1: []
    }

    print_test_result(math.isclose(answers.get(variant)[0], calculated_value) and
                      math.isclose(answers.get(variant)[1], absolute_error) and
                      math.isclose(answers.get(variant)[2], relative_error))

