import os
import random
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

# Load .env
load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

# Jokes list
jokes = [
    "Why did the math book look sad? Because it had too many problems.",
    "Why don't scientists trust atoms? Because they make up everything!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!",
    "Why did the tomato turn red? Because it saw the salad dressing!",
    "Why don’t skeletons fight each other? They don’t have the guts.",
    "Why ix shortbread called shortbread? Because it's so short! (And delicious!)",
    "Why did the bicycle fall over? Because it was two-tired!",
    "Why did the golfer bring two pairs of pants? In case he got a hole in one!",
    "Why did the cookie go to the doctor? Because it felt crummy!",
    "Why did the computer go to the doctor? Because it had a virus!",
    "Why did the chicken join a band? Because it had the drumsticks!"
]

# Optional images/gifs for jokes
joke_images = [
    "https://media.giphy.com/media/3o7aD2saalBwwftBIY/giphy.gif",
    "https://media.giphy.com/media/l41lFw057lAJQMwg0/giphy.gif",
    "https://media.giphy.com/media/26ufdipQqU2lhNA4g/giphy.gif",

]

# Track how many jokes each user has seen
user_joke_count = {}

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_joke_count[user_id] = 0
    await update.message.reply_text(
        f"Hello, {update.effective_user.first_name}! I'm your Joke Bot 🤖\nType /joke to hear a joke!"
    )

# /help command
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Commands:\n"
        "/start - Greet the user\n"
        "/help - Show this message\n"
        "/joke - Tell a random joke\n"
        "/count - See how many jokes you've received"
    )

# /joke command
async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    user_joke_count[user_id] = user_joke_count.get(user_id, 0) + 1

    joke_text = random.choice(jokes)
    await update.message.reply_text(joke_text)

    # 50% chance to send a funny gif/image
    if random.choice([True, False]):
        image_url = random.choice(joke_images)
        await update.message.reply_animation(image_url)

# /count command
async def count(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    count = user_joke_count.get(user_id, 0)
    await update.message.reply_text(f"You've seen {count} joke(s) so far!")

# Main
app = ApplicationBuilder().token(TOKEN).build()

# Add handlers
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("joke", joke))
app.add_handler(CommandHandler("count", count))

print("Advanced Joke Bot is running...")
app.run_polling()