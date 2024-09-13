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
        0: [0.0968833, 1.77317, 1.264],
        1: [1.33087, 0.693101, 1.80223],
        2: [0.315303, 2.71416, 0.696447],
        3: [0.353504, 0.0697012, 0.361935],
        4: [0.662356, 0.073004, 0.0939455],
        5: [-4.03548, -2.26276, 1.95411],
        6: [2.66466, -0.479367, 1.37559],
        7: [3.42888, 1.66575, -0.791453],
        8: [-0.0254608, 0.915112, 0.335678],
        9: [4.00603, -16.3377, 7.46537],
        10: [1.42206, 0.943326, 0.581255],
        11: [2.3517, 5.4152, -3.2978],
        12: [1.1159, 0.833911, -0.429364]
    }

    print_test_result(math.isclose(answers.get(variant)[0], x_1, rel_tol=1e-03, abs_tol=1e-03) and
                      math.isclose(answers.get(variant)[1], x_2, rel_tol=1e-03, abs_tol=1e-03) and
                      math.isclose(answers.get(variant)[2], x_3, rel_tol=1e-03, abs_tol=1e-03))


def task_3(variant, x_1, x_2, x_3):
    answers = {
        0: [0.597, 0.246, -0.881],
        1: [0.435393, 1.19918, 0.854251],
        2: [2.68177, -0.378547, 0.344393],
        3: [-0.0501454, -0.095175, 1.13761],
        4: [1.02483, -0.717518, -3.28158],
        5: [0.706922, 0.13147, -0.652621],
        6: [1.26763, 0.983518, 0.402159],
        7: [-4.78963, 0.631743, -1.92956],
        8: [0.458052, 0.609697, -2.01265],
        9: [0.52556, 0.467528, -2.50982],
        10: [0.0140315, -0.427274, -0.932843],
        11: [0.993543, 0.14247, 0.0704647],
        12: [0.529332, -0.269463, -0.436742],
    }

    print_test_result(math.isclose(answers.get(variant)[0], x_1, rel_tol=1e-03, abs_tol=1e-03) and
                      math.isclose(answers.get(variant)[1], x_2, rel_tol=1e-03, abs_tol=1e-03) and
                      math.isclose(answers.get(variant)[2], x_3, rel_tol=1e-03, abs_tol=1e-03))


def task_4(variant, x_1, x_2, x_3):
    answers = {
        0: [-0.916, 0.413, 1.184]
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
