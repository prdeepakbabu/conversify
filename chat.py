import json
import logging
from conversify.turn import Turn
from conversify.formatters import Formatters

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Chat:
    """Maintains a sequence of conversational turns.

    Attributes:
        user_name (str): The name of the user in the conversation.
        bot_name (str): The name of the bot in the conversation.
        turns (list): A list to store conversation turns.
        turn_counter (int): Keeps track of turn numbering.
    """

    def __init__(self, user_name="User", bot_name="Bot"):
        """Initializes a Chat instance.

        Args:
            user_name (str, optional): Name to represent the user. Defaults to "User".
            bot_name (str, optional): Name to represent the bot. Defaults to "Bot".
        """
        self.turns = []
        self.turn_counter = 1  # Maintains numbered sequence
        self.user_name = user_name
        self.bot_name = bot_name

        logging.info("Initialized Chat session with user_name='%s' and bot_name='%s'", user_name, bot_name)

    def add(self, turn: Turn):
        """Adds a new turn to the conversation.

        Args:
            turn (Turn): A Turn object representing a single interaction in the chat.
        """
        self.turns.append({"turn_number": self.turn_counter, "turn": turn.to_dict()})
        self.turn_counter += 1
        logging.info("Added Turn #%d: User='%s', Bot='%s'", self.turn_counter - 1, turn.user_msg, turn.response)

    def beautify(self, format="json"):
        """Returns a beautified chat in a specified format.

        Args:
            format (str, optional): The desired output format (json, md, html). Defaults to "json".

        Returns:
            str: Formatted chat conversation in the specified format.
        """
        if format not in ["json", "md", "html"]:
            logging.error("Unsupported format requested: %s", format)
            raise ValueError("Supported formats are: json, md, html")

        formatted_chat = Formatters.format_chat(self.turns, format, self.user_name, self.bot_name)
        logging.info("Chat formatted as %s", format)
        return formatted_chat

    def export(self, format="json"):
        """Exports the chat as a file.

        Args:
            format (str, optional): The desired output format (json, md, html). Defaults to "json".

        Returns:
            str: The filename where the chat is saved.
        """
        formatted_data = self.beautify(format=format)
        filename = f"chat_history.{format}"
        with open(filename, "w", encoding="utf-8") as f:
            f.write(formatted_data)
        logging.info("Chat exported to file: %s", filename)
        return filename
