import json


class Config:
    def __init__(self):
        config = open("config.json", "r")
        config = json.load(config)

        self.token = config["Bot"]["Token"]
        self.prefix = config["Bot"]["Prefix"]
        self.description = config["Bot"]["Description"]
        self.status = config["Bot"]["Status"]
        self.color = config["Bot"]["Color"]
        self.icon = config["Bot"]["Icon"]

        self.guild = config["guild"]
        self.log = config["log"]
        self.save = config["save"]
