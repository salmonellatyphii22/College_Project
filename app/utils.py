import os


def save_history(prompt, category):

    os.makedirs("history", exist_ok=True)

    with open("history/history.txt", "a") as file:
        file.write(f"Prompt: {prompt}\n")
        file.write(f"Category: {category}\n")
        file.write("-"*40+"\n")