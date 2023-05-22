# Sends a telegram message if the electricity price for the current hour falls to and below 0
# Nordpool site - https://www.nordpoolgroup.com/en/Market-data1/Dayahead/Area-Prices/ALL1/Hourly/?view=table
# Don't forget to replace your Telegram bot and chat IDs

from nordpool.elspot import Prices
from datetime import datetime, timedelta
import telegram
import asyncio

# Telegram Bot API token
bot_token = 'REPLACE YOUR TELEGRAM BOT API TOKEN'

# Telegram chat ID to send the notifications to
chat_id = 'YOUR BOT CHAT ID'

# Create an instance of the Prices class
prices = Prices()

# Get the current datetime
current_datetime = datetime.now()

# Calculate the end date by
end_date = current_datetime

# Fetch the hourly prices until the specified end date and for your area. In this example, we use FI
hourly_prices = prices.hourly(end_date=end_date, areas=['FI'])

# Since Nordpool is in CET, you might want to add or remove an hour or two, depending where you are located. Below it removes one hour.
current_hour = (current_datetime - timedelta(hours=1)).hour

# Find the price with the current hour (change your area from FI to whatever you want)
current_price = next(
    (item for item in hourly_prices['areas']['FI']['values'] if item['start'].hour == current_hour),
    None
)

if current_price:
    # Get the current hourly price for electricity
    current_price_value = current_price['value']
    #Check if the current Elspot price is 0 or lower
    # here you can adjust it to whateve you want
    if current_price_value <= 0:
      message = f"💡🌞 ⤵ Hour: {current_hour+1}\n"
      message += f"El. price ⇛ {current_price_value/10} cents"

      async def send_telegram_notification():
        # Send the notification to Telegram
        bot = telegram.Bot(token=bot_token)
        await bot.send_message(chat_id=chat_id, text=message)

      # Execute the send_telegram_notification coroutine using asyncio.run()
      asyncio.run(send_telegram_notification())
