import discord
import google.generativeai as genai
import random
from collections import defaultdict, deque

print("🚀 Starting Jignesh bot...")

# Keys (replace with yours)
DISCORD_TOKEN = "TOKEN_HERE"
GEMINI_API_KEY = "KEY_HERE"

# Setup Gemini
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

# Setup Discord client
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
client = discord.Client(intents=intents)

# Store conversation history per user per channel
conversation_history = defaultdict(lambda: defaultdict(lambda: deque(maxlen=10)))

# Store active users per channel
active_users = {}  # channel_id -> user_id

# Default personality
DEFAULT_PERSONALITY = (
    "u are a person named jignesh made by Cultsicarias"
    "give answers that are not too lengthy and short"
    "fill it with emojis relevant to the answer"
    "be as funny as possible while not being rude"
    "sneak in japanese when u deem fit"

)
JIGNESH_PERSONALITY = DEFAULT_PERSONALITY

# Random roast intros
ROAST_INTROS = [
    "💀 Brace yourself…",
    "🔥 Oh, this is bad…",
    "☠️ Another victim!",
    "😈 You asked for it:",
    "😏 Dark truth incoming:",
    "⚡ Let's make this quick:",
]

@client.event
async def on_ready():
    print(f"✅ Logged in as {client.user}")

@client.event
async def on_message(message):
    global JIGNESH_PERSONALITY

    if message.author == client.user:
        return

    content = message.content.strip()
    channel_id = message.channel.id
    user_id = message.author.id

    # --- Reset ---
    if content.lower() == "jignesh reset":
        conversation_history[channel_id].pop(user_id, None)
        active_users.pop(channel_id, None)
        JIGNESH_PERSONALITY = DEFAULT_PERSONALITY
        await message.channel.send(
            f"{message.author.mention} ✅ Reset done. Memory + Personality wiped."
        )
        return

    # --- Personality Change ---
    if content.lower().startswith("jignesh personality "):
        new_persona = content[len("jignesh personality "):].strip()
        if new_persona:
            JIGNESH_PERSONALITY = new_persona
            await message.channel.send(
                f"{message.author.mention} 🎭 Personality updated successfully!"
            )
        else:
            await message.channel.send(
                f"{message.author.mention} ⚠️ Provide a personality text!"
            )
        return

    # --- Roast Me ---
    if content.lower() == "jignesh roast me":
        active_users[channel_id] = user_id
        async with message.channel.typing():
            response = model.generate_content(
                "You are Jignesh, a dark, savage AI. Roast the user brutally with short, punchy dark humor."
            )
            roast = response.text.strip()
            intro = random.choice(ROAST_INTROS)

            embed = discord.Embed(
                title="💀 Jignesh's Dark Roast",
                description=f"{intro} {roast}",
                color=0x8B0000
            )
            embed.set_footer(text=f"Victim: {message.author.display_name}")
            await message.channel.send(content=message.author.mention, embed=embed)
        return

    # --- Normal Chat Mode ---
    if content.lower().startswith("jignesh") or active_users.get(channel_id) == user_id:
        if content.lower().startswith("jignesh"):
            active_users[channel_id] = user_id
            user_message = content[len("jignesh"):].strip()
        else:
            user_message = content

        history = conversation_history[channel_id][user_id]
        history_text = "\n".join([f"{h['role']}: {h['content']}" for h in history])

        prompt = (
            f"{JIGNESH_PERSONALITY}\n"
            f"Conversation so far:\n{history_text}\n"
            f"User: {user_message}\nJignesh:"
        )

        async with message.channel.typing():
            response = model.generate_content(prompt)
            reply = response.text.strip()

        # Save to history
        history.append({"role": "user", "content": user_message})
        history.append({"role": "assistant", "content": reply})

        embed = discord.Embed(
            title="😈 Jignesh says:",
            description=reply,
            color=0x8B0000
        )
        embed.set_footer(text=f"Talking to {message.author.display_name}")
        await message.channel.send(content=message.author.mention, embed=embed)


# --- Run the bot ---
client.run(DISCORD_TOKEN)
