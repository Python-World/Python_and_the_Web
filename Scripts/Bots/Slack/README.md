# Python Script for Slack Bot

Slack is the messaging app for teams, like Discord this Slack is being used by organization to communicate, and this Python script will help you to made a bot that connected to Slack

# How to run

Requirements
1. python 3.7
2. pip
3. pipenv

you can use `pipenv install` and run `pipenv run python slackbot.py`

or

install first with `pip install -r requirements.txt`

and then run with command `python slackbot.py`

## Start with creating a new app in slack as a bot

First create your Slack app in the Slack API Control Panel. Log in to your workspace in Slack via a web browser and navigate to the API Control Panel. Now click on the Create an App button.

![](https://assets.digitalocean.com/articles/coinbot/h7VWJOX.png)

Next you’ll be prompted for the name of your app and to select a development Slack workspace. For this tutorial, name your app CoinBot and select a workspace you have admin access to. Once you have done this click on the Create App button

![](https://imgur.com/E4hnhMU.png)

Once your app is created you’ll be presented with the following default app dashboard. This dashboard is where you manage your app by setting permissions, subscribing to events, installing the app into workspaces, and more.

![](https://assets.digitalocean.com/articles/coinbot/ZjFaS1i.png)

In order for your app to be able to post messages to a channel you need to grant the app permissions to send messages. To do this, click the Permissions button in the control panel.

![](https://assets.digitalocean.com/articles/coinbot/IVcN8qg.png)

When you arrive at the OAuth & Permissions page, scroll down until you find the Scopes section of the page. Then find the Bot Token Scopes subsection in the scope and click on Add an OAuth Scope button.

![](https://assets.digitalocean.com/articles/coinbot/wQnTSQr.png)

Click on that button and then type chat:write. Select that permission to add it to your bot. This will allow the app to post messages to channels that it can access. For more information on the available permissions refer to [Slack’s Documentation](https://api.slack.com/scopes).

![](https://assets.digitalocean.com/articles/coinbot/unQYPeL.png)

Now that you’ve added the appropriate permission it is time to install your app into your Slack workspace. Scroll back up on the OAuth & Permissions page and click the Install App to Workspace button at the top.

![](https://assets.digitalocean.com/articles/coinbot/SiSxQB1.png)

Click this button and review the actions that the app can perform in the channel. Once you are satisfied, click the Allow button to finish the installation.

![](https://assets.digitalocean.com/articles/coinbot/lWUBsYR.png)

Once the bot is installed you’ll be presented with a Bot User OAuth Access Token for your app to use when attempting to perform actions in the workspace. Go ahead and copy this token; you’ll need it later.

![](https://assets.digitalocean.com/articles/coinbot/m1M9Ilt.png)

Finally, add your newly installed bot into a channel within your workspace. If you haven’t created a channel yet you can use the #general channel that is created by default in your Slack workspace. Locate the app in the Apps section of the navigation bar in your Slack client and click on it. Once you’ve done that open the Details menu in the top right hand side. If your Slack client isn’t full-screened it will look like an i in a circle.

![](https://assets.digitalocean.com/articles/coinbot/OJ5yTXP.png)

To finish adding your app to a channel, click on the More button represented by three dots in the details page and select Add this app to a channel…. Type your channel into the modal that appears and click Add.

![](https://assets.digitalocean.com/articles/coinbot/ojUMqeI.png)

You’ve now successfully created your app and added it to a channel within your Slack workspace. After you write the code for your app it will be able to post messages in that channel. In the next section you’ll start writing the Python code that will power CoinBot.

## To test your message

run this with include your `SLACK_TOKEN`
```
export SLACK_TOKEN=your-slack-token
```

and then run this command `python slackbot.py`

## Running Your Flask App

Now that you have a functioning application that can send messages to your Slack workspace, you need to create a long running process so your bot can listen to messages sent in the channel and reply to them if the text meets certain criteria. You’re going to use the Python web framework Flask to run this process and listen for events in your channel.

>In this section you will be running your Flask application from a server with a public IP address so that the Slack API can send you events. If you are running this locally on your personal workstation you will need to forward the port from your personal firewall to the port that will be running on your workstation. These ports can be the same, and this tutorial will be set up to use port 3000.


First, add your running application as an authorized handler for your Slackbot.

Navigate to the Basic Information section of your app in the Slack UI. Scroll down until you find the App Credentials section.


![](https://assets.digitalocean.com/articles/coinbot/lLB1jEB.png)

Copy the Signing Secret and export it as the environment variable SLACK_EVENTS_TOKEN:

```
export SLACK_EVENTS_TOKEN="MY_SIGNING_SECRET_TOKEN"
```

With this you have all the necessary API tokens to run your app. Refer to Step 1 if you need a refresher on how to export your SLACK_TOKEN. Now you can start your app and verify that it is indeed running. Ensure that your virtual environment is activated and run the following command to start your Flask app:

```
python3 app.py
```
You will see an output like this:

```
* Serving Flask app "app" (lazy loading)
* Environment: production
  WARNING: This is a development server. Do not use it in a production deployment.
  Use a production WSGI server instead.
* Debug mode: off
* Running on http://0.0.0.0:3000/ (Press CTRL+C to quit)
```

To verify that your app is up, open a new terminal window and curl the IP address of your server with the correct port at /slack/events:

```
curl http://YOUR_IP_ADDRESS:3000/slack/events
```

curl will return the following:

```
Output
These are not the slackbots you're looking for.
```

Receiving the message These are not the slackbots you're looking for., indicates that your app is up and running.

Now leave this Flask application running while you finish configuring your app in the Slack UI.

First grant your app the appropriate permissions so that it can listen to messages and respond accordingly. Click on Event Subscriptions in the UI sidebar and toggle the Enable Events radio button.

![](https://assets.digitalocean.com/articles/coinbot/lLB1jEB.png)

Once you’ve done that, type in your IP address, port, and /slack/events endpoint into the Request URL field. Don’t forget the HTTP protocol prefix. Slack will make an attempt to connect to your endpoint. Once it has successfully done so you’ll see a green check mark with the word Verified next to it.

![](https://assets.digitalocean.com/articles/coinbot/9wqUJwd.png)

Next, expand the Subscribe to bot events and add the message.channels permission to your app. This will allow your app to receive messages from your channel and process them.

![](https://assets.digitalocean.com/articles/coinbot/sCYYhM8.png)

Once you’ve done this you will see the event listed in your Subscribe to bot events section. Next click the green Save Changes button in the bottom right hand corner.

![](https://assets.digitalocean.com/articles/coinbot/NLNbmB4.png)

Once you do this you’ll see a yellow banner across the top of the screen informing you that you need to reinstall your app for the following changes to apply. Every time you change permissions you’ll need to reinstall your app. Click on the reinstall your app link in this banner to reinstall your app.

You’ll be presented with a confirmation screen summarizing the permissions your bot will have and asking if you want to allow its installation. Click on the green Allow button to finish the installation process.

![](https://assets.digitalocean.com/articles/coinbot/KQrNqzK.png)

Now that you’ve done this your app should be ready. Go back to the channel that you installed CoinBot into and send a message containing the phrase `hi`. Your bot will reply. Congrats! You’ve created a Slackbot!

### Refference
https://www.digitalocean.com/community/tutorials/how-to-build-a-slackbot-in-python-on-ubuntu-20-04#prerequisites