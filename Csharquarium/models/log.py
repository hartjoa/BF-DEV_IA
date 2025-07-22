class Log():
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def Log(self, text: str) -> None:
        with open(self.file_path, "a") as file:
            file.write(text + "\n")
            