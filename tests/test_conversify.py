import unittest
import json
import os
from conversify.conversify import Conversify
from conversify.turn import Turn

class TestConversify(unittest.TestCase):
    """Unit tests for the Conversify class."""

    def setUp(self):
        """Setup a Conversify instance before each test."""
        self.conversify = Conversify(format="json", theme="bw", export=False)
        self.turn1 = Turn("Hello, how are you?", "I'm good! How can I assist you today?")
        self.turn2 = Turn("What is AI?", "AI stands for Artificial Intelligence, enabling machines to learn and make decisions.")

    def test_add_turn(self):
        """Test adding turns to the conversation."""
        self.conversify.add_turn(self.turn1, self.turn2)
        self.assertEqual(len(self.conversify.turns), 2)
        self.assertEqual(self.conversify.turns[0]["turn"]["user_msg"], "Hello, how are you?")

    def test_to_json(self):
        """Test JSON output generation."""
        self.conversify.add_turn(self.turn1, self.turn2)
        output = self.conversify.to_json()
        json_data = json.loads(output)
        self.assertEqual(len(json_data), 2)
        self.assertIn("user_msg", json_data[0]["turn"])

    def test_to_md(self):
        """Test Markdown output generation."""
        self.conversify.add_turn(self.turn1, self.turn2)
        output = self.conversify.to_md()
        self.assertIn("**User:** Hello, how are you?", output)

    def test_to_html(self):
        """Test HTML output generation."""
        self.conversify.add_turn(self.turn1, self.turn2)
        output = self.conversify.to_html()
        self.assertIn("<b>User:</b> Hello, how are you?", output)

    def test_export_json(self):
        """Test exporting JSON output to a file."""
        self.conversify.export = True
        self.conversify.add_turn(self.turn1)
        self.conversify.to_json()
        self.assertTrue(os.path.exists("chat_history.json"))
        os.remove("chat_history.json")

    def test_export_md(self):
        """Test exporting Markdown output to a file."""
        self.conversify.export = True
        self.conversify.add_turn(self.turn1)
        self.conversify.to_md()
        self.assertTrue(os.path.exists("chat_history.md"))
        os.remove("chat_history.md")

    def test_export_html(self):
        """Test exporting HTML output to a file."""
        self.conversify.export = True
        self.conversify.add_turn(self.turn1)
        self.conversify.to_html()
        self.assertTrue(os.path.exists("chat_history.html"))
        os.remove("chat_history.html")

if __name__ == "__main__":
    unittest.main()
