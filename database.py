import datetime, json


class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.load()

    def load(self):
        with open(self.filename) as file:
            self.users = json.load(file)

    def get_user(self, email):
        if email in self.users:
            return self.users[email]
        else:
            return None

    def add_user(self, email, password, name):
        if email.strip() not in self.users:
            self.users[email.strip()] = (password.strip(), name.strip(), DataBase.get_date())
            self.save()
            return 1
        else:
            print("Email exists already")
            return -1

    def validate(self, email, password):
        if self.get_user(email) != None:
            return self.users[email][0] == password
        else:
            return False

    def save(self):
        with open(self.filename, "w") as file:
            json.dump(self.users, file)

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]