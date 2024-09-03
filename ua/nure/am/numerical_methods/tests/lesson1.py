def print_test_result(condition):
    if condition:
        print("Test passed.")
    else:
        print("Test not passed. Try again.")

def sample_test(variant):
    print("Test passed.")

def task1(variant, number, significant_numbers):
    answers = {
        0: [0.001230, "1, 2, 3, 0"],
        1: []
    }

    print_test_result(answers.get(variant)[0] == number and answers.get(variant)[1] == significant_numbers)