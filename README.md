# File Sorter

Let this program sort your files according to their file format!

## General info

This program parses arguments from the terminal to get the path to a specified
directory and scans all files in that directory. The program checks each file's
suffix with the dictionary of file formats, creates a new folder for the
specified file format if necessary and moves the file according to its format
into an appropriate directory. The program does not sort subdirectories.

Categories:
- HTML
- Images
- Videos
- Documents
- Archives
- Audio
- Plaintext
- PDF
- XML
- EXE
- SHELL

## Technology

- Python 3.8

## Usage

Using the terminal run the program and provide a path to the directory as 
a parameter:

```python clean_my_dir.py "/path/to/directory"```

### Example usage:

In this use case we will sort files in the test_files directory attached to 
this repository.

Run the program using the terminal:

```python clean_my_dir.py "./test_files"```

Enjoy a well-organized directory!
