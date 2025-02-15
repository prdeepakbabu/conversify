import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class Themes:
    """Defines different themes for chat formatting (bw, color, modern, traditional)."""

    themes = {
        "bw": "color: black; background: white; font-family: Arial;",
        "color": "color: blue; background: lightgray; font-family: Verdana;",
        "modern": "color: darkslategray; background: white; font-family: Helvetica;",
        "traditional": "color: black; background: beige; font-family: Times New Roman;"
    }

    @staticmethod
    def get_style(theme):
        """Retrieves the CSS style for the specified theme.

        Args:
            theme (str): The name of the theme.

        Returns:
            str: The corresponding CSS style.
        """
        if theme not in Themes.themes:
            logging.warning("Requested theme '%s' not found, defaulting to 'bw'", theme)
        else:
            logging.info("Applying theme: %s", theme)
        return Themes.themes.get(theme, Themes.themes["bw"])
