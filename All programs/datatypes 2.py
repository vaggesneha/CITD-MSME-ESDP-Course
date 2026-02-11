
# A GAME ON DATATYPES
# Solve the snippets


levels = [
    {
        "code": "print(True + True + False)",
        "question": "Predict the output:",
        "answer": "2",
        "explanation": "In Python, True = 1 and False = 0. So True + True + False = 1 + 1 + 0 = 2."
    },
    {
        "code": "a = 256\nb = 256\nprint(a is b)\nx = 257\ny = 257\nprint(x is y)",
        "question": "Predict the output (True/False) for both lines, separated by comma:",
        "answer": "True,False",
        "explanation": "Python caches integers -5 to 256. 'a is b' is True, 'x is y' is False."
    },
    
    {
        "code": "t = ([],)\nt[0].append(1)\nprint(t)",
        "question": "Predict the output:",
        "answer": "([1],)",
        "explanation": "Tuple is immutable, but the inner list can be modified."
    },
    {
        "code": "print(0.1 + 0.2 == 0.3)",
        "question": "Predict the output (True/False):",
        "answer": "False",
        "explanation": "Floating point arithmetic is approximate, so 0.1 + 0.2 != 0.3 exactly."
    },
    
    {
        "code": "a = [1,2,3]\nb = [1,2,3]\nprint(a == b)\nprint(a is b)",
        "question": "Predict the output (first line, second line) separated by comma:",
        "answer": "True,False",
        "explanation": "'==' compares values, 'is' compares identity."
    },
    
    {
        "code": "s = 'abc'\nprint(s * 3)\nprint(s + '3')",
        "question": "Predict the output (first line, second line) separated by comma:",
        "answer": "abcabcabc,abc3",
        "explanation": "'*' repeats string, '+' concatenates string with another string."
    }
]

score = 0

print("Welcome to the Game on Data Types!")
print("In this game you need to predict the outputs based on given questions.\n")

for i, levels in enumerate(levels, start=1):
    print(f"Level {i}:")
    print("Code:\n", levels["code"])
    user_answer = input(levels["question"] + " ").replace(" ", "")
    
    if user_answer == levels["answer"].replace(" ", ""):
        print(" Correct!\n")
        score += 1
    else:
        print(f" Wrong!")
        print(f"Your answer: {user_answer}")
        print(f"Correct answer: {levels['answer']}")
        print(f"Explanation: {levels['explanation']}\n")

print(f"                    Game Over! Your Score: {score}/{6}")
