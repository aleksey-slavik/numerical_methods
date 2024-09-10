import math


def print_test_result(condition):
    print("\n-----------------------------------\n")

    if condition:
        print("Test passed.")
    else:
        print("Test not passed. Try again.")


def sample_test(variant):
    print("Test passed. Variant used:", variant)


def task_1(variant, x_1, x_2, x_3, x_4):
    answers = {
        0: [2.826, -0.334, -2.712, -0.669],
        1: [-0.0225523, -0.432345, -1.1676, 0.113034],
        2: [13.2008, -22.4937, -12.8617, -6.97447],
        3: [0.695397, 0.529181, -1.89384, 1.51409],
        4: [5.72172, 0.515894, 0.496228, -0.711057],
        5: [-0.044407, 2.06848, -11.0798, 6.01936],
        6: [0.614443, 0.753883, 0.359035, -0.219238],
        7: [0.425986, -0.865805, -1.44668, -9.81018],
        8: [-4.93248, -79.8521, -14.8117, 6.46438],
        9: [0.956192, 0.814315, 0.888016, 0.781347],
        10: [0.118807, 0.86783, 0.10531, -0.379594],
        11: [1.03143, 0.200174, -1.16546, -0.821393],
        12: [1.09262, 0.355106, 0.96596, 0.0166178],
        13: [0.0841662, 2.72291, 6.47156, -1.01346],
        14: [3.07724, 5.9307, -0.378308, -5.84766]
    }

    print_test_result(math.isclose(answers.get(variant)[0], x_1, rel_tol=1e-03, abs_tol=1e-03) and
                      math.isclose(answers.get(variant)[1], x_2, rel_tol=1e-03, abs_tol=1e-03) and
                      math.isclose(answers.get(variant)[2], x_3, rel_tol=1e-03, abs_tol=1e-03) and
                      math.isclose(answers.get(variant)[3], x_4, rel_tol=1e-03, abs_tol=1e-03))


def task_2(variant, x_1, x_2, x_3):
    answers = {
        0: [0.097, 1.773, 1.264]
    }

    print_test_result(math.isclose(answers.get(variant)[0], x_1, rel_tol=1e-03, abs_tol=1e-03) and
                      math.isclose(answers.get(variant)[1], x_2, rel_tol=1e-03, abs_tol=1e-03) and
                      math.isclose(answers.get(variant)[2], x_3, rel_tol=1e-03, abs_tol=1e-03))


def task_3(variant, x_1, x_2, x_3):
    answers = {
        0: [0.597, 0.246, -0.881]
    }

    print_test_result(math.isclose(answers.get(variant)[0], x_1, rel_tol=1e-03, abs_tol=1e-03) and
                      math.isclose(answers.get(variant)[1], x_2, rel_tol=1e-03, abs_tol=1e-03) and
                      math.isclose(answers.get(variant)[2], x_3, rel_tol=1e-03, abs_tol=1e-03))


def task_4(variant, x_1, x_2, x_3):
    answers = {
        0: [-3.023, 0.413, 1.184]
    }

    print_test_result(math.isclose(answers.get(variant)[0], x_1, rel_tol=1e-03, abs_tol=1e-03) and
                      math.isclose(answers.get(variant)[1], x_2, rel_tol=1e-03, abs_tol=1e-03) and
                      math.isclose(answers.get(variant)[2], x_3, rel_tol=1e-03, abs_tol=1e-03))


def task_5(variant, x_1, x_2, x_3, x_4, x_5):
    answers = {
        0: [0.973, 0.894, 0.695, 0.184, -1.704]
    }

    print_test_result(math.isclose(answers.get(variant)[0], x_1, rel_tol=1e-03, abs_tol=1e-03) and
                      math.isclose(answers.get(variant)[1], x_2, rel_tol=1e-03, abs_tol=1e-03) and
                      math.isclose(answers.get(variant)[2], x_3, rel_tol=1e-03, abs_tol=1e-03) and
                      math.isclose(answers.get(variant)[3], x_4, rel_tol=1e-03, abs_tol=1e-03) and
                      math.isclose(answers.get(variant)[4], x_5, rel_tol=1e-03, abs_tol=1e-03))
