import json
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Formatters:
    """Handles formatting of the chat object into different formats (JSON, Markdown, HTML)."""

    @staticmethod
    def format_chat(chat_data, output_format="json", user_name="User", bot_name="Bot"):
        """Formats the chat into the specified format.

        Args:
            chat_data (list): List of chat turns.
            output_format (str): The desired output format (json, md, html).
            user_name (str): The name representing the user.
            bot_name (str): The name representing the bot.

        Returns:
            str: The formatted chat conversation.
        """
        if output_format == "json":
            return Formatters.to_json(chat_data)
        elif output_format == "md":
            return Formatters.to_markdown(chat_data, user_name, bot_name)
        elif output_format == "html":
            return Formatters.to_html(chat_data, user_name, bot_name)
        else:
            logging.error("Unsupported format requested: %s", output_format)
            raise ValueError("Supported formats are: json, md, html")

    @staticmethod
    def to_json(chat_data):
        """Converts chat data to JSON format.

        Args:
            chat_data (list): The chat data.

        Returns:
            str: JSON formatted chat conversation.
        """
        logging.info("Formatting chat to JSON")
        return json.dumps(chat_data, indent=4)

    @staticmethod
    def to_markdown(chat_data, user_name, bot_name):
        """Converts chat data to Markdown format.

        Args:
            chat_data (list): The chat data.
            user_name (str): The name representing the user.
            bot_name (str): The name representing the bot.

        Returns:
            str: Markdown formatted chat conversation.
        """
        logging.info("Formatting chat to Markdown")
        md = ""
        for turn in chat_data:
            md += f"**{user_name}:** {turn['turn']['user_msg']}  \n"
            md += f"**{bot_name}:** {turn['turn']['response']}  \n\n"
        return md

    @staticmethod
    def to_html(chat_data, user_name, bot_name):
        """Converts chat data to HTML format.

        Args:
            chat_data (list): The chat data.
            user_name (str): The name representing the user.
            bot_name (str): The name representing the bot.

        Returns:
            str: HTML formatted chat conversation.
        """
        logging.info("Formatting chat to HTML")
        html = '<div style="font-family: Arial, sans-serif;">'
        for turn in chat_data:
            html += f'<p><b>{user_name}:</b> {turn["turn"]["user_msg"]}</p>'
            html += f'<p><b>{bot_name}:</b> {turn["turn"]["response"]}</p>'
            html += "<hr/>"
        html += "</div>"
        return html
