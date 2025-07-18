class Log():
    def __init__(self, file_path):
        self.file_path = file_path

    def Log(self, text):
        with open(self.file_path, "a") as file:
            file.write(text + "\n")
            