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
        0: [0.00030000000000002247, 0.0008547008547009188],
        1: []
    }

    print_test_result(math.isclose(answers.get(variant)[0], absolute_error) and
                      math.isclose(answers.get(variant)[1], relative_error))


def task3(variant, right_count, right_numbers, doubtful_count, doubtful_numbers):
    answers = {
        0: [3, '8, 5, 2', 2, '6, 7'], 1: [3, '7, 5, 7', 4, '8, 7, 3, 6'], 2: [4, '3, 8, 1, 7', 3, '2, 1, 6'],
        3: [3, '7, 8, 1', 4, '9, 5, 1, 3'], 4: [2, '0, 1', 4, '4, 5, 6, 8'], 5: [4, '2, 7, 8, 4', 3, '9, 1, 7'],
        6: [3, '8, 9, 3', 3, '4, 5, 3'], 7: [3, '1, 5, 4', 4, '5, 6, 5, 7'], 8: [3, '5, 8, 9', 4, '4, 2, 3, 6'],
        9: [3, '4, 2, 1', 4, '2, 8, 2, 5'], 10: [3, '9, 4, 5', 4, '6, 4, 3, 3'], 11: [3, '3, 3, 2', 4, '0, 6, 5, 3'],
        12: [3, '8, 0, 2', 2, '2, 8'], 13: [4, '4, 8, 5, 4', 3, '5, 4, 5'], 14: [3, '2, 1, 4', 4, '6, 0, 5, 2'],
        15: [5, '8, 0, 8, 4, 6', 2, '2, 1'], 16: [3, '8, 7, 3', 4, '7, 3, 0, 4'], 17: [4, '4, 7, 2, 2', 3, '3, 2, 9'],
        18: [4, '8, 1, 8, 7', 3, '2, 8, 3'], 19: [3, '6, 5, 9', 4, '2, 8, 1, 9'], 20: [4, '8, 4, 2, 5', 3, '6, 0, 5'],
        21: [4, '8, 7, 6, 1', 3, '3, 2, 4'], 22: [3, '3, 2, 9', 4, '9, 4, 9, 3'], 23: [4, '8, 2, 0, 9', 3, '3, 1, 1'],
        24: [4, '1, 0, 7, 8', 3, '1, 4, 1'], 25: [4, '3, 1, 7, 5', 3, '7, 1, 4'], 26: [3, '2, 3, 9', 4, '3, 2, 5, 7'],
        27: [5, '9, 5, 9, 2, 6', 1, '7'], 28: [3, '8, 3, 1', 4, '0, 0, 5, 5'], 29: [5, '6, 0, 4, 0, 3', 2, '8, 3'],
        30: [4, '1, 2, 4, 0', 3, '1, 2, 1']
    }

    print_test_result(answers.get(variant)[0] == right_count and
                      answers.get(variant)[1] == right_numbers and
                      answers.get(variant)[2] == doubtful_count and
                      answers.get(variant)[3] == doubtful_numbers)


def task4(variant, right_count, right_numbers, doubtful_count, doubtful_numbers):
    answers = {
        0: [4, '8, 5, 2, 6', 1, '7'], 1: [4, '7, 5, 7, 8', 3, '7, 3, 6'], 2: [4, '3, 8, 1, 7', 3, '2, 1, 6'],
        3: [4, '7, 8, 1, 9', 3, '5, 1, 3'], 4: [3, '0, 1, 4', 3, '5, 6, 8'], 5: [4, '2, 7, 8, 4', 3, '9, 1, 7'],
        6: [3, '8, 9, 3', 3, '4, 5, 3'], 7: [4, '1, 5, 4, 5', 3, '6, 5, 7'], 8: [4, '5, 8, 9, 4', 3, '2, 3, 6'],
        9: [4, '4, 2, 1, 2', 3, '8, 2, 5'], 10: [4, '9, 4, 5, 6', 3, '4, 3, 3'], 11: [4, '3, 3, 2, 0', 3, '6, 5, 3'],
        12: [3, '8, 0, 2', 2, '2, 8'], 13: [4, '4, 8, 5, 4', 3, '5, 4, 5'], 14: [4, '2, 1, 4, 6', 3, '0, 5, 2'],
        15: [5, '8, 0, 8, 4, 6', 2, '2, 1'], 16: [4, '8, 7, 3, 7', 3, '3, 0, 4'], 17: [4, '4, 7, 2, 2', 3, '3, 2, 9'],
        18: [4, '8, 1, 8, 7', 3, '2, 8, 3'], 19: [4, '6, 5, 9, 2', 3, '8, 1, 9'], 20: [4, '8, 4, 2, 5', 3, '6, 0, 5'],
        21: [4, '8, 7, 6, 1', 3, '3, 2, 4'], 22: [4, '3, 2, 9, 9', 3, '4, 9, 3'], 23: [4, '8, 2, 0, 9', 3, '3, 1, 1'],
        24: [4, '1, 0, 7, 8', 3, '1, 4, 1'], 25: [4, '3, 1, 7, 5', 3, '7, 1, 4'], 26: [4, '2, 3, 9, 3', 3, '2, 5, 7'],
        27: [5, '9, 5, 9, 2, 6', 1, '7'], 28: [4, '8, 3, 1, 0', 3, '0, 5, 5'], 29: [5, '6, 0, 4, 0, 3', 2, '8, 3'],
        30: [4, '1, 2, 4, 0', 3, '1, 2, 1']
    }

    print_test_result(answers.get(variant)[0] == right_count and
                      answers.get(variant)[1] == right_numbers and
                      answers.get(variant)[2] == doubtful_count and
                      answers.get(variant)[3] == doubtful_numbers)


def task5(variant, calculated_value, absolute_error, relative_error):
    answers = {
        0: [-0.0099, 0.03, 1.4925373],
        1: []
    }

    print_test_result(math.isclose(answers.get(variant)[0], calculated_value) and
                      math.isclose(answers.get(variant)[1], absolute_error) and
                      math.isclose(answers.get(variant)[2], relative_error))
