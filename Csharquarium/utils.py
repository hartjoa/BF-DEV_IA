from colorama import Fore, init
init(autoreset=True)

class Utils:
    @staticmethod
    def nice_print(message: str, fore: str=Fore.BLACK) -> None:
        print(f"{fore}{message}")


