import requests
import os

SHEETBEST_USERS_ENDPOINT = f"{os.environ['SHEETBEST_ENDPOINT']}/tabs/users"

class UserInformation:
    def __init__(self):
        self.first_name = input("What is your name? ")
        self.last_name = input("What's your last name? ")
        self.email = "an email should be here"
        self.check_an_email()
        self.write_to_sheet()

    def check_an_email(self):
        self.email = input("What's your email? ")
        self.email_validation = input("Type your email again. ")
        if self.email == self.email_validation:
            pass
        else:
            print("\nYour emails doesn't match! Try again!\n")
            self.check_an_email()

    def write_to_sheet(self):
        sheetbest_body = {
            "First Name": self.first_name,
            "Last Name": self.last_name,
            "Email": self.email_validation
        }
        response = requests.post(SHEETBEST_USERS_ENDPOINT, json=sheetbest_body)
        try:
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            print("Something went wrong, restart the code! :с")
        else:
            print("Yay, you've entered the club! :)")



