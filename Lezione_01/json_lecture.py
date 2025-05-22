import json

PATH: str = "Lezione_01/config.json"
mode: str = "r"
encoding:str = "utf-8"

with open(PATH, mode, encoding=encoding) as file:

    config: dict = json.load(file)

config["Aggiunta"] = "Nuovo"
config["server"]["host"] = "google.it"

with open(PATH, mode="w", encoding=encoding) as file:

    json.dump(config, file, indent=4)


print(f"Host: {config["server"]["host"]} Port:{config["server"]["port"]}")