from tkinter import filedialog
import logging


class openFile:
    """
    Class to create the open file dialog window for a CSV file.
    """
    def __init__(self, parent):
        self.parent = parent
        self.openFile_window = None

    def init_view(self) -> str:
        """
        Creates the open file dialog window for a CSV file and returns the file path.
        If no file is selected, the program exits.
        """
        # Create the open file dialog window
        self.file = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])

        # Check if a file was selected
        if self.file:
            logging.info(f"Selected file: {self.file}")
            return self.file
        else:
            logging.error("No file selected. Program will exit.")
            exit()
