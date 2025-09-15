## Jignesh Discord Bot

A fun, emoji-filled, slightly savage Discord bot powered by Google Gemini. It supports light memory per user per channel, custom personalities, and a spicy "roast me" mode.

### Features
- **Conversation memory**: Remembers the last few messages per user in a channel
- **Custom personality**: Change the bot's style on the fly
- **Roast mode**: Short, punchy dark humor on demand
- **Embeds**: Clean, formatted responses in Discord

### Commands
- **jignesh ...**: Talk to the bot. Example: `jignesh hello`
- **jignesh roast me**: Get roasted
- **jignesh personality <text>**: Change persona. Example: `jignesh personality be a wholesome anime senpai`
- **jignesh reset**: Clear memory and reset personality

---

## 1) Prerequisites
- **Python**: 3.10+ recommended
- **Pip**: comes with Python
- A Discord account with permission to add a bot to your server

## 2) Create a Discord Bot
1. Open the [Discord Developer Portal](https://discord.com/developers/applications)
2. Click "New Application" → name it (e.g., "Jignesh")
3. Go to "Bot" tab → "Add Bot" → Confirm
4. Under "Privileged Gateway Intents", enable:
   - MESSAGE CONTENT INTENT
   - (Messages intent is enabled by default in code)
5. Click "Reset Token" → copy the token (you'll use it below)

## 3) Invite the Bot to Your Server
1. Go to "OAuth2" → "URL Generator"
2. Scopes: check `bot`
3. Bot Permissions: check `Send Messages`, `Embed Links`
4. Copy the generated URL and open it → choose your server → Authorize

## 4) Get a Google Gemini API Key
1. Go to [Google AI Studio](https://aistudio.google.com/) and sign in
2. Create an API key → copy it

## 5) Setup the Project
```bash
# Clone or download this repo, then in a terminal:
cd JigneshGPT

# (Optional but recommended) Create a virtual environment
# Windows (Command Prompt):
python -m venv .venv
.\.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
# Copy the example and fill in your keys
copy env.example .env
# Then edit .env and set values for:
#   DISCORD_TOKEN=...
#   GEMINI_API_KEY=...

# Run the bot
python bot.py
```

> On PowerShell, replace `copy` with `Copy-Item env.example .env`.

## 6) Usage Tips
- Start messages with `jignesh` to talk, or continue the thread after activating once
- Use `jignesh personality <text>` to change style dynamically
- Use `jignesh reset` if things feel off or too long

## Environment Variables
- **DISCORD_TOKEN**: Your Discord bot token
- **GEMINI_API_KEY**: Your Google Gemini API key

You can set these via a `.env` file in the project root, or as real environment variables. The app uses `python-dotenv` to load `.env` automatically.

## Troubleshooting
- **Missing intents / bot not responding**: Ensure "Message Content Intent" is enabled in the Bot tab and the bot has permission to send messages in the channel.
- **Invalid token**: Regenerate the Discord bot token and update `.env`.
- **Gemini API errors**: Verify your `GEMINI_API_KEY` and that the model `gemini-1.5-flash` is available to your key.
- **ImportError for dotenv/discord**: Run `pip install -r requirements.txt` in the same environment you execute `python bot.py`.

## Security
- Never commit your real `.env` with secrets. The repo includes `env.example` only.
- If a token was exposed, rotate it in Discord Developer Portal and Google AI Studio.

## Project Structure
```text
JigneshGPT/
├─ bot.py              # Main Discord bot
├─ personalities.py    # Predefined personalities (optional reference)
├─ requirements.txt    # Python dependencies
├─ env.example         # Template for environment variables (copy to .env)
```

## License
MIT (or your preferred license)
