# csv2md

Convert a CSV file into a Markdown table.

## Installation

To install the program, follow these steps:

1. Download the file `csv2md.zip` from the releases section.
1. Unzip the file into a non-temporary directory of your choice.
1. _(Optional)_ Create a shortcut for `csv2md.exe` and move it to your desktop for easy access.
1. Run `csv2md.exe`.

## Prerequisites

Follow this quick guide to understand how the program works.

- Windows OS

## Using the program

If you want to know, how the program works, follow this quick guide.

### Running the Program

1. Launch `csv2md.exe`.
1. The program will prompt you to select a compatible CSV file.
1. Once selected, the program will convert the CSV data into Markdown table format and copy it to your clipboard.

### Create the table in Markdown

#### .md

Simply paste the copied text into your `.md` file.

#### Confluence

1. Open Confluence and create a new page.
1. Press `ctrl`+`shift`+`d` to open the markup window.
1. Paste the copied text into the markup window to create the table.

## Example

### Input CSV

Example `data.csv` file:

```csv
Name,Age,City
Alice,30,New York
Bob,25,Los Angeles
Charlie,35,Chicago
```

### Output Markdown

After running the program and pasting, you should get:

| Name    | Age | City        |
| ------- | --- | ----------- |
| Alice   | 30  | New York    |
| Bob     | 25  | Los Angeles |
| Charlie | 35  | Chicago     |

## License

This project is licensed under the MIT License. See the LICENSE file for details.
