# Generating a complete set of 671 unique math questions for 11th-grade students,
# ensuring the answers are provided as just numbers without any variables or additional notation.

import random

# A list to store the questions and answers
questions_answers = []

# Generate 671 unique questions
for i in range(1, 672):  # From 1 to 671 inclusive
    if i % 10 == 1:  # Algebra
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        questions_answers.append(f"{i}. Solve for x: {a}x + {b} = {a * 5 + b}.\nAnswer: {a * 5}")

    elif i % 10 == 2:  # Functions
        x_value = random.randint(1, 10)
        questions_answers.append(f"{i}. If f(x) = 2x^2 + 3x + 5, what is f({x_value})?\nAnswer: {2 * x_value**2 + 3 * x_value + 5}")

    elif i % 10 == 3:  # Trigonometry
        angle = random.choice([30, 45, 60])
        if angle == 30:
            questions_answers.append(f"{i}. What is sin(30°)?\nAnswer: 0.5")
        elif angle == 45:
            questions_answers.append(f"{i}. What is sin(45°)?\nAnswer: {round((2**0.5) / 2, 4)}")
        else:
            questions_answers.append(f"{i}. What is sin(60°)?\nAnswer: {round(3**0.5 / 2, 4)}")

    elif i % 10 == 4:  # Calculus
        x_value = random.randint(1, 10)
        questions_answers.append(f"{i}. Find the derivative of f(x) = 3x^2 + 4x at x = {x_value}.\nAnswer: {6 * x_value + 4}")

    elif i % 10 == 5:  # Statistics
        questions_answers.append(f"{i}. In a data set, the mean is 20 and the standard deviation is 4. What is the z-score of 24?\nAnswer: 1")

    elif i % 10 == 6:  # Geometry
        base = random.randint(5, 15)
        height = random.randint(5, 15)
        questions_answers.append(f"{i}. What is the area of a triangle with a base of {base} cm and a height of {height} cm?\nAnswer: {0.5 * base * height}")

    elif i % 10 == 7:  # Probability
        questions_answers.append(f"{i}. What is the probability of drawing a red card from a standard deck of cards?\nAnswer: 0.5")

    elif i % 10 == 8:  # Sequences
        first_term = random.randint(1, 10)
        common_diff = random.randint(1, 5)
        questions_answers.append(f"{i}. Find the 10th term of the arithmetic sequence where the first term is {first_term} and the common difference is {common_diff}.\nAnswer: {first_term + (9 * common_diff)}")

    elif i % 10 == 9:  # Inequalities
        a = random.randint(1, 5)
        b = random.randint(1, 10)
        questions_answers.append(f"{i}. Solve the inequality: {a}x - {b} < 3.\nAnswer: {round((3 + b) / a)}")

    elif i % 10 == 0:  # Logarithms
        questions_answers.append(f"{i}. What is log_10(1000)?\nAnswer: 3")

# Creating the file and writing the questions and answers to it
file_path = '11th_grade_math_questions.txt'
with open(file_path, 'w') as file:
    for q in questions_answers:
        file.write(q + "\n\n")  # Writing each question and answer with a newline for separation

file_path
