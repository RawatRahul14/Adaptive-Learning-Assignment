# === Python Modules ===
import random

# === Main Body function to generate questions ===
def generate_question(
        age: int,
        level: str
) -> tuple[str, float]:
    """
    Generates a math puzzle based on the difficulty level and age.

    Args:
        age (int): The user's age
        level (str): The initial level the user selected

    Returns:
        question (str): formatted question (e.g. '8 + 5 = ?')
        answer (float): correct answer
    """
    ## === Scaling the numbers based on the user's age ===
    scale = 1 + (age - 5) * 0.1

    if level.lower() == "easy":
        a, b = random.randint(1, int(10 * scale)), random.randint(1, int(10 * scale))
        if age < 7:
            op = random.choice(
                ["+", "-"]
            )
        else:
            op = random.choice(
                ["+", "-", "*"]
            )

    elif level.lower() == "medium":
        a, b = random.randint(5, int(30 * scale)), random.randint(1, int(20 * scale))
        if age < 7:
            op = random.choice(
                ["+", "-"]
            )
        else:
            op = random.choice(
                ["+", "-", "*"]
            )

    else:
        if age >= 9 and random.random() < 0.5:
            a, b, c = random.randint(5, 20), random.randint(1, 10), random.randint(1, 5)
            op1 = random.choice(
                ["+", "-", "*"]
            )
            op2 = random.choice(
                ["+", "-", "*"]
            )
            question = f"({a} {op1} {b}) {op2} {c}"
            answer = eval(question)

            return question, answer

        a, b = random.randint(10, int(50 * scale)), random.randint(1, int(20 * scale))
        op = random.choice(["+", "-", "*", "/"])

    ## === Computing the naswers ===
    if op == "+":
        answer = a + b

    elif op == "-":
        answer = a - b

    elif op == "/":
        answer = round(a / b, 2)

    else:
        answer = a * b

    question = f"{a} {op} {b} = ?"

    return question, answer