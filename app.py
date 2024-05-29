import logging
from tkinter import Tk
import src.main as main

VERSION = "1.0.0"

class App:
    def __init__(self) -> None:

        # Create and hide root window to enable askopenfilename dialog
        self.root = Tk()
        self.root.withdraw()

        # Run main
        main.main(self.root)


if __name__ == "__main__":
    # configure logging
    logging.basicConfig(
        filename="csv2md.log",
        level=logging.INFO,
        format="%(asctime)s:%(levelname)s:%(message)s",
    )

    logging.info(f"Application started. Version {VERSION}")
    app = App()
