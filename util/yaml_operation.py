import yaml


class YamlOperation:
    def __init__(self, locator_file):
        with open(locator_file) as file:
            self.data = yaml.load(file, yaml.FullLoader)

    def get_locator(self, page, local):
        return self.data[page][local]
