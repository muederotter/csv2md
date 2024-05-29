import pyperclip
import logging
import pandas as pd

from src.views.openFile import openFile
from src.tools.csvTools import read_csv


class main:
    def __init__(self, root) -> None:
        self.root = root
        self.dataframe = pd.DataFrame()

        self.run()

    def run(self) -> None:
        """
        Main function of the program.
        """

        # Import .csv file
        self.dataframe = self.importFileContents()

        # Create table and copy to clipboard
        try:
            table = self.createTable()
            pyperclip.copy(table)
            logging.info("Table copied to clipboard")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")
            exit()

    def importFileContents(self) -> dict:
        """
        Import data from a CSV file.
        """
        self.openFile = openFile(self.root)
        file = self.openFile.init_view()

        return read_csv(file)

    def createTable(self) -> str:
        """
        Create a table from the drive data that can be pasted into confluence.
        """
        table = ""

        # Create header
        for column_name in self.dataframe.columns:
            table += f"| {column_name} "
        table += "|\n"

        # Iterate through all rows and cells
        for index, row in self.dataframe.iterrows():

            if index == 0:
                for column_name in self.dataframe.columns:
                    table += f"| ----------- "
                table += "|\n"

            for column_name in self.dataframe.columns:
                cell_value = row[column_name]
                table += f"| {cell_value} "
            table += "|\n"

        return table
