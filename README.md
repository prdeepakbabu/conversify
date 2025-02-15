# Conversify 🚀

Conversify is a Python package designed to structure, format, and beautify chat conversations. It supports **JSON, Markdown, and HTML** formats, with themes to enhance the visual appeal of conversations.A lightweight Python package that formats and visualizes chat interactions with pretty-printing, different output styles, supporting themes and optional export options. Conversify is designed to solve the challenges of structuring, formatting, and presenting conversational data in a clear and readable manner. In AI-driven applications, chat interactions often lack consistency, making it difficult to analyze, document, or visualize them effectively. Conversify standardizes chat logs by offering flexible formatting options in JSON, Markdown, and HTML, ensuring conversations are well-organized and easily interpretable. It enhances readability through proper indentation, metadata integration, and turn numbering, while also supporting hyperlinked citations and source snippets for traceability. Whether for chatbot development, customer interaction analysis, or conversational AI research, Conversify simplifies the process by transforming raw chat data into structured, professional, and shareable formats.

### 🎯 Features
✅ **Add multiple conversation turns** dynamically.  
✅ **Format chat conversations** into JSON, Markdown, and HTML.  
✅ **Support for themes** (`bw`, `color`, `modern`, `traditional`) in HTML output.  
✅ **Export chats** to a file or print inline.  
✅ **Easily configurable** (user/bot names, themes, output formats).  
✅ **Unit-tested** for robustness.
---
## 📦 Installation
```sh
pip install conversify
```

## 🚀 Quick Start
### 1️⃣ **Initialize Conversify**
```python
from conversify.conversify import Conversify
from conversify.turn import Turn

# Create a Conversify instance
chat = Conversify(format="html", theme="modern", export=False, user_name="Alice", bot_name="AI Assistant")
```

### 2️⃣ **Add Conversation Turns**
```python
chat.add_turn(
    Turn("Hello, how are you?", "I'm good! How can I assist you today?"),
    Turn("What is AI?", "AI stands for Artificial Intelligence, enabling machines \
    to learn and make decisions.")
)
```

### 3️⃣ **Generate Output**
```python
# Print formatted output
print(chat.to_json())  # JSON format
print(chat.to_md())    # Markdown format
print(chat.to_html())  # HTML format
```

### 4️⃣ **Export to File**
```python
chat.export = True  # Enable exporting
chat.to_html()  # Saves as `chat_history.html`
```


## 🎨 Themes
| Theme       | Description |
|------------|-------------|
| `bw`        | Black & White minimal style |
| `color`     | Colored UI for better readability |
| `modern`    | Sleek and contemporary look |
| `traditional` | Classic old-school typography |


## 🛠 API Reference
### **Conversify Class**
```python
Conversify(format="json", theme="bw", export=False, user_name="User", bot_name="Bot")
```
| Parameter  | Type   | Default | Description |
|------------|--------|---------|-------------|
| format     | `str`  | `json`  | Output format (`json`, `md`, `html`) |
| theme      | `str`  | `bw`    | Chat display theme |
| export     | `bool` | `False` | Save output to file |
| user_name  | `str`  | `User`  | Name of the user |
| bot_name   | `str`  | `Bot`   | Name of the chatbot |


## 🤝 Contributing
1. Fork the repository 🍴
2. Create a feature branch 🌱
3. Commit your changes ✅
4. Open a pull request 🚀


## 📜 License
MIT License © 2025 Conversify Developers


## 📢 Connect With Us
💬 Discussions: [GitHub Discussions](https://github.com/prdeepakbabu/conversify/issues)  
🐦 Twitter: [@ConversifyAI](https://twitter.com/ConversifyAI)  
📧 Email: support@conversify.com
