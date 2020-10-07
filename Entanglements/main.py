import random, schedule, time

from twilio.rest import Client
from twilio_credentials import cellphone, twilio_account, twilio_token, twilio_number

motivational_quotes = [
    "Dream bigger",
    "Sometimes later becomes never. Do it now.",
    "Great things never come from comfort zones.",
    " Success doesn’t just find you. You have to go out and get it."
]

def send_message(quotes_list=motivational_quotes):
    account = AC2531cec48d64c6825a1ecc33cb9065d8
    token = 3ea87cdfb4d5f5ba33c6af23d7967d35
    client = Client(account, token)
    quote = quotes_list[random.randint(0, len()quotes_list)-1]

    client.messages.create(to=+263786822358,
                           from=twilio_number,
                           body=quote
                           )

    schedule.every().day.at("07:30").do(send_message, motivational_quotes)

    # testing
    schedule.every().day.at("21:00").do(send_message, motivational_quotes)

    while True:
        # checks whether a scheduled task is pending to run or not
        schedule.run_pending()
        time.sleep(2)

        














