# slackbot-workout
A fun hack that gets Slackbot to force your teammates to work out!

This is a fork of **[slackbot-workout](https://github.com/brandonshin/slackbot-workout)** created by **[brandonshin](https://github.com/brandonshin)** with a little python cleanup and modifications to handle changes to Slack's API.


<img src = "https://ctrlla-blog.s3.amazonaws.com/2015/Jun/Screen_Shot_2015_06_10_at_5_57_55_PM-1433984292189.png" width = 500>


# Instructions

1. Clone the repo and navigate into the directory in your terminal.

    `$ git clone git@github.com:brandonshin/slackbot-workout.git`

   
2. In the **[Slack API Page](https://api.slack.com)**, Create an app, install it in your workspace, and give it OAuth permissions to list conversations, groups, and user info. Then grab the OAuth user token, which looks like this: `xoxp-2751727432-4028172038-5281317294-3c46b1`. This is your **SLACK_USER_TOKEN_STRING**



3. In the **Slackbot [Remote control Page](https://slack.com/apps/A0F81R8ET-slackbot)**. Register an integration by clicking Add Configuration. __Make sure you grab just the token out of the url__, e.g. `AizJbQ24l38ai4DlQD9yFELb`. This is your **SLACK_URL_TOKEN_STRING**

    
<img src="https://ctrlla-blog.s3.amazonaws.com/2015/Jun/Screen_Shot_2015_06_03_at_8_44_00_AM-1433557565175.png" width = 500>



4. Save your SLACK_USER_TOKEN_STRING and SLACK_URL_TOKEN_STRING in a file called `.env` at the root of the project directory. They should look like this:
   
   `SLACK_USER_TOKEN_STRING=xoxp-2751727432-4028172038-5281317294-3c46b1`
    
   `SLACK_URL_TOKEN_STRING=AizJbQ24l38ai4DlQD9yFELb`
   

   _Notice that the tokens are not enclosed in quotes._


5. Set up channel and customize configurations

    Open `default.json` and set `teamDomain` (ex: ctrlla) `channelName` (ex: general) and `channelId` (ex: B22D35YMS). Save the file as `config.json` in the same directory. Set any other configurations as you like.

    If you don't know the channel ID, fetch it using

    `$ python fetch_channel_id.py channelname`


6. While in the project directory, create a virtual environment (if you like) and run:

    `$ sudo pip install -r requirements.txt`

    `$ python slackbot_exercise.py`


Use ctrl+c to stop the script and log the workouts to `log.csv`.
