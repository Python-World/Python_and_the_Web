import os

from slack import WebClient

# Create a slack client
slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))


def send_message(channel, text):
    # message payload
    message = {
        "channel": channel,
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": (text),
                },
            },
        ],
    }

    # Post the onboarding message in Slack
    slack_web_client.chat_postMessage(**message)


send_message("#bebas", "Hola!")
