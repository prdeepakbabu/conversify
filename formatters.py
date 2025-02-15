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
    def truncate_snippet(snippet, max_length=100):
        """Truncates the snippet if it exceeds max_length."""
        if len(snippet) > max_length:
            return snippet[:50] + "..." + snippet[-50:]
        return snippet

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
        max_name_length = max(len(user_name), len(bot_name))
        md = ""
        for turn in chat_data:
            md += f"\n**Turn {turn['turn_number']}**  \n"
            md += f"**{user_name.ljust(max_name_length)}:** {turn['turn']['user_msg']}  \n"
            md += f"**{bot_name.ljust(max_name_length)}:** {turn['turn']['response']}  \n"

            if turn["turn"]["source_names"] and turn["turn"]["source_urls"]:
                sources = " | ".join([f"[{name}]({url})" for name, url in
                                      zip(turn["turn"]["source_names"], turn["turn"]["source_urls"])])
                md += f"source: {sources}  \n"
            if turn["turn"]["source_snippets"]:
                for snippet in turn["turn"]["source_snippets"]:
                    md += f"> {Formatters.truncate_snippet(snippet)}\\n"
            md += "\n"
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
        max_name_length = max(len(user_name), len(bot_name))
        html = '<div style="font-family: Arial, sans-serif;">'
        for turn in chat_data:
            html += f'<p><strong>Turn {turn["turn_number"]}</strong><br/></p>'
            html += f'<p><b>{user_name.ljust(max_name_length)}:</b> {turn["turn"]["user_msg"]}<br/></p>'
            html += f'<p><b>{bot_name.ljust(max_name_length)}:</b> {turn["turn"]["response"]}<br/></p>'

            if turn["turn"]["source_names"] and turn["turn"]["source_urls"]:
                sources = " | ".join([f'<a href="{url}" target="_blank">{name}</a>' for name, url in
                                      zip(turn["turn"]["source_names"], turn["turn"]["source_urls"])])
                html += f'<p><strong>Source:</strong> {sources}<br/></p>'
            if turn["turn"]["source_snippets"]:
                for snippet in turn["turn"]["source_snippets"]:
                    html += f'<blockquote style="white-space: pre-wrap;">{Formatters.truncate_snippet(snippet)}</blockquote>'
            html += "<hr/>"
        html += "</div>"
        return html
