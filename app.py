from flask import Flask, render_template
import requests

app = Flask(__name__)

# Your bot's API token and chat ID
bot_token = '7021561262:AAGxeBjFqw1I1NkyoT_dZiOYuoheZJQ7O58'  # Replace with your bot token
chat_id = '6935823453'  # Replace with your chat ID

# Function to send message to Telegram
def send_message_to_telegram(message):
    telegram_url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    data = {
        "chat_id": chat_id,
        "text": message
    }
    response = requests.post(telegram_url, data=data)
    return response.status_code

@app.route('/')
def home():
    # Fetch the public IP address
    response = requests.get("https://api.ipify.org")
    response_text = response.text  # This is the output from the API

    # Send the IP address to Telegram
    status_code = send_message_to_telegram(f"Here is the program output:\n{response_text}")

    # Render the HTML file located in the 'templates' folder
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)