import os
import requests
import json
import datetime
from dotenv import load_dotenv


# Environment variables must be set with your tokens
load_dotenv()
USER_TOKEN_STRING = os.environ["SLACK_USER_TOKEN_STRING"]


class User:
    def __init__(self, user_id):
        # The Slack ID of the user
        self.id = user_id

        # The username (@username) and real name
        self.username, self.real_name = self.fetch_names()

        # A list of all exercises done by user
        self.exercise_history = []

        # A record of all exercise totals (quantity)
        self.exercises = {}

        # A record of exercise counts (# of times)
        self.exercise_counts = {}

        # A record of past runs
        self.past_workouts = {}

        print("New user: " + self.real_name + " (" + self.username + ")")

    def store_session(self, run_name) -> None:
        try:
            self.past_workouts[run_name] = self.exercises
        except:
            self.past_workouts = {}

        self.past_workouts[run_name] = self.exercises
        self.exercises = {}
        self.exercise_counts = {}

    def fetch_names(self) -> tuple:
        params = {"token": USER_TOKEN_STRING, "user": self.id}
        response = requests.get("https://slack.com/api/users.info", params=params)
        user_obj = json.loads(response.text, encoding="utf-8")["user"]

        username = user_obj["name"]
        real_name = user_obj["profile"]["real_name"]

        return username, real_name

    def get_user_handle(self) -> str:
        return "@" + self.username

    def is_active(self) -> bool:
        """
        Returns true if a user is currently "active", else false
        """
        try:
            params = {"token": USER_TOKEN_STRING, "user": self.id}
            response = requests.get(
                "https://slack.com/api/users.getPresence", params=params
            )
            status = json.loads(response.text, encoding="utf-8")["presence"]

            return status == "active"

        except requests.exceptions.ConnectionError:
            print("Error fetching online status for " + self.get_user_handle())
            return False

    def add_exercise(self, exercise, reps) -> None:
        # Add to total counts
        self.exercises[exercise["id"]] = self.exercises.get(exercise["id"], 0) + reps
        self.exercise_counts[exercise["id"]] = (
            self.exercise_counts.get(exercise["id"], 0) + 1
        )

        # Add to exercise history record
        self.exercise_history.append(
            [
                datetime.datetime.now().isoformat(),
                exercise["id"],
                exercise["name"],
                reps,
                exercise["units"],
            ]
        )

    def has_done_exercise(self, exercise) -> str:
        return exercise["id"] in self.exercise_counts
