import yaml

class Config:
    def __init__(self, path):
        with open(path, 'r') as config_yaml:
            self.config = yaml.safe_load(config_yaml)

    def getconfig(self, cfg = "config_app"):
        return self.config[cfg]