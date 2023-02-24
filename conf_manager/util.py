import yaml


def load_account_conf(conf_path):
    with open(conf_path, "r") as file:
        return yaml.safe_load(file)
