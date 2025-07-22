from colorama import Fore, init
init(autoreset=True)

class Utils:
    @staticmethod
    def nice_print(message, fore=Fore.BLACK):
        print(f"{fore}{message}")


