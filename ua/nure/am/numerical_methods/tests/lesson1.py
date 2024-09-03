def task1(variant, number, significant_numbers):
    answers = {
        0: [0.001230, "1, 2, 3, 0"],
        1: []
    }

    return "Test passed." if (answers.get(variant)[0] == number and
                              answers.get(variant)[1] == significant_numbers) else "Test not passed. Try again."