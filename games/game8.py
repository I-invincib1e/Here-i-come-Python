#!/usr/bin/env python3
"""
Game 8: Quiz Game
A simple CLI quiz with multiple choice questions.
"""

questions = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Paris", "Madrid"],
        "answer": "Paris"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Venus", "Mars", "Jupiter", "Saturn"],
        "answer": "Mars"
    },
    {
        "question": "What is 2 + 2?",
        "options": ["3", "4", "5", "6"],
        "answer": "4"
    },
    {
        "question": "Who wrote 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
        "answer": "William Shakespeare"
    }
]

def quiz_game():
    print("Welcome to Quiz Game!")
    score = 0

    for i, q in enumerate(questions, 1):
        print(f"\nQuestion {i}: {q['question']}")
        for j, option in enumerate(q['options'], 1):
            print(f"{j}. {option}")

        try:
            answer = int(input("Your answer (1-4): "))
            if 1 <= answer <= 4 and q['options'][answer-1] == q['answer']:
                print("Correct!")
                score += 1
            else:
                print(f"Wrong! The correct answer is {q['answer']}")
        except ValueError:
            print("Invalid input!")

    print(f"\nYour final score: {score}/{len(questions)}")

if __name__ == "__main__":
    quiz_game()
