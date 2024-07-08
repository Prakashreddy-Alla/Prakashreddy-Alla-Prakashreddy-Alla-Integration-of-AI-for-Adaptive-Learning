import random

math_questions_list_easy = {
    1: [
        "What is the rank of the following 2x3 matrix?\n| 1  2  3 |\n| 4  5  6 |",
        ["A) 2", "B) 3", "C) 1", "D) 0"],
        "A",
    ],
    2: [
        "Which of the following is an example of a scalar in linear algebra?",
        ["A) A vector", "B) A matrix", "C) A real number", "D) A complex number"],
        "C",
    ],
    3: [
        "What is the trace of a 3x3 identity matrix?",
        ["A) 3", "B) 0", "C) 1", "D) 2"],
        "A",
    ],
    4: [
        "In a matrix multiplication AB, if A is an m x n matrix and B is an n x p matrix, what is the size of the resulting matrix AB?",
        ["A) m x p", "B) n x n", "C) p x m", "D) n x m"],
        "A",
    ],
    5: [
        "The determinant of a 2x2 matrix [a b; c d] is calculated as:",
        ["A) ad - bc", "B) ac - bd", "C) ab - cd", "D) bc - ad"],
        "A",
    ],
}

math_questions_list_hard = {
    1: [
        "Question: What is the determinant of a 3x3 matrix with the following entries?\n| 2  0  1 |\n| 3  1 -2 |\n| 4  3  5 |",
        ["A) -26", "B) 26", "C) 34", "D) -34"],
        "A",
    ],
    2: [
        "Question: Which of the following matrices is not invertible (i.e., has no inverse)?",
        ["A) Identity matrix (3x3)", "B) A matrix with all elements equal to zero", "C) A matrix with all elements equal to one", "D) A matrix with zero determinant"],
        "D",
    ],
    3: [
        "Question: The eigenvectors of a matrix are linearly independent when:",
        ["A) They are orthogonal to each other", "B) They have different eigenvalues", "C) They are linearly dependent", "D) None of the above"],
        "B",
    ],
    4: [
        "Question: Which of the following operations changes the rank of a matrix?",
        ["A) Adding a multiple of one row to another row", "B) Multiplying all elements in a row by a non-zero constant", "C) Swapping two rows", "D) None of the above"],
        "D",
    ],
    5: [
        "Question: The transpose of a row matrix results in a:",
        ["A) Row matrix", "B) Column matrix", "C) Diagonal matrix", "D) Square matrix"],
        "B",
    ],
}


def validate_option(answer, options):
    for option in options:
        if answer.upper() == option[0].upper():
            return True
    return False

def generate_adaptive_test(questions_list):
    easy_question_indices = list(questions_list.keys())
    hard_question_indices = list(questions_list.keys())
    used_easy_questions = []
    used_hard_questions = []

    easy_crct = 0
    hard_crct = 0

    while easy_crct + hard_crct < len(questions_list):
        if easy_question_indices and (easy_crct < 2 or (easy_crct - hard_crct) < 1):
            question_index = random.choice(easy_question_indices)
            easy_question_indices.remove(question_index)
            used_easy_questions.append(question_index)
        elif hard_question_indices:
            question_index = random.choice(hard_question_indices)
            hard_question_indices.remove(question_index)
            used_hard_questions.append(question_index)
        else:
            print("No more questions in both categories. Exiting.")
            break

        question = questions_list[question_index]

        if question_index in used_easy_questions:
            print("\n\nEasy Question:\n", question[0])
        else:
            print("\n\nHard Question:\n", question[0])

        for choice in question[1]:
            print(choice)

        while True:
            answer = input("Your answer: ").strip().upper()

            if validate_option(answer, [option[0] for option in question[1]]):
                break
            else:
                print("Invalid option. Please select a valid option.")

        if answer == question[2]:
            if question_index in used_easy_questions:
                easy_crct += 1
            else:
                hard_crct += 1
        else:
            print("Incorrect!")

    print("\n\nEasy Questions Correct:", easy_crct)
    print("Hard Questions Correct:", hard_crct)

def main():
    print("\nWelcome to the Adaptive Math Test!")
    category = input("\nChoose the category (easy/hard): ").lower()

    if category == "easy":
        generate_adaptive_test(math_questions_list_easy)
    elif category == "hard":
        generate_adaptive_test(math_questions_list_hard)
    else:
        print("Invalid category. Please choose 'easy' or 'hard'.")

if __name__ == "__main__":
    main()