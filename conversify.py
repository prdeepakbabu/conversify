import logging
import json
from conversify.turn import Turn
from conversify.formatters import Formatters
from conversify.themes import Themes

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Conversify:
    """Main class to handle chat conversations with configurable output settings.

    Attributes:
        format (str): Output format (json, md, html).
        theme (str): Theme for HTML output.
        export (bool): Whether to export the formatted chat to a file.
        user_name (str): The name of the user in the conversation.
        bot_name (str): The name of the bot in the conversation.
        turns (list): A list to store conversation turns.
    """

    def __init__(self, format="json", theme="bw", export=False, user_name="User", bot_name="Bot"):
        """Initializes Conversify with configuration settings.

        Args:
            format (str, optional): The output format (json, md, html). Defaults to "json".
            theme (str, optional): The theme for HTML output. Defaults to "bw".
            export (bool, optional): Whether to export the output to a file. Defaults to False.
            user_name (str, optional): Name to represent the user. Defaults to "User".
            bot_name (str, optional): Name to represent the bot. Defaults to "Bot".
        """
        if format not in ["json", "md", "html"]:
            logging.error("Unsupported format requested: %s", format)
            raise ValueError("Supported formats are: json, md, html")

        self.format = format
        self.theme = theme
        self.export = export
        self.user_name = user_name
        self.bot_name = bot_name
        self.turns = []

        logging.info("Initialized Conversify with format='%s', theme='%s', export='%s'", format, theme, export)

    def add_turn(self, *turns):
        """Adds one or more turns to the conversation.

        Args:
            *turns (Turn): One or more Turn objects to be added.
        """
        for turn in turns:
            self.turns.append({"turn_number": len(self.turns) + 1, "turn": turn.to_dict()})
            logging.info("Added Turn #%d: User='%s', Bot='%s'", len(self.turns), turn.user_msg, turn.response)

    def to_json(self):
        """Generates JSON output for the chat conversation.

        Returns:
            str: JSON formatted conversation.
        """
        output = Formatters.to_json(self.turns)
        self._handle_output(output, "json")
        return output

    def to_md(self):
        """Generates Markdown output for the chat conversation.

        Returns:
            str: Markdown formatted conversation.
        """
        output = Formatters.to_markdown(self.turns, self.user_name, self.bot_name)
        self._handle_output(output, "md")
        return output

    def to_html(self):
        """Generates HTML output for the chat conversation.

        Returns:
            str: HTML formatted conversation.
        """
        output = Formatters.to_html(self.turns, self.user_name, self.bot_name)
        self._handle_output(output, "html")
        return output

    def _handle_output(self, output, extension):
        """Handles output printing or exporting based on configuration.

        Args:
            output (str): The formatted chat output.
            extension (str): The file extension for export.
        """
        if self.export:
            filename = f"chat_history.{extension}"
            with open(filename, "w", encoding="utf-8") as f:
                f.write(output)
            logging.info("Chat exported to file: %s", filename)
        else:
            print(output)
