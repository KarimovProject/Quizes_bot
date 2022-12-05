import telegram


TOKEN = "5874141721:AAHprnHkQKf7XnaIGSinLI1Y-j8T2Blc_kI"

bot = telegram.Bot(token=TOKEN)

print(bot.get_me())