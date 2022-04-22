#!/usr/bin/python3

"""Run this program in a specified directory that needs cleaning up. The
program parses arguments from the terminal to get the path to a specified
directory and scans all files in that directory. The program checks each file's
suffix with the dictionary of file formats, creates a new folder for the
specified file format if necessary and moves the file according to its format
into an appropriate directory. The program does not sort subdirectories."""

import os
import argparse
from pathlib import Path

Directories = {
               "HTML": [".html5", ".html", ".htm", ".xhtml"],
               "Images": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png",
                          ".bpg", "svg", ".heif", ".psd"],
               "Videos": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm",
                          ".vob", ".mng", ".qt", ".mpg", ".mpeg", ".3gp"],
               "Documents": [".oxps", ".epub", ".pages", ".docx", ".doc",
                             ".fdf", ".ods", ".odt", ".pwi", ".xsn", ".xps",
                             ".dotx", ".docm", ".dox", ".rvg", ".rtf",
                             ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                             "pptx"],
               "Archives": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz",
                            ".7z", ".dmg", ".rar", ".xar", ".zip"],
               "Audio": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p",
                         ".mp3", ".msv", "ogg", "oga", ".raw", ".vox", ".wav",
                         ".wma"],
               "Plaintext": [".txt", ".in", ".out"],
               "PDF": [".pdf"],
               "XML": [".xml"],
               "EXE": [".exe"],
               "SHELL": [".sh"]
               }

File_Format_Dictionary = {
                          file_format: directory
                          for directory, file_formats in Directories.items()
                          for file_format in file_formats
                          }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('dir', type=str, help='Directory path')
    args = parser.parse_args()
    # Get an absolute path to the directory to clean up
    abs_dir_path = Path(args.dir).resolve()
    for entry in os.scandir(abs_dir_path):
        # Ignore already existing directories
        if entry.is_dir():
            continue
        file_path = Path(entry)
        file_format = file_path.suffix.lower()
        if file_format in File_Format_Dictionary:
            # Create the destination directory
            destination_dir = Path(abs_dir_path.joinpath
                                   (File_Format_Dictionary[file_format]))
            destination_dir.mkdir(exist_ok=True)
            # Move the file into the destination directory
            file_path.rename(destination_dir.joinpath(entry.name))


if __name__ == "__main__":
    main()
