import logging
import os

from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter

# Initialize a Flask app to host the events adapter
app = Flask(__name__)
# Create an events adapter and register it to an endpoint in the slack app for event injestion.
slack_events_adapter = SlackEventAdapter(
    os.environ.get("SLACK_EVENTS_TOKEN"), "/slack/events", app
)


# When a 'message' event is detected by the events adapter, forward that payload
# to this function.
@slack_events_adapter.on("message")
def message(payload):
    """Parse the message event, and if the activation string is in the text,
    send a reply
    """

    # Get the event data from the payload
    event = payload.get("event", {})

    # Get the text from the event that came through
    text = event.get("text")

    # Check and see if the activation phrase was in the text of the message.
    if "hi" == text.lower():
        # Since the activation phrase was met
        # get the channel ID that the event was executed on
        channel_id = event.get("channel")

        # Execute the send message
        return send_message(channel_id, "Hello!")

    if "how are you" in text.lower():
        channel_id = event.get("channel")
        return send_message(channel_id, "Hello!")


def send_message(channel, text):
    # Initialize a Web API client
    slack_web_client = WebClient(token=os.environ.get("SLACK_TOKEN"))

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


if __name__ == "__main__":
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    logger.addHandler(logging.StreamHandler())

    # Run our app on our externally facing IP address on port 3000 instead of
    # running it on localhost, which is traditional for development.
    app.run(host="0.0.0.0", port=3000)
