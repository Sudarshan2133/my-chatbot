# 🧠 Open-Source Python Chatbot

This is a simple, fully open-source Python chatbot using the OpenRouter API.

## 🚀 Setup
```
pip install -r requirements.txt
python chatbot.py
```

## 🔑 Add API key
Edit `config.py` and add your OpenRouter API key.

## 📄 License
MIT License.

**System Requirements**

Python:
Python 3.13.9 or the latest stable version
Operating System Compatibility

Linux:
Must support systemctl (for daemon/service checks)
Requires read access to /etc/crontab

macOS:
Unix-based system
Requires read access to /etc/crontab
(systemctl is not available on macOS)

Windows:
No additional system requirements
File-based validation only


**Platform Support**

This project is designed to work across all major operating systems with minimal setup.

✅ Windows
Fully supported
No additional dependencies
Works out-of-the-box using Python and file-based validation

🟢 Linux (Ubuntu, Debian, Arch, Fedora, etc.)
Fully supported
Requires access to systemctl for service/daemon checks
Requires read access to /etc/crontab
Recommended for production or server setups

🍎 macOS (Intel & Apple Silicon)
Fully supported
Requires read access to /etc/crontab
Note: macOS does not provide systemctl


_**Setup & Installation**_

1. Clone the Repository
git clone https://github.com/Sudarshan2133/my-chatbot.git

2. Open the Project Folder
"cd my-chatbot"

3. Install Dependencies
Make sure you have Python + pip installed, then run:
"pip install -r requirements.txt"

4. Add Your API Key
Open the config.py file and replace the placeholder:
"API_KEY = "YOUR_OPENROUTER_API_KEY"
MODEL = "deepseek/deepseek-chat" "

5. Run the Chatbot
"python chatbot.py"

🎉 You're All Set!

Your chatbot is now ready to use. Start typing and enjoy interacting with your AI assistant.



"The Corpus.txt file contains Pre-added Responses and it won't Overlapp with the OpenRouter Models"

⚠️ Important Notice About OpenRouter Billing

OpenRouter is not fully free by default. You must manually select and use free-tier models (such as deepseek/deepseek-chat) to avoid charges.
If you run your chatbot with a paid model, OpenRouter will charge your account, even if it happens by mistake.

Before running the project, always double-check that the MODEL value in your config.py is set to a free model.
