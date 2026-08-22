def log_error(message):
    with open("logs.txt", "a", encoding="utf-8") as file:
        file.write(f"{message}\n")
