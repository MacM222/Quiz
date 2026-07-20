# quiz_game.py
# A simple terminal-based quiz game in Python

def run_quiz():
    # List of quiz questions, options, and correct answers
    quiz_questions = [
        {
            "question": "What is my dog's name?",
            "options": ["A) True", "B) False"],
            "answer": "B, my dog's name is not the word \"What\" HAHAHAHAH GET IT!"
        },
        {
            "question": "What is the correct line?.",
            "options": ["A) Luke, I am your father.", "B) I am your father.", "C) No, I am your father."],
            "answer": "C"
        },
        {
            "question": "Which of the following words is spelled correctly?",
            "options": ["A) Pneumonoultramicroscopicsilicovolcanoconiosis", "B) Mississippi", "C) Committee", "D) Accomodate"],
            "answer": "D"
        }
    ]

    score = 0

    print("=== Welcome to the Quiz Game ===\n")
    for idx, q in enumerate(quiz_questions, start=1):
        print(f"Q{idx}: {q['question']}")
        for option in q["options"]:
            print(option)

        # Input validation loop
        while True:
            user_answer = input("Your answer (A/B/C/D): ").strip().upper()
            if user_answer in ["A", "B", "C", "D"]:
                break
            else:
                print("Invalid choice. Please enter A, B, C, or D.")

        if user_answer == q["answer"]:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Close! But not quite! The correct answer was {q['answer']}.\n")

    print(f"=== Quiz Finished! ===\nYour score: {score}/{len(quiz_questions)}")
    if score == len(quiz_questions):
        print("🎉 Perfect score! Well done!.")
    elif score >= len(quiz_questions) // 2:
        print("👍 You did good!")
    else:
        print("📚 Keep practicing!!")

if __name__ == "__main__":
    try:
        run_quiz()
    except KeyboardInterrupt:
        print("\nQuiz interrupted. Goodbye!")