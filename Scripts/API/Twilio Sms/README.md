# Twilio SMS
This script helps to send SMS messages using Twilio API services.

### Prerequisites
##### Before using this script please create a free trial twilio account,

1. First go to your console, using this [link](https://www.twilio.com/console "Twilio console")
2. Then under the project info, create one phone number, 
3. Use this phone number as the **from** phone number in the script,
4. Then copy your **Account sid** and **Auth token** from the console, and paste it in the appropriate places in the code,
5. Install the packages using, ```pip install -r requirements.txt```.

##### Small note - if you are using trial account, you can only send SMS to your verified phone number, which was used in the account creation,

### How to run the script
1. Now, run your scipt using the python, ```python3 twilio_sms.py <TO PHONE NUMBER> <YOUR MESSAGE>```.
2. ```<TO PHONE NUMBER>``` is the verified phone number, you should mention the country code in front of the phone number like *+278521479630*.
2. Type, ```python3 twilio_sms.py help``` to know more.

### Screenshot/GIF showing the sample use of the script
![Alt Screenshot](/output.png "output")

## *Author Name*
[Ajay-Raj-S](https://www.github.com/Ajay-Raj-S "Ajay")