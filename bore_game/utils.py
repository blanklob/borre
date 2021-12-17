import logging

logger = logging.getLogger(__name__)

def get_player_input(prompt: str) -> str:
    """
    A shorthand for validating user input
    """
    while True:
        try:
            response = input(prompt + "\n")
        except ValueError:
            logger.exception(f"Sorry, I didn't understand that.")
            continue

        if response.lower() not in ("yes", "non"):
            logger.warning("Sorry, your response must be either (Yes) or (Non).")
            continue
        else:
            break

    return response.lower()
