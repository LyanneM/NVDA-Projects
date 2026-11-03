import random


MIN_NUMBER = 1
MAX_NUMBER = 100


def show_header():
    print("\n╭──────────────────────────────────────────╮")
    print("│           GUESS THE NUMBER               │")
    print("│        A little game of intuition        │")
    print("╰──────────────────────────────────────────╯")


def play():
    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    guesses = 0

    show_header()
    print(f"Hi! I am Lyanne, and Lyanne at the moment is thinking of a number between {MIN_NUMBER} to {MAX_NUMBER}.")
    print("Can you find it? Type 'q' whenever you want to quit.\n")

    while True:
        guess_text = input("  Your guess › ").strip()

        if guess_text.lower() == "q":
            print(f"\n  Aaaaww!You were so close! The number was {secret_number}. But no worries; you did it better than the other guy. Good job! See you next time!\n")
            break

        try:
            guess = int(guess_text)
        except ValueError:
            print("  That's not a number bestiee!\n")
            continue

        if not MIN_NUMBER <= guess <= MAX_NUMBER:
            print("  Bestie! The range! 1–100! XD\n")
            continue

        guesses += 1
        if guess < secret_number:
            print("  ↑ Too low bestie— try a little higher.\n")
        elif guess > secret_number:
            print("  ↓ Oof! Too high bestie — try a little lower.\n")
        else:
            print(f"\n  ✨ That's it! You got it in {guesses} { 'guess' if guesses == 1 else 'guesses' }. ✨\n")
            break


if __name__ == "__main__":
    play()
