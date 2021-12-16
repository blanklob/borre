def get_player_input(prompt: str) -> str:
    """
    Validates and returns user input
    """
    while True:
        try:
            response = input(prompt + "\n")
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if response.lower() not in ("yes", "non"):
            print("Sorry, your response must be either (Yes) or (Non).")
            continue
        else:
            break

    return response.lower()
