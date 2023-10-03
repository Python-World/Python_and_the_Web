import sys

from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client


def send_message_phone(phone, body):
    account_sid = "<YOUR ACCOUNT_SID>"  # Replace this with your account sid
    auth_token = (
        "<YOUR AUTH_TOKEN>"  # Replace this with your account Auth Token
    )
    # Create a client object from Twilio Rest
    client = Client(account_sid, auth_token)
    retry_count = 0
    while retry_count < 3:
        try:
            # Create a client which internally call the Twilio API to send request
            message = client.messages.create(
                body="{}".format(body),
                from_="<NEW PHONE NUMBER>",  # Place your newly created phone number here,
                to="{}".format(phone),
            )
            break
        except TwilioRestException as e:
            # This is the error code that most commonly people will encounter, because they will try to send SMS to unverified numbers
            if e.code == 21608:
                print(
                    "You can't send messages to unverified numbers from trial account"
                )
                return False
            print(e)
        except Exception as e:
            # General exception which would have happened in the code
            print(e)

        retry_count += 1

    if retry_count == 3:
        return False
    # Send True by default, all other cases are handled above
    return True


def initiate():
    to_phone_number = None
    message = None

    if len(sys.argv) > 1:
        if sys.argv[1] == "help":
            print("\nTwilio SMS - usage")
            print(
                'twilio_sms +917894561230 "Your message" - Requires phone number with country code and your SMS message'
            )
            print("twilio_sms help - Prints this message\n")
            sys.exit()
        if len(sys.argv) != 3:
            print("twilio_sms help - for usage")
            sys.exit()

        to_phone_number = sys.argv[1]
        message = sys.argv[2]

    if to_phone_number and message:
        if send_message_phone(to_phone_number, message):
            print("Message sent")
        else:
            print("Can't send message")
    else:
        print("Requires phone number and message, type help for proper usage")


if __name__ == "__main__":
    initiate()
